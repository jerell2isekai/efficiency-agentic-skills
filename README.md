# efficiency-agentic-skills

[繁體中文版 README（taiwan-legal-doc）](taiwan-legal-doc/README.zh-TW.md)

Curated agentic skills for Codex and Claude Code.

This repository collects production-minded skills, references, and deterministic helpers for real workflows. The first public release focuses on Taiwan commercial legal drafting and review. Additional skills from this workspace are planned and listed below as `coming soon`.

## Available Now

### `taiwan-legal-doc`

Draft, triage, review, redline, and revise Taiwan commercial legal documents, including:

- NDA / 保密協議
- personal data consent forms / 個資同意書
- consultant and service agreements / 顧問合約、服務合約
- IP assignment and ownership clauses / 著作權讓與、智財歸屬
- portrait and likeness authorization / 肖像授權

Highlights:

- Taiwan-focused workflow for `Quick Triage`, `Full Review`, `Redline`, `Draft`, and `Clause Insert`
- official-source governance using `law.moj.gov.tw`
- deterministic verifier for official legal sources via `curl` with `agent-browser` fallback
- structured output contract with mandatory `法條來源（官方）`

## Install

Use `skills.sh` if you want the standard install path for agent skills.

```bash
npx skills add -g https://github.com/jerell2isekai/efficiency-agentic-skills --skill taiwan-legal-doc
```

You can also inspect the package before installing:

```bash
npx skills add https://github.com/jerell2isekai/efficiency-agentic-skills --list
```

### Manual install

If you prefer to clone the repository and copy the skill yourself:

#### Codex

```bash
git clone https://github.com/jerell2isekai/efficiency-agentic-skills.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R efficiency-agentic-skills/taiwan-legal-doc "${CODEX_HOME:-$HOME/.codex}/skills/"
```

#### Claude Code

```bash
git clone https://github.com/jerell2isekai/efficiency-agentic-skills.git
mkdir -p .claude/skills
cp -R efficiency-agentic-skills/taiwan-legal-doc .claude/skills/
```

## Quick Start

```text
# Codex / skill reference style
Use $taiwan-legal-doc to review this Taiwan NDA and identify material risks.
Use $taiwan-legal-doc to redline this consultant agreement for Taiwan use.
Use $taiwan-legal-doc to draft a Taiwan personal data consent form for expert interviews.

# Other coding CLIs with slash-skill triggers
/taiwan-legal-doc Review this Taiwan NDA and identify material risks.
/taiwan-legal-doc Redline this consultant agreement for Taiwan use.
/taiwan-legal-doc Draft a Taiwan personal data consent form for expert interviews.

# Generic slash pattern for this repository
/taiwan-legal-doc ...
/arch-review ...        # coming soon
/conductor ...          # coming soon
/research ...           # coming soon
```

## Skill Catalog

| Skill | Status | Notes |
| --- | --- | --- |
| `taiwan-legal-doc` | available | Taiwan legal drafting and review |
| `arch-review` | coming soon | architecture review workflow |
| `conductor` | coming soon | end-to-end task orchestration |
| `crossover` | coming soon | cross-agent review workflow |
| `design-conductor` | coming soon | design orchestration |
| `git` | coming soon | git and GitHub operations |
| `handover` | coming soon | cross-session continuity |
| `orient` | coming soon | repository orientation |
| `planner` | coming soon | planning workflow |
| `prelude` | coming soon | shared governance bootstrap |
| `research` | coming soon | deep technical investigation |
| `rolling` | coming soon | execution engine |
| `self-review-loop` | coming soon | iterative self-review |
| `writer` | coming soon | markdown and documentation writing |

## Repository Layout

```text
.
├── README.md
└── taiwan-legal-doc/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    └── scripts/
```

## Notes

- Only `taiwan-legal-doc` is included in the initial public push.
- Other local skills in this workspace are intentionally withheld for now and listed as roadmap entries only.
- AI-generated legal output should still be reviewed by a licensed Taiwan attorney before signature or live use.
- This repository is released under the MIT License. See `LICENSE`.
