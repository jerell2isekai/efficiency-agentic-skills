#!/usr/bin/env python3
"""Verify Taiwan official legal sources from law.moj.gov.tw.

This helper gives the skill a deterministic way to check:
- law name
- revision date
- effective status / pending-effective note
- whether requested article numbers are present on the official law page

Default transport is `auto`, which prefers curl and falls back to agent-browser.
"""

from __future__ import annotations

import argparse
import json
import re
import secrets
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from html import unescape
from typing import Iterable
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse


LAW_HOST = "law.moj.gov.tw"
LAW_ALL_PATH = "/LawClass/LawAll.aspx"


class VerificationError(RuntimeError):
    """Raised when official-source verification cannot complete safely."""


@dataclass
class ArticleCheck:
    article: str
    found: bool
    evidence: str | None


@dataclass
class VerificationResult:
    url: str
    transport: str
    law_name: str | None
    pcode: str | None
    revision_date: str | None
    effective_status: str | None
    has_pending_effective_note: bool
    pending_effective_note: str | None
    article_checks: list[ArticleCheck]
    warnings: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify official Taiwan legal sources from law.moj.gov.tw."
    )
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--url", help="Official law.moj.gov.tw URL to verify.")
    target.add_argument("--pcode", help="PCode to verify, e.g. I0050021.")
    parser.add_argument(
        "--article",
        action="append",
        default=[],
        help="Article number to verify, e.g. 8 or 13-1. Repeat as needed.",
    )
    parser.add_argument(
        "--transport",
        choices=("auto", "curl", "agent-browser"),
        default="auto",
        help="Fetch transport. Default: auto.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=20,
        help="Network timeout in seconds per command. Default: 20.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of human-readable text.",
    )
    return parser.parse_args()


def normalize_target_url(raw_url: str | None, pcode: str | None) -> tuple[str, str | None]:
    if pcode:
        clean_pcode = pcode.strip()
        if not clean_pcode:
            raise VerificationError("PCode cannot be empty.")
        return f"https://{LAW_HOST}{LAW_ALL_PATH}?{urlencode({'PCode': clean_pcode})}", clean_pcode

    assert raw_url is not None
    parsed = urlparse(raw_url.strip())
    if parsed.scheme != "https":
        raise VerificationError("Only https:// URLs are allowed.")
    if parsed.netloc.lower() != LAW_HOST:
        raise VerificationError("Only law.moj.gov.tw URLs are allowed.")

    query = parse_qs(parsed.query)
    pcode_values = query.get("PCode") or query.get("pcode") or []
    normalized_query: list[tuple[str, str]] = []
    normalized_pcode = pcode_values[0] if pcode_values else None
    if normalized_pcode:
        normalized_query.append(("PCode", normalized_pcode))

    normalized = urlunparse(
        (
            "https",
            LAW_HOST,
            parsed.path or LAW_ALL_PATH,
            "",
            urlencode(normalized_query),
            "",
        )
    )
    return normalized, normalized_pcode


def require_command(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise VerificationError(f"Required command not found: {name}")
    return path


def run_command(command: list[str], timeout: int) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )


def fetch_with_curl(url: str, timeout: int) -> str:
    require_command("curl")
    result = run_command(
        [
            "curl",
            "--fail",
            "--silent",
            "--show-error",
            "--location",
            "--max-time",
            str(timeout),
            url,
        ],
        timeout=timeout + 5,
    )
    if result.returncode != 0:
        stderr = result.stderr.strip() or "curl failed without stderr"
        raise VerificationError(f"curl fetch failed: {stderr}")
    return result.stdout


def fetch_with_agent_browser(url: str, timeout: int) -> str:
    require_command("agent-browser")
    session_name = f"taiwan-legal-doc-{secrets.token_hex(4)}"
    commands = [
        ["agent-browser", "--session-name", session_name, "open", url],
        ["agent-browser", "--session-name", session_name, "wait", "--load", "networkidle"],
        ["agent-browser", "--session-name", session_name, "snapshot", "-s", "body"],
    ]
    try:
        for command in commands[:-1]:
            result = run_command(command, timeout=timeout + 10)
            if result.returncode != 0:
                stderr = result.stderr.strip() or result.stdout.strip() or "agent-browser failed"
                raise VerificationError(f"agent-browser failed: {stderr}")

        snapshot = run_command(commands[-1], timeout=timeout + 10)
        if snapshot.returncode != 0:
            stderr = snapshot.stderr.strip() or snapshot.stdout.strip() or "agent-browser snapshot failed"
            raise VerificationError(f"agent-browser snapshot failed: {stderr}")
        return snapshot.stdout
    finally:
        close_result = run_command(
            ["agent-browser", "--session-name", session_name, "close"],
            timeout=10,
        )
        _ = close_result


def fetch_source(url: str, requested_transport: str, timeout: int) -> tuple[str, str]:
    if requested_transport == "curl":
        return fetch_with_curl(url, timeout), "curl"
    if requested_transport == "agent-browser":
        return fetch_with_agent_browser(url, timeout), "agent-browser"

    try:
        return fetch_with_curl(url, timeout), "curl"
    except VerificationError as curl_error:
        try:
            content = fetch_with_agent_browser(url, timeout)
            return content, "agent-browser"
        except VerificationError as browser_error:
            raise VerificationError(
                f"Unable to verify via curl or agent-browser. curl={curl_error}; agent-browser={browser_error}"
            ) from browser_error


