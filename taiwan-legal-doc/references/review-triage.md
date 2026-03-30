# Review Triage for Taiwan Commercial Documents

Use this reference for fast first-pass routing when the user wants to know whether a document looks safe enough to sign, should be negotiated, or should be escalated to deeper review.

## Table of Contents

1. [Purpose](#1-purpose)
2. [When to use triage](#2-when-to-use-triage)
3. [Risk routing](#3-risk-routing)
4. [Escalation triggers](#4-escalation-triggers)
5. [NDA-specific quick checks](#5-nda-specific-quick-checks)
6. [Output style](#6-output-style)

## 1. Purpose

Triage is not a clause-by-clause legal opinion. It is a routing mechanism.

The goal is to answer:

- Is the document broadly acceptable?
- Is there a specific cluster of issues that makes it risky?
- Does this need a full review before signature?

## 2. When to Use Triage

Use `Quick Triage` when:

- the user says "先幫我快速看一下"
- the user wants a sign / negotiate / escalate recommendation
- the document is long and the user wants a first-pass read
- the input is partial or OCR-limited and a full review would overclaim certainty

Do not stay in triage if the user asks for:

- rewrite language
- redline-ready findings
- full clause inventory
- negotiation fallback wording
- detailed compliance analysis

## 3. Risk Routing

### Green

Use `Green` when:

- no obvious Taiwan-law conflict is visible
- the document appears commercially balanced for the user's role
- no major gap is visible in confidentiality, data, IP, liability, or governing law
- any issues are minor wording or process issues

Typical recommendation:

- suitable to proceed
- optionally clean up a few low-risk items

### Yellow

Use `Yellow` when:

- the document is generally workable but has terms that deserve negotiation
- risk is concentrated in one or two areas rather than making the whole document unacceptable
- the user could decide based on leverage, deal value, or risk tolerance

Typical Yellow patterns:

- overbroad confidentiality definition
- missing carve-outs
- unclear IP ownership
- one-sided indemnity
- vague data handling duties
- penalty / liquidated damages without clear basis
- automatic renewal or termination asymmetry

Typical recommendation:

- negotiate listed terms
- upgrade to `Full Review` if the deal is material

### Red

Use `Red` when:

- the document likely conflicts with Taiwan enforceability or core legal structure
- ownership, confidentiality, or personal data obligations are dangerously unclear
- the commercial burden is plainly one-sided
- required Taiwan-law mechanics are absent in a way that creates real legal exposure
- the user is being asked to sign while the document remains incomplete or contradictory

Typical Red patterns:

- clause likely invalid or highly vulnerable to challenge
- copyright transfer language that ignores moral rights limits
- collection of personal data without required notice structure
- blanket criminal-liability language treating all confidential information as trade secrets
- uncapped, undefined, or internally contradictory penalty provisions
- critical exhibits missing

Typical recommendation:

- do not sign as-is
- escalate to `Full Review`
- consult counsel if commercially important

## 4. Escalation Triggers

Upgrade from triage to `Full Review` when any of these appear:

- cross-referenced clauses materially affect the visible issue
- multiple Yellow issues interact
- Red issue appears
- the document controls personal data, core IP, trade secrets, exclusivity, or long-term service delivery
- the user asks for revision language
- the user's internal fallback positions matter

## 5. NDA-Specific Quick Checks

For NDA triage, check these first:

1. Which side is the discloser and which is the recipient?
2. Is confidential information defined too broadly or too vaguely?
3. Are standard carve-outs present?
4. Does confidentiality survive termination?
5. Are use restrictions, return/destruction duties, and breach notification addressed?
6. Does the penalty structure look commercially plausible under Taiwan practice?
7. Does any criminal-liability wording improperly imply all confidential information is automatically a trade secret?

If the user is the **recipient**, pay extra attention to:

- residual knowledge language
- reverse engineering restrictions
- employee / affiliate access restrictions
- indefinite confidentiality periods

If the user is the **discloser**, pay extra attention to:

- evidence of reasonable protective measures
- breach reporting timing
- downstream sharing restrictions
- destruction and backup handling

## 6. Output Style

Keep triage short. The output should route, not overwhelm.

Recommended fields:

- `風險等級`
- `一句結論`
- `關鍵風險`
- `是否建議升級 Full Review`
- `立即處理建議`

If the input is incomplete, add:

- `檢視限制`
