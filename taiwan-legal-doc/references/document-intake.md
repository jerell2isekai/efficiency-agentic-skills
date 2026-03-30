# Document Intake for Taiwan Legal Review

Use this reference when the user provides a PDF, DOCX, pasted text, scan, screenshot, or only part of a legal document.

## Table of Contents

1. [Purpose](#1-purpose)
2. [Supported inputs](#2-supported-inputs)
3. [Intake sequence](#3-intake-sequence)
4. [Confidence and downgrade rules](#4-confidence-and-downgrade-rules)
5. [Citation rules](#5-citation-rules)
6. [Special file conditions](#6-special-file-conditions)

## 1. Purpose

Do not jump straight into legal conclusions. First identify what text is actually available, how trustworthy the extraction is, and what portion of the document can be reviewed with confidence.

This reference absorbs the useful part of generic legal-document-analyzer workflows but keeps the output narrow and Taiwan-focused.

## 2. Supported Inputs

Handle these input types:

- Pasted contract text
- Markdown or plain text files
- PDF contracts
- DOCX contracts
- Scanned or image-derived text
- Partial excerpts, screenshots, or a single clause

Treat these as high-risk inputs that require explicit caveats:

- Image-only PDF with weak OCR
- Partial screenshots without surrounding clauses
- Documents that reference missing appendices, schedules, exhibits, data processing appendices, or rate cards
- Redlines / tracked changes when the revision state is not visible

## 3. Intake Sequence

Follow this order:

1. Identify file type and readability
2. Identify whether the document is complete or partial
3. Extract visible structure
4. Identify document type
5. Identify parties and roles
6. Extract key clauses for the requested task
7. State review confidence before concluding

### Structural Extraction Checklist

Extract, if visible:

- Title
- Effective date
- Parties and role labels
- Section headings / article numbers
- Definitions
- Economic terms
- Confidentiality / data / IP / liability / termination / governing law clauses
- Signature block
- Exhibits or appendices references

If the user only wants one clause reviewed, still scan surrounding definitions, liability, governing law, and conflict clauses if visible.

## 4. Confidence and Downgrade Rules

Use explicit confidence language.

### High confidence

Use when:

- Text is machine-readable
- Relevant sections are present
- Clause numbers and headings are visible
- No key appendices appear missing for the requested question

### Medium confidence

Use when:

- The document is mostly readable but some pages, tables, or tracked changes context are missing
- You can evaluate visible clauses but not the full contract interaction

### Low confidence

Use when:

- OCR is poor
- Only screenshots or fragments are available
- Cross-referenced clauses or appendices are missing
- The user asks for a full review from only part of the document

When confidence is medium or low, say:

- what you reviewed
- what you could not verify
- whether the result is suitable only for triage rather than full review

## 5. Citation Rules

For every review finding, cite one of:

- article / section number
- heading name
- nearby quoted text snippet
- page + visible heading if page numbers are available

Good examples:

- `第 7 條「保密資訊」`
- `Section 4.2 Limitation of Liability`
- `簽署頁上要求填寫身分證字號之欄位`
- `「乙方不得於任何情形主張著作人格權」`

Bad examples:

- `合約看起來有問題`
- `後面那一條`
- `某處似乎限制太重`

## 6. Special File Conditions

### Partial excerpts

Do not pretend to have reviewed the full contract. Limit the conclusion to:

- clause wording quality
- obvious legal conflict
- likely missing companion clauses

### Tracked changes / redlines

If the changed-vs-current state is unclear:

- say whether you are reviewing visible final text or markup only
- avoid concluding that a term was deleted or accepted unless that is clearly shown

### OCR-poor scans

If names, numbers, or defined terms are unreliable:

- avoid drafting precise replacement language keyed to those terms
- offer triage or a checklist instead of clause-level markup

### Missing appendices

If the contract references missing documents, treat any dependent conclusion as provisional. Common examples:

- DPA / personal data appendix
- statement of work
- fee schedule
- deliverable list
- security appendix

### DOCX / PDF intake posture

When the request is to review a `.docx` or `.pdf`, do not assume the format itself provides extra authority. The governing factor is the visible text, not the file extension.
