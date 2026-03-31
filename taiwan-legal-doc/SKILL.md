---
name: taiwan-legal-doc
description: |
  Draft, triage, review, redline, revise, or add clauses to Taiwan (R.O.C.) commercial and employment legal documents, especially NDAs (保密協議), personal data consent forms (個資同意書), consultant/service agreements (顧問合約/服務合約), IP assignment agreements (著作權讓與/智財權歸屬), portrait/likeness authorizations (肖像授權), employment contracts (勞動契約/僱傭合約), non-compete agreements (競業禁止), and combined instruments. Use when the user asks to draft, review, redline, revise, or insert clauses into a specific Taiwan commercial or employment document, provides a PDF/DOCX/text contract for Taiwan-focused analysis, wants quick risk triage, or wants clause-by-clause replacement language. Also trigger when 個資法, 營業秘密法, 著作權法, 勞基法, 勞動基準法, 勞動契約, 僱傭合約, 資遣費, 加班費, 競業禁止, 保密條款, 違約金條款, contract review, NDA review, employment contract, 合約審查, redline, or clause insertion are mentioned in the context of a concrete document. Do NOT use for litigation, court filings, family law, criminal defense, tax law, immigration, or abstract legal Q&A unrelated to drafting or reviewing a specific Taiwan document.
---

# Taiwan Legal Document Drafter & Reviewer

Handle Taiwan-focused commercial and employment legal documents. Keep the skill narrow: draft documents, insert clauses, triage incoming contracts, redline visible text, and review concrete documents for Taiwan use. Do not drift into general legal research or non-Taiwan practice unless the user explicitly asks for cross-border comparison.

**Important**: Produce AI-assisted drafts and reviews only. Advise the user to have a licensed Taiwan attorney (台灣執業律師) review any document before signature, filing, or live use.

## Core Rules

1. Keep Taiwan law as the governing baseline unless the user explicitly chooses another jurisdiction.
2. Treat `https://law.moj.gov.tw` as the primary source for Taiwan legal requirements, article numbers, and current law status. Treat local references in this skill as secondary working summaries, not final citation authority.
3. **Every mode — including Quick Triage and Draft — must run `scripts/verify_official_legal_source.py` (or direct `curl` to `law.moj.gov.tw`) for every statute or article it mentions, references, or relies on.** No exception. If the verification script is unreachable or the article cannot be confirmed, the output must say so explicitly and mark the citation as `未驗證`. Do not present any article number as confirmed without a successful verification call.
4. Distinguish **法律要求** from **drafting preferences**. Cite statutes only after official-source verification. Label non-statutory points as typical, preferred, risk-reducing practice, or negotiation posture.
5. Prefer the user's contract playbook or fallback positions when provided, but never let internal preference override Taiwan law or enforceability constraints.
6. Do not invent missing parties, courts, dates, attachments, or clause text you have not seen. Use `[待填]` placeholders when the user asks you to proceed without complete information.
7. If the request is really litigation, dispute strategy, tax planning, or abstract legal Q&A, say this skill is out of scope instead of stretching it.
8. After finishing contract drafting or review, always append a `法條來源（官方）` section listing every statute cited in the output or contract notes, with `law.moj.gov.tw` source URLs. If no statute is cited, say so explicitly.

## Mode Selection

Choose the lightest mode that matches the request:

| Mode | Use when | Output |
|---|---|---|
| `Quick Triage` | The user wants a fast first-pass risk read on an incoming document | Green / Yellow / Red routing with a short risk summary and escalation advice |
| `Full Review` | The user wants clause-level findings, revisions, negotiation notes, or a formal review | Structured review with severity-tagged findings and rewrite suggestions |
| `Redline` | The user wants clause-by-clause replacement language or markup-ready revisions against visible text | Redline report with current text, proposed replacement, rationale, and negotiation posture |
| `Draft` | The user wants a new Taiwan-use document from scratch | Structured markdown or `.docx` draft with placeholders where needed |
| `Clause Insert` | The user wants one or more clauses added or replaced in an existing document | Clause text, placement advice, and conflict/integration notes |

## Workflow

### Step 1: Scope the Task

Establish these items before writing or reviewing:

