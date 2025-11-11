# 🧭 PropTech-Vault Overview

## 🔹 Purpose
This vault serves as the **central intelligence system** for the PropTech / InnCurrent initiative — uniting:
- **Funding & Grants tracking**
- **Product development roadmaps (MVP → Full Build)**
- **Research & Learning notes (Python, LangChain, automation)**
- **Execution pipelines (n8n, GitHub Actions, AI agents)**

All data here is version-controlled via GitHub and readable by your **Custom GPT** or other AI connectors for live recall and summarization.

---

## 📁 Vault Structure

```
PropTech-Vault/
│
├── 0_Company_Overview/           → Mission, org chart, partner profiles
├── 1_Research_and_Learning/      → Python / LangChain / AI notes
├── 2_Funding_&_Grants/           → All grant trackers and funding dashboards
│     ├── PropTech_Funding_MERGED_Annotated.csv
│     └── Funding_Tracker.md
├── 3_Product_Development/        → MVP & Full Product plans, architecture notes
├── 4_Execution_&_Automation/     → n8n pipelines, GitHub Actions, automations
└── Templates/                    → Standardized note templates
```

---

## 🧩 Key Files

### `2_Funding_&_Grants/PropTech_Funding_MERGED_Annotated.csv`
- Unified table of **Canada + Hong Kong** funding programs
- Columns: `Region`, `Scheme`, `Administering Body`, `Type of Support`, `Official Link`, `Stage`, `Next Review`
- “Next Review” = yearly reminder for link and program updates

### `2_Funding_&_Grants/Funding_Tracker.md`
Interactive **Dataview dashboard** showing:
- MVP vs Full Product programs
- Country segmentation
- Tasks plugin reminders for the next review cycle

---

## ⚙️ Automation Loop (2-Hour Semi-Automatic Cycle)

**1. Obsidian → GitHub**
- Managed by *Obsidian Git Plugin*
- Commits & pushes the entire vault every 2 hours

**2. GitHub → GPT Chatroom**
- Your GPT is connected to this repo and can:
  - Read the latest CSV data
  - Summarize funding opportunities by region or stage
  - Suggest next-review actions from the Tasks section

**3. GPT → You**
- Run queries such as:
  - *“Show me active MVP grants in Hong Kong.”*
  - *“Which programs are due for review this month?”*
  - *“Summarize Full Product funding eligible for AI automation projects.”*

---

## 🪄 Updating or Adding Grants
1. Open `PropTech_Funding_MERGED_Annotated.csv` in Obsidian or Excel.
2. Add or edit entries.
3. Commit changes — Obsidian Git will sync automatically.
4. The **Funding Tracker** note will update instantly after sync.

**Optional Automation:**
- Run a Python or n8n script to validate URLs weekly and append broken-link flags.
- Use a GitHub Action to raise an issue automatically if any link fails.

---

## 🧠 Tip for Custom GPT
When configuring your custom GPT:
- Grant it access to your GitHub repo.
- Point its retrieval scope to the `2_Funding_&_Grants/` folder.
- Use retrieval prompts like:
  - *“List all funding programs with Stage = MVP and Region = Canada.”*
  - *“Summarize updates since last commit.”*

---

## ✅ Maintenance
| Task | Frequency | Responsible | Notes |
|------|------------|-------------|-------|
| Link check / grant status | Annual (see “Next Review”) | Sam / AI Agent | Validate each Official Link |
| Sync to GitHub | Every 2 h | Obsidian Git Plugin | Auto-commit |
| GPT access test | Monthly | Sam | Verify API retrieval |
| Vault backup | Quarterly | GitHub mirror | Archive to zip if needed |

---

## 💡 Future Expansion
- Add Dataview dashboards for **Learning Progress**, **Project Milestones**, and **Automation Health**.
- Introduce **n8n → GitHub → GPT** webhook chain for real-time grant alerts.
- Include **InvestHK / InnoHK / FedDev Ontario** live API integrations when available.
