# Video 6 — Your First Python → Local LLM Program

---

## What you'll build

A 30-line Python script that sends a prompt to the LLM running inside LM Studio and prints the answer.

**Files for this video:**
- [06_first_local_ai_call.py](06_first_local_ai_call.py) — fully commented walkthrough
- [06_first_local_ai_call_short.py](06_first_local_ai_call_short.py) — minimal demo version

---

## Pre-flight check

✅ LM Studio is open
✅ A model is loaded in the **Server** tab
✅ The server is **started** (you see `http://localhost:1234`)
✅ Your `.env` has `LOCAL_LLM_BASE_URL` and `LOCAL_LLM_MODEL`

If any of these aren't true, replay [Video 5](05_lm_studio_README.md).

---

## The big idea

```
Your Python  ──►  http://localhost:1234/v1  ──►  Model running on your CPU/GPU
            (OpenAI SDK)         (LM Studio's OpenAI-compatible server)
```

Because LM Studio speaks OpenAI's API format, **the same `openai` Python package** that talks to OpenAI/Azure can talk to your local server. You only change two things:

1. `base_url` → `http://localhost:1234/v1`
2. `api_key` → any non-empty string (it's ignored locally)

---

## Code walkthrough

### 1. Load config from `.env`

```python
from dotenv import load_dotenv
import os

load_dotenv()
base_url = os.getenv("LOCAL_LLM_BASE_URL", "http://localhost:1234/v1")
model    = os.getenv("LOCAL_LLM_MODEL", "local-model")
```

Why `.env`? You learned this in Video 4 — secrets and config out of code.

### 2. Create the client

```python
from openai import OpenAI

client = OpenAI(base_url=base_url, api_key="lm-studio")
```

Note we use `OpenAI`, not `AzureOpenAI`. LM Studio is OpenAI-compatible, not Azure-flavoured.

### 3. Send a prompt

```python
response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "user", "content": "Why is Python great for AI?"}
    ],
    temperature=0.7,
    max_tokens=200,
)
print(response.choices[0].message.content)
```

You're already familiar with the `messages` shape from Video 3 — a list of dicts with `role` and `content`.

---

## Concepts introduced

### `temperature`
Controls randomness.
- `0.0` — deterministic, repeatable, "boring"
- `0.7` — balanced (default we use)
- `1.0+` — creative, surprising, sometimes nonsensical

Try the bonus block at the bottom of `06_first_local_ai_call.py` to see the same prompt at temperature `0.2` and `1.0`.

### `max_tokens`
A token is roughly **¾ of a word** in English. `max_tokens=200` caps the response at ~150 words. Local LLMs are slow per token, so keep this modest while learning.

### Tokens & cost
For local LLMs, "cost" = your CPU time. For cloud LLMs, it's $ — that's why every cloud API gives you token usage in `response.usage`.

---

## Common errors

| Error | Likely cause |
|-------|--------------|
| `Connection refused` | LM Studio server not started |
| `404` on `/v1/chat/completions` | Wrong `base_url` (check trailing `/v1`) |
| Empty response | Model finished thinking but used all tokens — raise `max_tokens` |
| Hangs forever | Model is loading on first call — wait once, then it's fast |

---

## Assignment 2 unlocks here

After this video you have everything needed for **Assignment 2 — Bug Report Generator**:
[assignments/assignment_2_bug_report_generator/](assignments/assignment_2_bug_report_generator/)

You'll build a script that turns rough bug notes (one-line summary + repro steps + environment) into a polished, structured bug report — the kind any developer would happily pick up.

---

Next: [Video 7](07_chat_with_memory_README.md) — keeping a conversation alive.
