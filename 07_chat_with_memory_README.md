# Video 7 — Multi-Turn Chat with Memory

> **Duration:** 10–12 minutes · **Type:** Hands-on code

---

## 🎯 What you'll learn

- The three message roles: `system`, `user`, `assistant`.
- The "the model has no memory — *you* give it memory" pattern.
- How a system prompt shapes behaviour without changing the model.

**Files for this video:**
- [07_chat_with_memory.py](07_chat_with_memory.py) — full version with comments
- [07_chat_with_memory_short.py](07_chat_with_memory_short.py) — minimal demo

---

## The mental model

A chat completion is **stateless**. Every call is independent.

To create the *illusion* of memory, you keep a list of messages and resend the entire list with each call:

```
Call 1:  [system, user1]                                        → assistant1
Call 2:  [system, user1, assistant1, user2]                     → assistant2
Call 3:  [system, user1, assistant1, user2, assistant2, user3]  → assistant3
```

Once you internalise this, every "ChatGPT clone" tutorial on the internet stops being magic.

---

## The three roles

| Role | Who writes it | Purpose |
|------|--------------|---------|
| `system` | You (developer) | Behaviour, persona, rules. Sent once at the top. |
| `user`   | The human | Each new question or input. |
| `assistant` | The model | The model's previous reply, fed back in. |

---

## Pattern in 5 lines

```python
messages = [{"role": "system", "content": "You are concise."}]
messages.append({"role": "user", "content": "Hi!"})
reply = client.chat.completions.create(model=model, messages=messages).choices[0].message.content
messages.append({"role": "assistant", "content": reply})
# next user turn → repeat last 3 lines
```

---

## Watch out for

- **Context window.** Every model has a token limit (e.g., 4K, 8K, 32K). Keep the list bounded — drop oldest turns or summarize after N messages.
- **Temperature for tasks vs chat.** Use lower (0.2–0.4) for factual / extraction tasks. Default 0.7 for general chat.
- **Empty replies on small models.** Local 3B models sometimes "use all tokens for thinking." Raise `max_tokens` or ask simpler questions.

---

Next: [Video 8](08_life_assistant_README.md) — wrap this pattern into a class and ship a real assistant.
