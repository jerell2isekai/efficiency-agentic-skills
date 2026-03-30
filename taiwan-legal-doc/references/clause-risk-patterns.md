# Clause Risk Patterns for Taiwan Commercial Documents

Use this reference for drafting and clause insertion. It captures common Taiwan-focused red flags and preferred clause patterns without replacing the statutory baseline in `tw-legal-framework.md`.

## Table of Contents

1. [How to use this file](#1-how-to-use-this-file)
2. [NDA / confidentiality](#2-nda--confidentiality)
3. [PDPA consent and data notices](#3-pdpa-consent-and-data-notices)
4. [Consultant / service agreements](#4-consultant--service-agreements)
5. [IP assignment](#5-ip-assignment)
6. [Portrait / likeness authorization](#6-portrait--likeness-authorization)
7. [Combined documents](#7-combined-documents)

## 1. How to Use This File

Treat these as clause-engineering patterns:

- some points are statute-driven
- some are enforceability-driven
- some are current commercial practice

If a point is only a market preference, present it as `通常`, `建議`, or `常見`, not as an absolute legal requirement.

## 2. NDA / Confidentiality

### Core clauses

Include or verify:

- definition of confidential information
- permitted purpose / use limitation
- disclosure restrictions
- internal access control
- standard carve-outs
- return / destruction
- breach / incident notification
- duration and survival
- governing law and forum

### Common red flags

- definition so broad that it captures all discussions forever without useful boundary
- no public-domain / prior-possession / independent-development carve-outs
- no survival language
- no treatment of backups or system snapshots
- criminal-liability language implying all confidential information automatically meets trade-secret requirements

### Drafting notes

- If the user needs stronger protection, tie the clause structure to reasonable protective measures rather than only demanding secrecy.
- AI tool prohibition is a current risk-management preference in many post-2024 agreements; present it as a practice choice, not a statutory requirement.
- Fixed penalties should have a clear calculation basis or fallback amount.

## 3. PDPA Consent and Data Notices

### Core clauses

Include or verify:

- collecting entity
- purpose of collection
- data categories
- use period / territory / recipients / methods
- data subject rights and exercise method
- effect of refusing to provide data

### Common red flags

- collecting phone, address, signature, or ID number in the signature block without covering them in the notice
- saying the data will be used for "all business needs" without specific purpose framing
- collecting ID number without clear necessity
- no contact channel for rights exercise

### Drafting notes

- If the user wants a consent form, keep notice language specific and readable.
- If a third party processes data, align contract duties with commissioned-processing supervision rather than using vague processor language.

## 4. Consultant / Service Agreements

### Core clauses

Include or verify:

- scope of services / deliverables
- fees and payment timing
- confidentiality
- data handling
- IP ownership or license
- subcontracting
- conflict of interest or non-compete posture
- termination and post-termination duties

### Common red flags

- deliverables undefined but ownership assigned broadly
- consultant expected to handle personal data without security or supervision mechanics
- broad non-compete language with no reasonableness boundary
- destruction obligation that ignores backups and device realities

### Drafting notes

- For consultants, conflict-of-interest language is often more workable than a sweeping non-compete.
- If the consultant uses personal devices, add minimum security requirements and incident reporting.

## 5. IP Assignment

### Core clauses

Include or verify:

- assignment of copyrightable work product
- treatment of moral rights
- treatment of non-copyrightable work product
- pre-existing materials carve-out, if relevant
- scope of permitted reuse, if any

### Common red flags

- "all rights transfer automatically" wording without handling moral-rights limits
- silence on pre-existing tools, templates, or know-how
- ownership clause that does not distinguish commissioned work from background IP

### Drafting notes

- Use language that assigns transferable rights and separately addresses non-assertion of moral rights.
- If the user is the consultant, propose a carve-out for pre-existing materials and generalized know-how where appropriate.

## 6. Portrait / Likeness Authorization

### Core clauses

Include or verify:

- who may use the likeness
- permitted media / channels
- purpose of use
- territory and duration
- edit / adaptation scope
- revocation and post-revocation handling

### Common red flags

- perpetual unrestricted usage language without clear scope
- no distinction between internal use, marketing use, and sublicensed use
- conflict between revocation rights and already-published materials

### Drafting notes

- If likeness use also collects personal data, check consistency with the data notice.

## 7. Combined Documents

When combining NDA + consent + consultant/IP terms in one instrument:

- preserve section-level clarity
- ensure cross-references resolve
- specify dependencies between parts
- keep signature logic clear

Common contradiction traps:

- revocable consent vs perpetual usage language
- allowed channels vs blanket cloud ban
- compelled disclosure exception vs strict confidentiality wording
