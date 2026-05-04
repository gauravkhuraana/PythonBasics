# Video 9 — Code Faster with GitHub Copilot

---

## What you'll get from this video

- The **three Copilot surfaces** every Python+AI dev should know: inline, Chat, and slash commands.
- Watch a real feature get added to the Life Assistant — using Copilot.
- Habits that make Copilot dramatically more useful (and ones that backfire).
- How to sign up for a **free GitHub Copilot account** and activate it in VS Code.
- How to point Copilot Chat at your **local LM Studio model** — free, private, no rate limits.

---

---

## Get GitHub Copilot Free — Sign Up & Activate

### 1. Sign up (it's free)

1. Go to **<https://github.com/features/copilot>** and click **"Start for free"**.
2. Sign in with your GitHub account (or create one — also free).
3. The **Free tier** gives you:
   - 2,000 code completions per month
   - 50 Copilot Chat messages per month
   - No credit card required

### 2. Install the VS Code extensions

Open VS Code → Extensions panel (`Ctrl+Shift+X`) → search and install both:

| Extension | What it adds |
|-----------|-------------|
| **GitHub Copilot** | Inline ghost-text completions |
| **GitHub Copilot Chat** | Sidebar chat + slash commands |

### 3. Activate (sign in)

1. In VS Code, click the **Accounts** icon in the bottom-left Activity Bar (person silhouette).
2. Select **"Sign in with GitHub to use GitHub Copilot"**.
3. A browser tab opens — authorise the connection.
4. Back in VS Code, the **Copilot icon** (two overlapping circles) in the status bar turns solid. You're live.

> 💡 **Verify:** Open any `.py` file, type `def greet(name`, and a ghost-text completion should appear in grey. Press **Tab** to accept.

---

## Connect Copilot Chat to a Local LM Studio Model

Copilot Chat can use your local LM Studio model instead of (or in addition to) the cloud. This is 100% free, fully private, and has no monthly message cap.

**Pre-requisite:** LM Studio is running with a model loaded and the local server started on port 1234 (Video 5).

### Steps

1. Open **Copilot Chat** (`Ctrl+Alt+I` or click the Copilot icon in the sidebar).
2. In the chat input box, click the **model picker dropdown** (shows the current model name, e.g. *"GPT-4o"*).
3. Choose **"Use a different model…"** → **"Add OpenAI-compatible endpoint"**.
4. Fill in:
   ```
   Base URL:  http://localhost:1234/v1
   API Key:   lm-studio          (any string — local server ignores it)
   Model ID:  (paste the model name from LM Studio's server tab, e.g. lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF)
   ```
5. Click **Save**. The model picker now shows your local model. Select it.
6. Ask a question in chat — the response comes from LM Studio on your machine.

### Trade-offs

| | Local (LM Studio) | OpenRouter | Cloud (GitHub Copilot) |
|---|---|---|---|
| Cost | Free, unlimited | Free tier + pay-per-token | 50 messages/month on free tier |
| Privacy | All traffic stays on your machine | Requests go to OpenRouter | Sent to GitHub/OpenAI |
| Quality | Good for small tasks (3B–8B models) | 100+ models incl. GPT-4o / Claude | Best-in-class (GPT-4o / Claude) |
| Speed | Depends on your hardware | Fast, consistent | Fast, consistent |
| Internet | Not required | Required | Required |

> 🧠 **Tip:** Use the local model for bulk tasks (generating lots of test cases, scaffolding repetitive code). Save your cloud messages for complex questions where quality really matters.

---

## 🌐 Use OpenRouter as an AI Backend

[OpenRouter](https://openrouter.ai) gives you a **single OpenAI-compatible API** that routes to dozens of models — GPT-4o, Claude 3.5, Gemini, Llama 3, Mistral, and more — all through one endpoint and one API key.

**Why it's useful for this course:** no model is locked behind a single provider, free-tier models are available, and the same `openai` Python client you already know works without changes.

### Quick start

1. Go to **<https://openrouter.ai>** and create a free account.
2. Under **Keys**, generate an API key.
3. Add it to your `.env` file:
   ```
   OPENROUTER_API_KEY=sk-or-...
   OPENROUTER_MODEL=openai/gpt-4o-mini   # or any model slug from openrouter.ai/models
   ```
4. The companion script `openrouter.py` in this repo already shows the full pattern:

```python
from openai import OpenAI
import os

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

response = client.chat.completions.create(
    model=os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini"),
    messages=[{"role": "user", "content": "In 3 bullets: why is Python great for AI?"}],
)
print(response.choices[0].message.content)
```

### Connect OpenRouter to Copilot Chat

You can point Copilot Chat at OpenRouter the same way you point it at LM Studio:

1. Open Copilot Chat → model picker → **"Add OpenAI-compatible endpoint"**.
2. Fill in:
   ```
   Base URL:  https://openrouter.ai/api/v1
   API Key:   <your OPENROUTER_API_KEY>
   Model ID:  openai/gpt-4o-mini   (or any slug from openrouter.ai/models)
   ```
3. Click **Save** and select the model.

### How the three options compare

| | LM Studio (local) | OpenRouter | GitHub Copilot (cloud) |
|---|---|---|---|
| Cost | Free, unlimited | Free tier + pay-per-token | 50 messages/month free |
| Privacy | 100% local | Requests go to OpenRouter | Sent to GitHub/OpenAI |
| Model choice | Whatever you downloaded | 100+ models, one API | GPT-4o / Claude (fixed) |
| Setup | Install + download model | Account + API key | GitHub account |
| Internet required | No | Yes | Yes |

> 💡 **Best strategy:** prototype and bulk-generate with LM Studio, switch to OpenRouter when you need a specific model (e.g. Claude for nuanced reasoning), and keep Copilot Chat for pair-programming inside VS Code.

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

We open `10_life_assistant.py` and add **a `/save` command** that writes the current conversation to a `chat_log.txt` file when the user types `/save` instead of a question.

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

## Assignment 3 unlocks here

After this video, take **Assignment 3 — QA Agent**:
[assignments/assignment_3_qa_agent/](assignments/assignment_3_qa_agent/)

It's the hardest of the three: a multi-skill QA agent (test plan / bug triage / test-run summary / release risk). Use Copilot freely — explain *what* you want, let it draft, then read every line.

---

Next: [Video 10](10_life_assistant_README.md) — build the Personal Life Assistant.
