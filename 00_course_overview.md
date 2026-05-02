# Course Overview — Getting Started with Python + AI

> A learner-facing snapshot of what's in the course, what you need beforehand, and what you'll be able to do at the end.

---

## At a glance

| | |
|---|---|
| **Audience** | Testers / SDETs / QA engineers — no coding experience needed |
| **Level** | Absolute beginner |
| **Duration** | ~2 hours of video, ~4–6 hours including assignments |
| **Format** | Pre-recorded videos + working code + 3 graded assignments + 1 capstone |
| **Outcome** | A QA-focused AI assistant running on **your laptop** that you understand line by line |
| **Cost to follow along** | $0 (LM Studio is free; cloud is bonus only) |

---

## ✅ What you need before Video 1

| Software | Purpose | Where |
|----------|---------|-------|
| Python 3.11+ | Run the code | <https://www.python.org/downloads/> |
| VS Code | Write the code | <https://code.visualstudio.com/> |
| VS Code Python extension | IntelliSense + Run button | VS Code Extensions panel |
| GitHub Copilot *(optional)* | Used in Video 9 | VS Code Extensions panel |
| LM Studio | Run AI on your laptop | <https://lmstudio.ai/> (installed in Video 5) |

System hints for LM Studio: at least **8 GB RAM** (16 GB ideal), **5 GB free disk**, any modern CPU. A discrete GPU is great but not required for the small models we use.

---

## 🎯 What you'll learn (by section)

### Section 1 — Foundations (Videos 1–3)
What Python is, how it runs, and just enough syntax to build with it. Examples are framed around test cases and QA workflows.

### Section 2 — Project setup & first local AI call (Videos 4–6)
Pro project hygiene (`venv`, `.env`, `.gitignore`), getting a model running locally with LM Studio, and your first prompt → response in Python.

### Section 3 — Building conversational AI (Videos 7–9)
Multi-turn chat (with a real test-run-summary example), system prompts, a class-based personal assistant, and shipping faster with GitHub Copilot.

### Section 4 — Beyond local (Videos 10–11)
Same code, swapped to Azure OpenAI in the cloud. Then a wrap-up and capstone brief.

---

## 🟢 Assignments (QA-themed)

| # | Difficulty | Builds |
|---|:---------:|--------|
| 1 | ⭐ | Test Case Catalog (pure Python) |
| 2 | ⭐⭐ | Bug Report Generator (first LLM call) |
| 3 | ⭐⭐⭐ | QA Agent (multi-skill: plan, triage, summary, risk) |

Bonus capstone: **Defect Triage Assistant** with cross-bug memory.

---

## 🏆 Final capstone

In Video 11 you pick **one** mini-project to extend and submit (or invent your own). All four options are in [`assignments/`](assignments/), including the bonus **Defect Triage Assistant** with persistent cross-bug memory.

---

## ❓ FAQ

**Do I need prior coding experience?**
No. Video 3 covers everything you need.

**Do I need a paid Azure / OpenAI account?**
No — the main path is fully local. Video 10 (cloud) is a bonus.

**My laptop is old. Will LM Studio work?**
Probably yes with a 3B Q4 model. If responses are very slow, that's expected on CPU; outputs will still be coherent for learning.

**Can I follow along on Mac / Linux?**
Yes. Where commands differ, the README calls it out.

**Will the code I write here scale to a real product?**
The patterns will. The exact local LLM probably won't — but Video 10 shows you the swap.

---

## 📁 Repository map

```
PythonBasics/
├─ README.md                              ← Course landing page
├─ 00_course_overview.md                  ← (you are here)
├─ 01_what_is_python_README.md            ← V1 notes
├─ 02_setup_vscode_copilot_README.md      ← V2 install guide
├─ 03_python_essentials.{py,_short.py,_README.md}
├─ 04_project_setup.{py,_short.py,_README.md}
├─ 05_lm_studio_README.md                 ← V5 tool walkthrough
├─ 06_first_local_ai_call.{py,_short.py,_README.md}
├─ 07_chat_with_memory.{py,_short.py,_README.md}
├─ 08_life_assistant.{py,_short.py,_README.md}
├─ 09_copilot_for_devs_README.md          ← V9 demo notes
├─ 10_bonus_cloud_azure.{py,_short.py,_README.md}
├─ 11_next_steps_README.md                ← Outro + capstone brief
├─ assignments/
│   ├─ assignment_1_test_case_catalog/
│   ├─ assignment_2_bug_report_generator/
│   ├─ assignment_3_qa_agent/
│   └─ capstone_options/                  ← Bonus: Defect Triage Assistant
├─ solutions/                             ← (gitignored)
├─ requirements.txt
├─ .env.example
└─ .gitignore
```

---

## 📬 Author

Made by Gaurav — <https://gauravkhurana.com>

---

Ready? Open [Video 1's README](01_what_is_python_README.md) and let's go. 🚀
