# Video 9 — Code Faster with GitHub Copilot

> **Duration:** 8–10 minutes · **Type:** Demo (live coding)

---

## 🎯 What you'll get from this video

- The **three Copilot surfaces** every Python+AI dev should know: inline, Chat, and slash commands.
- Watch a real feature get added to the Life Assistant from Video 8 — using Copilot.
- Habits that make Copilot dramatically more useful (and ones that backfire).

---

## The three surfaces

### 1. Inline (ghost text)
Just start typing — Copilot suggests the rest in grey. **Tab** to accept, **Esc** to dismiss, **Alt+]** / **Alt+[** to cycle alternatives.

**Best for:** finishing a line, generating a function body from a clear name & docstring.

```python
def count_action_items(text: str) -> int:
    """Return the number of bullet points in `text` that look like action items."""
    # ↑ Write the docstring first — Copilot uses it as a spec.
```

### 2. Copilot Chat (sidebar)
`Ctrl+Alt+I` (or click the Copilot icon). Free-form chat about code. Can read your open file as context.

**Best for:**
- "Explain what this function does"
- "Refactor this into smaller functions"
- "Add a CLI flag for X"

### 3. Slash commands (in Chat)
- `/explain` — walks through selected code
- `/fix` — diagnoses an error and proposes a patch
- `/tests` — drafts unit tests
- `/doc` — adds docstrings

---

## Live demo (this video)

We open `08_life_assistant.py` and add **a `/save` command** that writes the current conversation to a `chat_log.txt` file when the user types `/save` instead of a question.

Steps shown on screen:

1. Highlight the `while True:` loop in the assistant.
2. Open Chat: *"Add a `/save` command. When the user types `/save`, write the entire `assistant.history` (skipping the system message) to `chat_log.txt` and confirm to the user."*
3. Apply the diff Copilot suggests.
4. Run, ask 2 questions, type `/save`, confirm `chat_log.txt` exists.

---

## Habits that work

| Do | Don't |
|----|------|
| Write a clear docstring **before** asking for code | Accept ghost text without reading it |
| Give Copilot Chat the file context (use `#file`) | Paste secrets into Chat |
| Ask "what could go wrong with this?" | Trust Copilot for security-sensitive code |
| Use `/explain` on legacy code you're learning | Skip writing tests because Copilot wrote it |

> 🧠 Rule of thumb: Copilot is a **junior pair programmer**, not a senior. You're the reviewer.

---

## 🟢 Assignment 3 unlocks here

After this video, take **Assignment 3 — QA Agent**:
[assignments/assignment_3_qa_agent/](assignments/assignment_3_qa_agent/)

It's the hardest of the three: a multi-skill QA agent (test plan / bug triage / test-run summary / release risk). Use Copilot freely — explain *what* you want, let it draft, then read every line.

---

Next: [Video 10](10_bonus_cloud_azure_README.md) — same code, but in the cloud.