1. **Document type** — NDA, consent form, service agreement, consultant agreement, IP assignment, portrait authorization, employment contract (勞動契約/僱傭合約), non-compete agreement, or combined instrument
2. **Parties and roles** — company legal name, counterparty role, and whether the user is protecting the discloser, the recipient, the buyer, the vendor, or a neutral form
3. **Subject matter** — what services, information, personal data, IP, likeness, or deliverables are involved
4. **Jurisdiction** — default to Taiwan law and a specific Taiwan district court unless the user says otherwise
5. **Working mode** — quick triage, full review, redline, draft, or clause insert

### Step 2: Run the Clarification Gate

Before producing output, check whether enough information is available.

**For `Draft`:**
- Ask for company legal name
- Ask for counterparty role
- Ask for subject matter
- Ask for jurisdiction / preferred district court

If the user explicitly wants an immediate draft without answering, proceed with `[待填]` placeholders and append an `Assumptions Block` listing every missing fact.

**For `Full Review`:**
- Review only the document text actually provided
- Cite the clause location or visible section for every finding
- State clearly when a file is partial, unreadable, image-only, or missing appendices

**For `Clause Insert`:**
- Confirm where the clause should sit
- Check for conflicts with existing definitions, liability, confidentiality, IP, or governing law clauses

**For `Redline`:**
- Confirm whether the user wants strict replacement wording, negotiation fallback options, or both
- Limit markup to text you can actually see; if the source is partial or OCR-poor, switch to proposed replacement blocks instead of pretending you can patch invisible wording
- If tracked changes or revision state are unclear, say you are providing `redline-ready wording` rather than a definitive line-by-line markup

### Step 3: Ingest the Document Correctly

When the user provides a PDF, DOCX, scan, pasted text, or partial excerpt, follow `references/document-intake.md`.

Use these intake rules:

- If the document is attached or file-based, extract structure first: title, parties, sections, definitions, signature block, appendices.
- If the document is incomplete, downgrade confidence and say what you could not assess.
- If the document appears to be OCR-poor, image-only, or missing tracked changes context, say so before offering clause-level conclusions.
- When quoting or citing, reference the visible section heading, article number, or nearby text snippet.

### Step 4: Determine the Governing Legal Baseline

Read `references/tw-legal-framework.md` for Taiwan commercial law issue-spotting. For employment/labor contracts, also read `references/tw-labor-framework.md`. Use them to identify which statutes matter:

- 個資法 / 施行細則
- 營業秘密法
- 著作權法
- 民法違約金與一般契約原則
- 勞動基準法 / 勞工退休金條例 / 性別平等工作法 / 就業服務法 / 職業安全衛生法 (for employment documents)

Before presenting any **法律要求**, article number, or "current law" claim, follow `references/official-legal-sources.md` and verify against the official source at `law.moj.gov.tw`.

When deterministic verification helps, run `scripts/verify_official_legal_source.py` with the official law page URL or `PCode` before citing the point in the output.

### Step 4A: Verify the Official Legal Source

Use `references/official-legal-sources.md` whenever the output will include law names, article numbers, penalty ranges, enforcement-rule requirements, or "latest / current" statements.

Mandatory verification cases:

- Any finding whose `法律依據` relies on a statute or article number
- Any statement about current law, amendments, effective status, or whether a rule is still in force
- Any criminal / civil penalty statement
- Any claim about Enforcement Rules, delegated regulations, or administrative rules

Verification rules:

1. Use `law.moj.gov.tw` as the primary source
2. Use `中央法規` for laws and regulations; use `跨機關檢索` when the issue turns on administrative rules
3. Confirm the law name, article number, `修正日期`, `生效狀態`, and whether the local reference still matches the official text
4. If the page shows pending amendments or partial non-effective text, do not assume the amended text is already current
5. If the official source conflicts with local references, the official source wins
6. If you cannot verify the official source, do not present the point as a definite legal requirement

Deterministic helper:

- Prefer `python3 scripts/verify_official_legal_source.py --pcode <PCode> --article <n>`
- Default transport is `auto`, which tries `curl` first and falls back to `agent-browser`
- Use `--transport agent-browser` when the page is readable in browser automation but `curl` is insufficient for the verification task
- Capture the verified law page URL from the script output for the final `法條來源（官方）` section

When verification genuinely fails (network error, page not found, ambiguous result), use these labels — but treat them as last-resort fallbacks, not convenient shortcuts to skip verification:

