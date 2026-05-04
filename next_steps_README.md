# Wrap-Up & Your Next Steps

---

## 🎉 What you've actually learned

- Python's data types and structures most relevant to AI work.
- How to set up a clean, secure Python project (`venv`, `.env`, `.gitignore`).
- How to run an LLM **on your own laptop** with LM Studio.
- The OpenAI SDK pattern that works for **both local and cloud** models.
- Multi-turn conversations with system prompts and message history.
- Building a real, persona-driven AI assistant.
- Shipping faster with GitHub Copilot.

That's a full-stack starter foundation for everything that comes next.

---

## 🏆 Your capstone — pick one

Take what you built in Video 8 and one of the assignments and ship it as a small project. Pick whichever excites you most:

| # | Project | Difficulty | Source files |
|---|---------|-----------|--------------|
| 1 | **Test Case Catalog++** — extend Assignment 1 with an AI helper that suggests missing edge cases for each module | ⭐ | [assignments/assignment_1_test_case_catalog/](assignments/assignment_1_test_case_catalog/) |
| 2 | **Bug Report Generator++** — turn Assignment 2 into a CLI tool with platform presets and severity calibration | ⭐⭐ | [assignments/assignment_2_bug_report_generator/](assignments/assignment_2_bug_report_generator/) |
| 3 | **QA Agent** — finish Assignment 3 (multi-skill: test plan, triage, run summary, risk) | ⭐⭐⭐ | [assignments/assignment_3_qa_agent/](assignments/assignment_3_qa_agent/) |
| 4 | **Defect Triage Assistant** — interactive triage with cross-bug memory | ⭐⭐⭐ | [assignments/capstone_options/](assignments/capstone_options/) |

**Definition of done** for any capstone:
- It runs end-to-end with a single `python file.py`.
- It uses your local LLM (LM Studio) by default.
- The code is in a public GitHub repo with a README.
- You've recorded a 60-second screen recording of it working.

Submit your repo link via the Topmate link in the course description for a 1:1 review.

---

## 🛣️ Where to go next

In rough order of usefulness:

1. **Function calling / tools** — let the LLM call your Python functions. (search: "openai tools api")
2. **RAG (Retrieval-Augmented Generation)** — feed the LLM your own documents. Try [LlamaIndex](https://www.llamaindex.ai/) or [LangChain](https://www.langchain.com/).
3. **Streaming responses** — make the UI feel snappy: `stream=True` on chat completions.
4. **A web UI** — wrap your assistant in [Streamlit](https://streamlit.io/) or [Gradio](https://www.gradio.app/) (~50 extra lines).
5. **Better local models** — try `ollama`, `llama.cpp`, or quantized 7B/8B models when your hardware allows.
6. **Agent frameworks** — when you're ready: LangGraph, Microsoft Agent Framework, OpenAI Agents SDK.

---

## Stay in touch

- 🌐 **Website** — <https://gauravkhurana.com>
- ⭐ **Star the repo** so you can find it later.
- 💬 **Topmate** — book a 1:1 if you want feedback on your capstone.
- 🎥 **Udemy reviews** — they help more than you think; please leave one if this course was useful.

---

## Final word

You started this course not knowing how a `.py` file runs.
You're ending it with an AI assistant that *you* built and *you* understand — running on your own machine.

That's not nothing. Now go ship something. 🚀

— Gaurav
