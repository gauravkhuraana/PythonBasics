# Getting Started with Python + AI

An 11-video starter course that takes you from "what is Python?" to "I built a personal AI assistant running on my own laptop."

---

## Who this course is for

- Testers, SDETs, QA engineers who want to add Python + AI to their toolkit — the assignments and capstone are all QA-flavoured.
- You may have zero coding experience.
- You don't want to pay for cloud APIs while you're learning.

By the end you will have built a real Defect Triage Assistant (or one of three other QA-focused mini-projects) running entirely on your laptop.

---

## The 11 Videos

| # | Title | Materials |
|---|-------|-----------|
| 1 | Welcome & What is Python + AI | [README](01_what_is_python_README.md) |
| 2 | Setting Up Your AI Workshop | [README](02_setup_vscode_copilot_README.md) |
| 3 | Python Essentials for AI in 15 Minutes | [Code](03_python_essentials.py) · [Short](03_python_essentials_short.py) · [README](03_python_essentials_README.md) |
| 4 | Pro Project Setup (venv, .env, .gitignore) | [Code](04_project_setup.py) · [Short](04_project_setup_short.py) · [README](04_project_setup_README.md) |
| 5 | Run AI on Your Laptop with LM Studio | [README](05_lm_studio_README.md) |
| 6 | Your First Python → Local LLM Program | [Code](06_first_local_ai_call.py) · [Short](06_first_local_ai_call_short.py) · [README](06_first_local_ai_call_README.md) |
| 7 | Multi-Turn Chat with Memory | [Code](07_chat_with_memory.py) · [Short](07_chat_with_memory_short.py) · [README](07_chat_with_memory_README.md) |
| 8 | Smarter AI Patterns (OpenRouter, debugging, chat loop) | [Code](08_smarter_ai_patterns.py) · [Short](08_smarter_ai_patterns_short.py) · [README](08_smarter_ai_patterns_README.md) |
| 9 | Code Faster with GitHub Copilot | [README](09_copilot_for_devs_README.md) |
| 10 | Build a Personal Life Assistant | [Code](10_life_assistant.py) · [Short](10_life_assistant_short.py) · [README](10_life_assistant_README.md) |
| 11 | Assignments: Key Concepts & Tips | [README](11_assignments_recap_README.md) |

After the videos: [Wrap-Up & Your Next Steps](next_steps_README.md) — capstone brief and where to go from here.

---

## Assignments (QA-themed)

Three graded assignments unlock as you progress:

| After Video | Difficulty | Assignment | What you build |
|:-----------:|:----------:|------------|----------------|
| 3 | Easy | [Test Case Catalog](assignments/assignment_1_test_case_catalog/) | Pure-Python catalog: store, search, summarise test cases |
| 6 | Medium | [Bug Report Generator](assignments/assignment_2_bug_report_generator/) | LLM turns rough bug notes into a polished bug report |
| 9 | Hard | [QA Agent](assignments/assignment_3_qa_agent/) | Multi-skill agent: test plan / triage / run summary / risk |

A bonus capstone — the [Defect Triage Assistant](assignments/capstone_options/) — is also available for those who want a fourth project with a real interactive loop.

Reference solutions live in [`solutions/`](solutions/) — try each assignment yourself first, then compare.

---

## Quick start

```powershell
# Windows PowerShell — Mac/Linux is similar

# 1. Clone and enter
git clone <repo-url>
cd PythonBasics

# 2. Create + activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Install packages
pip install -r requirements.txt

# 4. Configure environment
Copy-Item .env.example .env
# (edit .env — for Videos 1-9 you only need LOCAL_LLM_* variables)

# 5. Start LM Studio, load a model, click "Start Server" (Video 5)

# 6. Run your first AI program (Video 6)
python 06_first_local_ai_call.py
```

---

## What's installed

```
openai          — OpenAI SDK (also speaks to LM Studio + OpenRouter)
python-dotenv   — load .env files
```

---

## Course philosophy

- Local first. No cloud account, no credit card, no rate limits while learning.
- Build something real. Every concept is taught via a file you'll actually run.
- One short + one long file per video. Use the short one in your demos and the long one to read at your own pace.
- No frameworks until you need them. Pure Python and the OpenAI SDK — that's it.

---

## Connect

- Website: <https://gauravkhurana.com>
- Find this course on Udemy: *(link in course description)*
- Topmate for 1:1 review of your capstone: *(link in course description)*
- If this helped you, star the repo so you can find it later.

---

Made by Gaurav ([gauravkhurana.com](https://gauravkhurana.com)). See you in [Video 1](01_what_is_python_README.md).