- Fallback: `依本 skill 內部參考資料初步判斷（未驗證）`
- Fallback: `需再以法務部全國法規資料庫確認（驗證失敗）`
- Never allowed: fabricated article numbers, confident "現行法就是如此" claims, or fake statutory quotes
- Never allowed: skipping the verification call entirely because the mode is "quick" or "draft"

When the output cites a verified statute, capture the official law page URL for the final `法條來源（官方）` section.

If the request concerns workflow rather than black-letter law, also load:

- `references/review-triage.md` for quick routing
- `references/review-playbook.md` when business fallback positions or negotiation posture matter
- `references/clause-risk-patterns.md` for clause design and red-flag patterns

If the user has a legal playbook or wants review calibrated to internal standards:

1. Look for `.claude/legal.local.md` in the current repo or shared workspace
2. If found, treat it as the highest-priority business posture source after Taiwan law
3. If not found, use `references/legal-local-playbook-template.md` as the expected schema and say defaults are being used instead of inventing positions

### Step 5: Produce the Result

#### `Quick Triage`

Use this when the user wants a fast decision, not a full markup. Speed does not override accuracy — every statute referenced in the triage output must be verified against `law.moj.gov.tw` before the output is finalized.

Run `scripts/verify_official_legal_source.py` for each statute or article number that informs the risk rating, escalation advice, or immediate-action recommendation. Include the verified URLs in the `法條來源（官方）` section. If a statute cannot be verified, mark it as `（未驗證）` and note the verification failure.

Output:

```md
## 初步分流

- 風險等級: Green / Yellow / Red
- 一句結論: ...
- 關鍵風險: ...
- 是否建議升級 Full Review: yes / no
- 原因: ...
- 立即處理建議: ...

### 法條來源（官方）
- [法規名稱 + 相關條號]: [law.moj.gov.tw URL]
```

Load `references/review-triage.md` first.

Even in Quick Triage, the risk assessment almost always touches on at least one statute (個資法, 營業秘密法, 著作權法, or 民法). Identify and verify them. If after thorough analysis the triage genuinely cites no statute, include:

```md
### 法條來源（官方）
- 本次輸出未直接引用具體法條。
```

#### `Full Review`

Use the review playbook and give concrete findings.

Output:

```md
## 審查報告：[Document Name]

### 整體評估
[1-2 sentence summary]

### Findings

#### [P0/P1/P2/P3] — [Short title]
- **條款位置**: [Article / section / nearby snippet]
- **問題**: [What is wrong]
- **法律依據**: [Taiwan statute / principle / or "實務偏好 / 風險管理"; if statute-based, verify via `law.moj.gov.tw` first]
- **風險說明**: [Why this matters]
- **建議修正**: [Rewrite or structural change]
- **待確認事項**: [Questions for the user, if any]

### 優良之處
- [What works well]

### 法條來源（官方）
- [法規名稱 + 相關條號]: [law.moj.gov.tw URL]

> 提醒：本審查報告由 AI 產生，正式使用前請諮詢台灣執業律師。
```

Severity meanings:

- `P0` — likely invalid, unenforceable, or fundamentally misaligned with Taiwan law
- `P1` — material gap or term creating real litigation / compliance / ownership risk
- `P2` — important improvement for clarity, leverage, or operational safety
- `P3` — minor wording, formatting, or cross-reference issue

Load `references/review-playbook.md` when internal standards, negotiation posture, or fallback language matter.

Every finding that cites a statute must be verified via `scripts/verify_official_legal_source.py` or direct `curl` to `law.moj.gov.tw` before inclusion. Use this citation format for verified statutes:

- `個人資料保護法第 8 條（已依 law.moj.gov.tw 驗證）`
- `營業秘密法第 2 條（已依 law.moj.gov.tw 驗證）`
- `民法第 252 條（已依 law.moj.gov.tw 驗證）`

If verification fails, mark the citation as `（未驗證）` and explain the failure. Always include the matching official source URLs in the final `法條來源（官方）` section.

#### `Redline`

Use this when the user wants replacement language tied to specific visible clauses.

Output:

