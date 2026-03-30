# Local Legal Playbook Template for Taiwan Reviews

Use this reference when the user wants the review aligned to internal policy, fallback positions, or approval routing.

## Table of Contents

1. [Purpose](#1-purpose)
2. [Discovery rule](#2-discovery-rule)
3. [Minimum schema](#3-minimum-schema)
4. [Default behavior when missing](#4-default-behavior-when-missing)
5. [Suggested template](#5-suggested-template)

## 1. Purpose

Do not treat "playbook-aware review" as a vague idea. Use a repeatable discovery rule and a minimum structure.

This file defines the expected shape for a local legal playbook such as `.claude/legal.local.md`.

## 2. Discovery Rule

Look in this order:

1. The current repo's `.claude/legal.local.md`
2. A user-provided path or attached playbook
3. A shared workspace playbook explicitly pointed to by the user

If multiple playbooks exist, prefer the closest repo-specific file unless the user says otherwise.

## 3. Minimum Schema

The playbook should define, at minimum:

- the side the organization usually protects
- standard vs acceptable fallback positions
- escalation triggers
- clause-specific preferences for NDAs, data handling, IP, liability, and governing law
- any forbidden terms that require immediate escalation

Recommended sections:

- `## Review Posture`
- `## NDA Defaults`
- `## Data / PDPA`
- `## IP Ownership`
- `## Liability / Liquidated Damages`
- `## Term / Termination`
- `## Governing Law / Venue`
- `## Escalation Triggers`
- `## Style / Drafting Preferences`

## 4. Default Behavior When Missing

If no playbook is available:

- say that no internal playbook was found
- use Taiwan-law baseline first
- use role-based commercial reasonableness from `review-playbook.md`
- distinguish clearly between `法律要求` and `內部偏好未提供`

Do not invent approval matrices, fallback ranges, or red lines.

## 5. Suggested Template

```md
# Legal Playbook Configuration

## Review Posture
- Protected side: discloser / recipient / buyer / vendor / neutral
- Default review style: conservative / balanced / business-forward

## NDA Defaults
- Mutual obligations required: yes / no / depends
- Standard term: ...
- Standard survival: ...
- Required carve-outs: ...
- Forbidden terms: non-compete / non-solicit / residuals / exclusivity / other

## Data / PDPA
- Require separate notice or appendix when personal data is involved: yes / no
- Breach notification target: 24h / 48h / other
- Required sub-processor controls: ...

## IP Ownership
- Preferred ownership rule: ...
- Background IP carve-out required: yes / no
- Moral-rights handling preference: ...

## Liability / Liquidated Damages
- Preferred cap or structure: ...
- Acceptable fallback: ...
- Escalate if: ...

## Governing Law / Venue
- Preferred governing law: Taiwan
- Preferred venue: [district court]
- Acceptable alternatives: ...

## Escalation Triggers
- ...

## Style / Drafting Preferences
- Use ROC date format: yes / no
- Prefer bilingual definitions: yes / no
- Preferred clause tone: strict / balanced / plain-language
```
