# Video 1 — Welcome & What is Python + AI

---

## What you'll get from this video

- Why this course exists and who it's for
- A 30-second peek at the **final project** (a personal AI assistant running on your laptop)
- What Python actually is and why it dominates AI
- How a `.py` file gets executed (interpreted vs compiled — in plain English)
- The roadmap for the next 10 videos

---

## Course promise

By the end of this 11-video course you will:

1. Understand the Python building blocks needed to talk to an AI model.
2. Run an AI model **on your own laptop** (no cloud, no credit card, no rate limits).
3. Build and modify a personal AI assistant.
4. Know exactly what to learn next.

This is a **starter course**. We optimize for "you build something real and you understand it" — not for covering every Python feature.

---

## 🐍 What is Python?

Python is a **high-level, general-purpose programming language**. For our purposes, three facts matter:

| Fact | Why it matters for AI |
|------|----------------------|
| It's **interpreted**, not compiled | You can write a line and run it. No build step. Fast feedback loop. |
| It has a **massive ecosystem** | Almost every AI library (OpenAI SDK, PyTorch, transformers, LangChain…) is Python-first. |
| The syntax is **close to English** | `for item in list:` reads exactly like what it does. |

### Interpreted vs Compiled (one-liner)

- **Compiled** (C, C++, Go): write code → translate the *whole* file to machine code → run.
- **Interpreted** (Python): write code → Python reads it line-by-line and runs it directly.

That's why you can do `python myfile.py` and it just works — there's no separate build step.

> 💡 Technically Python compiles to bytecode first, then interprets that — but for a beginner, "it runs your file directly" is the right mental model.

---

## ▶️ How a Python program runs

```
your_file.py  ──►  python interpreter  ──►  output in terminal
```

Three ways you'll run code in this course:

1. **Terminal**: `python my_file.py`
2. **VS Code Run button** (▶️ at top right of the editor)
3. **REPL** (Read-Eval-Print Loop): just type `python` to get an interactive prompt

---

## 🗺️ Course roadmap

| # | Video | What you'll do |
|---|-------|---------------|
| 1 | Welcome & What is Python + AI | *(this video)* |
| 2 | Setting Up Your AI Workshop | Install Python, VS Code, Copilot |
| 3 | Python Essentials for AI in 15 Minutes | Variables, lists, dicts, loops, functions |
| 4 | Pro Project Setup | venv, requirements, `.env`, `.gitignore` |
| 5 | Run AI on Your Laptop with LM Studio | Install + load a local model |
| 6 | Your First Python → Local LLM Program | First real AI API call (local!) |
| 7 | Multi-Turn Chat with Memory | System prompts + conversation history |
| 8 | Build a Personal Life Assistant | **Flagship hands-on build** |
| 9 | Code Faster with GitHub Copilot | Inline + Chat + /explain + /fix |
| 10 | Build a Personal Life Assistant | Menu-driven multi-persona chat on your local LLM |
| 11 | Wrap-Up & Your Next Steps | Pick a capstone, learn what's next |

---

## ✅ Action items before Video 2

- Make sure you can open a terminal on your machine (Windows: PowerShell, Mac/Linux: Terminal).
- Have ~30 minutes for the next video — there's a small install.

See you in [Video 2](02_setup_vscode_copilot_README.md). 🚀
