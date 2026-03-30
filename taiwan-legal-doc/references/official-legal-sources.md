# Official Legal Sources for Taiwan Verification

Use this reference whenever the output depends on statute names, article numbers, current law status, or whether a legal proposition is still in force.

## Table of Contents

1. [Purpose](#1-purpose)
2. [Source hierarchy](#2-source-hierarchy)
3. [When verification is mandatory](#3-when-verification-is-mandatory)
4. [Verification workflow](#4-verification-workflow)
5. [Downgrade rules](#5-downgrade-rules)
6. [Citation style](#6-citation-style)
7. [Output requirement](#7-output-requirement)

## 1. Purpose

Do not rely on memory or local summaries for Taiwan legal citations when the output asserts a legal requirement.

Use `law.moj.gov.tw` as the primary source of truth.

## 2. Source Hierarchy

Use this order:

1. `https://law.moj.gov.tw`
   - `中央法規` for laws and regulations
   - `跨機關檢索` when the issue depends on administrative rules
2. User-provided official legal text or screenshots from the official source
3. Local skill references such as `tw-legal-framework.md`
4. General drafting heuristics or market practice

If the official source conflicts with local references, the official source wins.

## 3. When Verification Is Mandatory

Official verification is mandatory when:

- citing a law name and article number
- describing a mandatory notice item or statutory element
- describing civil or criminal penalties
- saying a rule is current, amended, repealed, or still effective
- relying on Enforcement Rules, delegated regulations, or administrative rules
- answering any request that uses words such as `最新`, `現行`, `目前`, `是否已修正`

Official verification is still recommended, but not always mandatory, when:

- explaining pure drafting preferences
- discussing negotiation posture
- discussing enforceability risk without pinning it to a precise article

## 4. Verification Workflow

1. Identify whether the point is:
   - `法律要求`
   - `可執行性風險`
   - `實務偏好`
2. If it is `法律要求`, search the official source first.
3. Confirm:
   - law name
   - article number
   - revision date
   - effective status
   - whether the text still appears as stated
   - whether it is a law, enforcement rule, or administrative rule
4. Only then present the point as a verified legal basis.
5. If the point is about administrative rules and it does not appear in `中央法規`, check `跨機關檢索`.

Deterministic helper:

- Run `python3 scripts/verify_official_legal_source.py --pcode <PCode> --article <n>` when you want a repeatable pre-citation check.
- Default transport is `auto`, which prefers `curl` and falls back to `agent-browser`.
- Use `--transport agent-browser` when browser-rendered text is easier to inspect than raw page source.

If the official page shows `部分或全部條文尚未生效` or another pending-effective note:

- do not assume the newest amendment is already applicable
- distinguish `已公布但未生效` from `現行有效`
- when necessary, say the law is in transition and identify whether your conclusion relies on the currently effective text or a pending amendment

## 5. Downgrade Rules

If official verification is unavailable:

- say the point is based on local working references only
- say official confirmation is still needed
- avoid asserting article numbers as certain

Good wording:

- `依本 skill 內部參考資料初步判斷，仍需再以法務部全國法規資料庫確認。`
- `此處目前先作為可執行性風險提示，不作確定條號判斷。`

Bad wording:

- fabricated article numbers
- confident "現行法明定" claims without verification
- long verbatim statutory text quoted from memory

## 6. Citation Style

Preferred citation wording in findings:

- `個人資料保護法第 8 條（已依 law.moj.gov.tw 驗證）`
- `個人資料保護法施行細則第 8 條（已依 law.moj.gov.tw 驗證）`
- `營業秘密法第 2 條（已依 law.moj.gov.tw 驗證）`
- `民法第 252 條（已依 law.moj.gov.tw 驗證）`

If the output format allows links, prefer linking to the official page rather than a third-party summary.

## 7. Output Requirement

After drafting or reviewing a contract, always append a `法條來源（官方）` section.

Rules:

- List every statute actually cited in the output or contract notes
- Use `law.moj.gov.tw` URLs only
- One law page URL may cover multiple cited articles from the same law
- If no statute is cited, say `本次輸出未直接引用具體法條`
- Do not fabricate deep links or article URLs that were not verified

Recommended format:

```md
### 法條來源（官方）
- 個人資料保護法第 3 條、第 8 條: https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=I0050021
- 個人資料保護法施行細則第 8 條: https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=I0050022
- 營業秘密法第 2 條: https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=J0080028
```