def collapse_ws(value: str | None) -> str | None:
    if value is None:
        return None
    without_tags = re.sub(r"<[^>]+>", " ", value)
    without_entities = unescape(without_tags).replace("\xa0", " ")
    return re.sub(r"\s+", " ", without_entities).strip()


def extract_with_patterns(text: str, patterns: Iterable[re.Pattern[str]]) -> str | None:
    for pattern in patterns:
        match = pattern.search(text)
        if match:
            return collapse_ws(unescape(match.group(1)))
    return None


def parse_law_name(text: str) -> str | None:
    return extract_with_patterns(
        text,
        [
            re.compile(r'id="hlLawName"[^>]*>([^<]+)<', re.IGNORECASE),
            re.compile(r'rowheader "法規名稱：".*?cell "([^"]+?) EN"', re.DOTALL),
            re.compile(r'link "([^"]+)" \[ref=.*?\]\s*$', re.MULTILINE),
        ],
    )


def parse_revision_date(text: str) -> str | None:
    return extract_with_patterns(
        text,
        [
            re.compile(r"修正日期：</th>\s*<td[^>]*>\s*([^<]+)\s*</td>", re.IGNORECASE),
            re.compile(r'rowheader "修正日期：".*?cell "([^"]+)"', re.DOTALL),
        ],
    )


def parse_effective_status(text: str) -> str | None:
    return extract_with_patterns(
        text,
        [
            re.compile(r"生效狀態：\s*</th>\s*<td[^>]*>\s*(.*?)\s*</td>", re.IGNORECASE | re.DOTALL),
            re.compile(r'rowheader "生效狀態：".*?cell "([^"]+)"', re.DOTALL),
        ],
    )


def article_patterns(article: str) -> list[re.Pattern[str]]:
    escaped = re.escape(article)
    return [
        re.compile(rf"flno={escaped}(?:[\"&'])", re.IGNORECASE),
        re.compile(rf'name="{escaped}"', re.IGNORECASE),
        re.compile(rf"第\s*{escaped}\s*條"),
        re.compile(rf'link "第\s*{escaped}\s*條"'),
    ]


def extract_article_evidence(text: str, article: str) -> str | None:
    for line in text.splitlines():
        if re.search(rf"第\s*{re.escape(article)}\s*條", line):
            return collapse_ws(unescape(re.sub(r"<[^>]+>", " ", line)))
    return None


def parse_result(url: str, transport: str, text: str, pcode: str | None, articles: list[str]) -> VerificationResult:
    effective_status = parse_effective_status(text)
    pending_note = effective_status if effective_status and "尚未生效" in effective_status else None
    law_name = parse_law_name(text)
    warnings: list[str] = []

    if not law_name:
        warnings.append("Could not parse law name from official source output.")
    if not parse_revision_date(text):
        warnings.append("Could not parse revision date from official source output.")

    article_checks = []
    for article in articles:
        found = any(pattern.search(text) for pattern in article_patterns(article))
        article_checks.append(
            ArticleCheck(
                article=article,
                found=found,
                evidence=extract_article_evidence(text, article),
            )
        )
        if not found:
            warnings.append(f"Requested article not found on page: 第 {article} 條")

    return VerificationResult(
        url=url,
        transport=transport,
        law_name=law_name,
        pcode=pcode,
        revision_date=parse_revision_date(text),
        effective_status=effective_status,
        has_pending_effective_note=bool(pending_note),
        pending_effective_note=pending_note,
        article_checks=article_checks,
        warnings=warnings,
    )


def render_text(result: VerificationResult) -> str:
    lines = [
        f"Verification: {'success' if not result.warnings else 'success_with_warnings'}",
        f"URL: {result.url}",
        f"Transport: {result.transport}",
        f"Law Name: {result.law_name or '[unparsed]'}",
        f"PCode: {result.pcode or '[unknown]'}",
        f"Revision Date: {result.revision_date or '[unparsed]'}",
        f"Effective Status: {result.effective_status or '[unparsed]'}",
        f"Pending Effective Note: {'yes' if result.has_pending_effective_note else 'no'}",
    ]

    if result.article_checks:
        lines.append("Article Checks:")
        for check in result.article_checks:
            status = "found" if check.found else "missing"
            evidence = f" | evidence: {check.evidence}" if check.evidence else ""
            lines.append(f"- 第 {check.article} 條: {status}{evidence}")

    if result.warnings:
        lines.append("Warnings:")
        for warning in result.warnings:
            lines.append(f"- {warning}")

    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    try:
        url, pcode = normalize_target_url(args.url, args.pcode)
        raw_text, transport = fetch_source(url, args.transport, args.timeout)
        result = parse_result(url, transport, raw_text, pcode, args.article)
    except VerificationError as exc:
        print(f"Verification failed: {exc}", file=sys.stderr)
        return 2
    except subprocess.TimeoutExpired as exc:
        print(f"Verification failed: command timed out: {exc.cmd}", file=sys.stderr)
        return 2

    if args.json:
        print(
            json.dumps(
                {
                    **asdict(result),
                    "article_checks": [asdict(check) for check in result.article_checks],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(render_text(result))

    return 0


if __name__ == "__main__":
    sys.exit(main())
