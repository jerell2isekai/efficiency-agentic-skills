# Taiwan Legal Framework Reference

Detailed Taiwan legal working summary for document drafting and review. Use this file for issue-spotting and structured thinking, not as the final citation authority when an official source can verify the point.

## How to Read This File

- Treat this file as a **secondary reference**.
- For statute names, article numbers, current law status, and mandatory legal requirements, verify against `law.moj.gov.tw` before presenting the point as definite.
- If this file conflicts with the official source, the official source wins.

- Sections **1-4** are primarily statute-grounded legal rules.
- Sections **5-7** mix legal framing with drafting heuristics and review checklists.
- When writing findings, distinguish:
  - **法律要求 / statutory baseline**
  - **可執行性風險 / enforceability risk**
  - **實務偏好 / drafting or market preference**

If the user asks for the **latest** legal or regulatory status, verify current law before treating any time-sensitive note here as current.

## Table of Contents

1. [Personal Data Protection Act (個資法)](#1-personal-data-protection-act)
2. [Trade Secrets Act (營業秘密法)](#2-trade-secrets-act)
3. [Copyright Act (著作權法)](#3-copyright-act)
4. [Civil Code — Penalties (民法違約金)](#4-civil-code-penalties)
5. [Consultant-Specific Considerations](#5-consultant-specific-considerations)
6. [Combined Document Patterns](#6-combined-document-patterns)
7. [Common Pitfalls Checklist](#7-common-pitfalls-checklist)

---

## 1. Personal Data Protection Act

### §4 — Commissioned Processing

受委託蒐集、處理或利用個資者，於本法適用範圍內，**視同委託機關**。

Implications:
- The commissioning company **remains liable** for the processor's violations
- The processor must comply with all PDPA obligations as if they were the original controller
- Supervision is mandatory under the Enforcement Rules §8

### §8 — Notification Obligations (6 mandatory items)

When collecting personal data, the collector must inform data subjects of:
1. Entity name (機關名稱)
2. Collection purpose (蒐集目的)
3. Data categories (資料類別)
4. Use period, territory, recipients, methods (利用之期間、地區、對象、方式)
5. Data subject rights under §3 and exercise methods (當事人權利及行使方式)
6. Impact of not providing data (不提供之影響)

**Critical**: Every piece of data actually collected (including in signature blocks — phone, address, signature, ID number) must be covered by the notice. A common compliance failure is collecting data in the signing section without listing it in the notice categories.

### §27 / §20-1 — Security Maintenance

Non-government agencies must implement appropriate security measures. The 2025 amendment consolidated §27 into new §20-1 under the Personal Data Protection Commission (PDPC).

### §29 — Civil Liability

Non-government agencies are liable for unlawful collection/processing/use unless they prove absence of intent or negligence. The commissioning company cannot fully shift liability to the processor via contract.

### §41 — Criminal Penalties

Intent to unlawfully benefit self/third party + violation + damage to others → up to **5 years imprisonment** + NT$1,000,000 fine. These are public offenses (non-complaint crimes).

### Enforcement Rules §8 — Supervision Requirements

When commissioning data processing, the commissioning agency must:
1. Specify scope, categories, purpose, duration
2. Confirm processor's security measures
3. Require approval for sub-commissioning
4. Require immediate incident notification
5. Require return/deletion upon termination
6. Conduct regular inspections with documented results

### Consent Form Design

- Sensitive data (medical, health) requires **written consent**
- Regular personal data consent need not be written, but written is strongly recommended for evidence
- Secondary use requires **explicit written consent** (implied insufficient)
- ID numbers (身分證字號) are high-sensitivity — require clear justification if collected

---

## 2. Trade Secrets Act

### §2 — Definition (Three Requirements)

Information qualifies as a trade secret only if ALL three are met:
1. **Non-public** (秘密性) — not generally known to persons in the relevant field
2. **Economic value** (經濟價值) — actual or potential value due to its secrecy
3. **Reasonable protective measures** (合理保密措施) — the owner has taken steps to protect it (NDAs, access controls, marking, etc.)

Not all "confidential information" in an NDA qualifies as a trade secret. Criminal liability references should be conditional: "如符合本法第2條要件者…"

### §12-13 — Civil Remedies

- Damages: actual loss method OR infringer's profit method
- **Treble damages** for intentional misappropriation (up to 3x proven damages)
- Statute of limitations: 2 years from discovery, 10 years from act

### §13-1 — Criminal Penalties (Domestic)

Intentional acquisition/use/disclosure of trade secrets:
- Up to **5 years imprisonment**
- NT$1-10 million fine
- Or up to 3x illicit gain
- Complaint-based: 6-month filing window after identifying offender

### §13-2 — Aggravated (Cross-Border)

Intent to use trade secrets abroad (including China, HK, Macau):
- **1-10 years imprisonment**
- NT$3-50 million fine
- Or up to 10x illicit gain
- **No statute of limitations**

### §13-3/13-4 — Corporate Liability

When an employee/agent commits §13-1 or §13-2 in the course of business, both the individual and the employer face penalties — unless the employer proves "utmost care" prevention measures.

---

## 3. Copyright Act

### §12 — Commissioned Works (出資聘人完成之著作)

Default rules when no contract exists:
- **Copyright (著作財產權)**: belongs to the **creator** (not the commissioner)
- **Commissioner**: gets a license to use within the originally agreed scope

Contract can override: assign copyright to commissioner. Always specify explicitly.

### Moral Rights (著作人格權)

- **Cannot be transferred** by law (§21)
- Include: right of attribution (姓名表示權), right of integrity (同一性保持權), right of disclosure (公開發表權)
- Best practice: licensee agrees "not to assert moral rights in a manner that obstructs the permitted use" (不對甲方主張妨礙該利用之權利)

### Non-Copyrightable Work Product

Review opinions, annotations, checklists, correction marks, and factual compilations may not meet the originality threshold for copyright protection. Handle separately:
- "Ownership and usage rights of non-copyrightable work product belong to the commissioning party"

---

## 4. Civil Code — Penalties

### §250 — Liquidated Damages Types

Two types:
1. **Compensatory** (損害賠償預定性) — replaces actual damages proof; cannot claim additional damages
2. **Punitive** (懲罰性) — penalty on top of actual damages; can still claim actual damages separately

If the contract doesn't specify type, courts presume **compensatory**. For NDAs, specify punitive explicitly if you want the penalty + actual damages.

### §252 — Judicial Reduction

Courts have discretion to reduce "excessively high" liquidated damages to an "appropriate amount." Factors considered:
- Proportionality to actual/foreseeable harm
- Economic position of the parties
- Degree of fault
- Whether obligation was partially performed

### Practical Multipliers for Taiwan

| Multiplier | Court treatment | Notes |
|-----------|----------------|-------|
| 10-30% of contract value | Safe zone for general commercial | Almost never reduced |
| **3x contract value** | Commonly accepted for IP/NDA | Entertainment, tech licensing precedent |
| 5x+ | High reduction risk | Need strong justification |
| Fixed amount | Depends on reasonableness | Good for variable-fee contracts |

### Design Tips

- Always specify calculation basis clearly (total contract amount including tax)
- Include fallback amount for contracts without fixed fees
- Preserve separate actual damages claim: "前項違約金不影響甲方另行請求超過違約金部分之實際損害賠償"
- Add template notes for blank fields: "（本欄位於無固定報酬情境下為必填）"

---

## 5. Consultant-Specific Considerations

### Non-Compete vs Conflict of Interest

| Aspect | Non-Compete (競業禁止) | Conflict of Interest (利益衝突) |
|--------|----------------------|-------------------------------|
| Legal basis | 民法 (for consultants) | Contractual |
| Compensation required? | No (勞基法 §9-1 50% rule applies only to employees) | No |
| Enforceability | Must meet reasonableness: duration, geography, scope | Generally enforceable |
| Recommended for consultants | Usually too aggressive | Preferred — lighter, less friction |

For consultants, prefer conflict of interest declarations over full non-compete. Define "direct competitor" with specificity: industry, market, geographic scope.

### Data Handling When Consultant Downloads Files

When a consultant downloads data to personal devices:
- Require minimum security standards: screen lock, updated OS/antivirus, no shared accounts
- Prohibit upload to unauthorized cloud/platforms
- Prohibit AI tool input (ChatGPT, Copilot, etc.) — increasingly standard since 2024
- Require 24-hour security incident notification
- Destruction obligation: "reasonably accessible and controllable" copies; address auto-backups (Time Machine, system snapshots) separately
- Require transmission via designated or mutually agreed channels only

---

## 6. Combined Document Patterns

When combining multiple legal instruments (e.g., consent form + NDA) in one document:

### Structure
- Main title covering the whole document
- Part A / Part B (甲部 / 乙部) with separate section titles
- Each part has its own signature block
- General provisions (governing law, jurisdiction) in the final part or shared section

### Independence vs Cross-Reference

State independence (可分性) with explicit dependencies:

```
各部內容相互獨立，任一部分之無效不影響其餘部分之效力。
但乙部涉及乙方個人資料揭露之條款，應以甲部乙方之同意範圍為限。
```

### Common Contradiction Traps

1. **Perpetual license vs revocable consent**: If Part A allows consent withdrawal while Part B grants "perpetual" rights, clarify that "perpetual" means "does not auto-expire on project end" not "irrevocable." Add: "惟乙方依甲部第X條撤回者，甲方仍應依甲部第X條第Y款辦理。"

2. **Authorized channels vs blanket cloud ban**: If one clause allows "甲方指定之管道" while another bans "公用雲端," qualify the ban: "未經甲方指定或雙方書面同意之公用雲端空間"

3. **Legal disclosure vs confidentiality**: Compelled disclosure exception must include: "於法律許可範圍內，於揭露前儘速通知；如依法不得事前通知，應於限制解除後儘速通知"

---

## 7. Common Pitfalls Checklist

Use this checklist when reviewing any Taiwan legal document:

- [ ] Every collected personal data item appears in the PDPA notice
- [ ] Signature block data (phone, address, ID) is covered by collection purposes
- [ ] ID number collection has clear legal basis stated, or is marked optional with accurate impact description
- [ ] Withdrawal/deletion mechanism has specific timeline (not "合理期間")
- [ ] Force majeure exclusion for third-party caches/search engine snapshots
- [ ] Confidentiality period survives termination (explicit statement)
- [ ] Liquidated damages have clear, calculable basis with fallback amount
- [ ] Criminal liability reference is conditional on meeting 營業秘密法 §2 requirements
- [ ] IP assignment covers both copyrightable and non-copyrightable work product
- [ ] Moral rights clause uses "不主張妨礙" pattern (cannot transfer, can agree not to assert)
- [ ] Cross-references between document parts actually resolve correctly
- [ ] Jurisdiction clause specifies a district court (e.g., 臺灣新北地方法院)
- [ ] R.O.C. calendar date format used
- [ ] AI tool prohibition clause included for post-2024 agreements
- [ ] Security incident notification timeline specified (recommend 24 hours)
- [ ] Destruction obligation scoped to "可合理存取與控制" copies
