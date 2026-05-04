# Video 10 — Build a Personal Life Assistant

> **Duration:** 15–18 minutes · **Type:** Flagship hands-on build

---

## 🎯 What you'll build

A **menu-driven personal AI assistant** that runs entirely on your laptop:

```
🌟 YOUR PERSONAL LIFE ASSISTANT 🌟

How can I help you today?
  1. 🥗 Diet & Nutrition
  2. 💪 Fitness & Exercise
  3. 🤖 AI & Tech Learning
  4. 🧘 Motivation & Mindset
  5. 💰 Personal Finance
  6. 📚 Book & Learning Recommendations
  7. ⏰ Productivity & Time Management

Pick a number (1-7):
```

Each "mode" loads a different system prompt, giving you a different *expert* on the same chat engine. The conversation has memory across turns. When you `quit`, it sends you off with a thoughtful farewell.

**Files for this video:**
- [10_life_assistant.py](10_life_assistant.py) — full version with comments
- [10_life_assistant_short.py](10_life_assistant_short.py) — minimal demo version

---

## What's new vs Video 7

Video 7 taught chat with memory. Video 8 adds three patterns you'll re-use forever:

1. **Personas via system prompts** — same model, totally different behaviour.
2. **A class-based agent** — `LifeAssistant` wraps the chat loop, history, and stats.
3. **A "second prompt" finale** — the farewell uses a one-shot completion separate from the main thread, showing you can mix conversation patterns in one app.

---

## Architecture

```
┌────────────────────────────────────────────────┐
│  categories = { "1": {name, prompt}, ... }     │  ← persona library
└────────────────────────────────────────────────┘
                       │
                       ▼
┌────────────────────────────────────────────────┐
│  user picks 1-7  →  build LifeAssistant(prompt)│
└────────────────────────────────────────────────┘
                       │
                       ▼
┌────────────────────────────────────────────────┐
│  while True:                                    │
│      user_input = input()                       │
│      if quit: break                             │
│      print(assistant.chat(user_input))          │
└────────────────────────────────────────────────┘
                       │
                       ▼
┌────────────────────────────────────────────────┐
│  farewell (one-shot completion + stats)         │
└────────────────────────────────────────────────┘
```

The `LifeAssistant` class owns:
- `client`, `model` — the LLM connection (passed in, not hard-coded)
- `history` — the message list, seeded with the chosen system prompt
- `chat(user_message)` — append → send → append → return
- `question_count` — tiny stat for the farewell

---

## Why dependency injection on `client`?

Notice the constructor takes `client` and `model` as parameters:

```python
assistant = LifeAssistant(client, model, system_prompt, name)
```

Because `client` is passed in, swapping providers (e.g. to a cloud model) only changes the top of the file. The assistant itself doesn't care.

---

## Try it yourself

1. Make sure LM Studio is running (Video 5).
2. `python 10_life_assistant.py`
3. Pick a category (start with 4 — Motivation, it's the most fun on small models).
4. Ask 3-4 questions, watching how it remembers earlier context.
5. Type `quit` and read the farewell.

---

## Stretch ideas (optional)

- **Add a `/switch` command** that lets you change category mid-conversation without losing memory.
- **Persist history** to a JSON file so a re-launch picks up where you left off.
- **Add an 8th category** that's specific to *you*.

We'll do something like the first one in Video 9 — using GitHub Copilot to write the code for us.

---

Next: [Video 11](11_assignments_recap_README.md) — assignments key concepts & tips.