```md
## Redline Report: [Document Name]

### Working Assumptions
- Review basis: [visible final text / OCR text / partial excerpt / screenshot]
- Redline confidence: High / Medium / Low
- Playbook basis: [internal playbook / default Taiwan commercial posture]

### Redlines

#### [P0/P1/P2/P3] — [Short title]
- **條款位置**: [Article / section / nearby snippet]
- **目前文字**: [Quote or summarize the visible wording]
- **問題**: [What needs to change]
- **建議替換文字**:
  [Full replacement clause or sentence]
- **修正理由**: [Taiwan law / enforceability / business posture]
- **談判姿態**: [Must fix / Preferred fallback / Acceptable if deal pressure is high]
- **待確認事項**: [Questions or dependencies]

### Integration Notes
- [Definitions, cross-references, schedules, or signature blocks that also need updates]

### 法條來源（官方）
- [法規名稱 + 相關條號]: [law.moj.gov.tw URL]

> 提醒：若原始檔並非可直接編修之文字版本，本輸出屬 redline-ready wording，而非原檔 track changes。
```

Use `references/review-playbook.md` when fallback positions matter and `references/clause-risk-patterns.md` when replacement wording needs Taiwan-specific clause engineering.

Every `修正理由` that cites a statute or article number must be verified via `law.moj.gov.tw` before inclusion. Run the verification script for each cited article. If verification fails, mark the citation as `（未驗證）` — do not silently downgrade to `可執行性風險` or `實務偏好` as a way to skip verification.

#### `Draft`

Draft in Traditional Chinese unless the user asks otherwise. Use legal Chinese for operative clauses and keep technical product terms in English when that is market standard.

Structure:

1. Title
2. Parties
3. Recitals
4. Numbered operative clauses
5. General provisions
6. Signature blocks

After the draft, always append:

```md
### 法條來源（官方）
- [法規名稱 + 相關條號]: [law.moj.gov.tw URL]
```

Use `references/clause-risk-patterns.md` and `references/tw-legal-framework.md` while drafting.

Drafting a contract from scratch still requires verifying every statute cited in the operative clauses, notes, or compliance statements. Run `scripts/verify_official_legal_source.py` for each article referenced in the draft. A draft with unverified law citations is incomplete — verify first, then finalize.

#### `Clause Insert`

Provide:

1. The clause text
2. Recommended placement
3. Definitions or cross-references that must also change
4. Any collision with existing liability, confidentiality, IP, or data-handling language
5. `法條來源（官方）` — verify every statute cited in the clause text or explanation via `law.moj.gov.tw` and list the verified URLs. This is mandatory, not conditional.

## Reference Map

- `references/document-intake.md`
  Use for PDF / DOCX / pasted text / partial document intake, OCR caveats, and citation method.
- `references/review-triage.md`
  Use for first-pass routing, Green / Yellow / Red logic, and escalation triggers.
- `references/review-playbook.md`
  Use when a negotiation playbook, fallback positions, role-based review, or business posture matters.
- `references/official-legal-sources.md`
  Use whenever the output depends on statute names, article numbers, current law status, official legal verification, or final source-URL listing.
- `references/legal-local-playbook-template.md`
  Use when the user wants organization-specific review positions or when `.claude/legal.local.md` is missing and you need the expected playbook shape.
- `references/clause-risk-patterns.md`
  Use for clause design, common red flags, and Taiwan-specific drafting patterns.
- `references/tw-legal-framework.md`
  Use for commercial law issue-spotting and Taiwan legal grounding before official-source verification.
- `references/tw-labor-framework.md`
  Use for employment/labor contract issue-spotting: LSA termination, severance, non-compete, working hours, overtime, leave, wage structure, and pension obligations.

## Constraints

- Do not present a practice preference as if it were a statutory mandate.
- Do not cite statute names or article numbers from memory when official-source verification is required.
- Do not import U.S. or EU default assumptions into a Taiwan document without saying so explicitly.
- Do not claim to have reviewed annexes, schedules, tracked changes, or referenced exhibits unless they were actually provided.
- Do not fabricate citations, cases, or clauses.
- Do not treat local reference files as the final authority when `law.moj.gov.tw` can verify the point.
- Do not claim to have produced a native redline against a `.docx` or PDF when you only saw extracted text; label it as `redline-ready wording` instead.
- If the user requests "latest" legal or regulatory status, verify current law before answering.
