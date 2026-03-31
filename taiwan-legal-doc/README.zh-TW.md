# 台灣商務及勞動法律文件助手

[English](../README.md)

用 Claude Code 或 Codex 起草、審查台灣商務及僱傭法律文件的技能（skill）。丟合約進來就能跑初篩、逐條審查、紅線修改或從零起草。產出僅供參考，正式使用前請找台灣執業律師看過。

## 支援的文件類型

**商務合約**
- 保密協議（NDA）
- 個人資料蒐集同意書
- 顧問合約、服務合約
- 著作權讓與、智慧財產權歸屬條款
- 肖像授權書
- 混合型合約（同時包含多種條款）

**勞動 / 僱用合約**
- 勞動契約（不定期 / 定期）
- 競業禁止條款
- 工時、加班、休假相關條款
- 資遣與離職相關條款

## 功能特色

| 工作模式 | 說明 |
|----------|------|
| Quick Triage | 快速初篩，將文件分成綠、黃、紅三級風險，附帶處理建議 |
| Full Review | 逐條審查，標示 P0–P3 嚴重度，給出修正語句和談判建議 |
| Redline | 針對原文逐條提供替換文字，附修正理由與談判姿態 |
| Draft | 從零起草台灣適用的合約，以繁體中文為預設語言 |
| Clause Insert | 對既有合約新增或替換特定條款，檢查與現有條文的衝突 |

法條引用不靠記憶：

- 法條出處一律對照法務部「全國法規資料庫」（law.moj.gov.tw）
- 內建驗證腳本，透過 `curl` 或 `agent-browser` 自動比對官方條文
- 每份輸出都附 `法條來源（官方）` 區塊，列出引用法規的官方連結
- 區分「法律要求」和「起草偏好」，不把慣例當成法律義務

法規基線涵蓋：

- 個人資料保護法（個資法）及施行細則
- 營業秘密法
- 著作權法
- 民法（違約金、定型化契約）
- 勞動基準法（工時、加班、資遣、競業禁止）
- 勞工退休金條例（勞退新制 6% 提撥）
- 性別平等工作法（產假、陪產假、育嬰留停）
- 就業服務法（就業歧視、外籍勞工）
- 職業安全衛生法（健檢、職災通報）

## 安裝方式

### 透過 skills.sh 安裝

```bash
npx skills add -g https://github.com/jerell2isekai/efficiency-agentic-skills --skill taiwan-legal-doc
```

查看套件內容：

```bash
npx skills add https://github.com/jerell2isekai/efficiency-agentic-skills --list
```

### 手動安裝

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

## 使用範例

```text
# Codex 風格
Use $taiwan-legal-doc to review this Taiwan NDA and identify material risks.

# Claude Code slash 指令
/taiwan-legal-doc 審查這份台灣 NDA，找出重大風險。
/taiwan-legal-doc 幫這份顧問合約做 redline，確保符合台灣法規。
/taiwan-legal-doc 起草一份個資蒐集同意書，用途是專家訪談。
/taiwan-legal-doc 審查這份勞動契約，看資遣費和競業禁止條款有沒有問題。
/taiwan-legal-doc 起草一份不定期勞動契約，含試用期和加班約定。
```

## 運作流程

1. **界定範圍** — 確認文件類型、雙方角色、標的、管轄法院、工作模式
2. **資訊確認** — 檢查是否有足夠資訊開始作業；不足時使用 `[待填]` 標記
3. **文件讀取** — 根據文件格式（PDF、DOCX、純文字、截圖）正確擷取內容
4. **法規比對** — 載入台灣法律框架，辨識相關法規後向 law.moj.gov.tw 驗證
5. **產出結果** — 依選定模式輸出審查報告、修改建議、草稿或條款
6. **附上法源** — 每次輸出都附帶 `法條來源（官方）` 區塊

## 參考資料目錄

| 檔案 | 用途 |
|------|------|
| `references/document-intake.md` | 文件讀取與格式處理規則 |
| `references/review-triage.md` | 快速分流的路由邏輯 |
| `references/review-playbook.md` | 談判姿態與內部審查標準 |
| `references/official-legal-sources.md` | 官方法規驗證流程 |
| `references/legal-local-playbook-template.md` | 組織內部審查偏好的範本格式 |
| `references/clause-risk-patterns.md` | 條款設計與常見紅旗模式 |
| `references/tw-legal-framework.md` | 台灣商業法律爭點辨識基礎 |
| `references/tw-labor-framework.md` | 台灣勞動法規基礎（勞基法、勞退、性平法、就服法、職安法） |

## 注意事項

- 產出不構成法律意見，簽署前請找律師看過
- 法條引用以法務部全國法規資料庫為準，技能內部參考資料只是輔助
- MIT 授權
