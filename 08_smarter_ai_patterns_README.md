# Video 8 — Cloud, Debugging, and a Real Chat Loop

---

## What you'll learn

Three small, practical upgrades to what you built in Video 7:

1. **OpenRouter** — connect to a cloud model when your laptop isn't enough.
2. **Basic Python debugging** — the four moves pro devs actually use.
3. **A real chat loop** — wrap the API call in a function, ask questions until you type `quit`, and learn the parameters that change how the model behaves.

**Files for this video:**
- [08_smarter_ai_patterns.py](08_smarter_ai_patterns.py) — full version with comments
- [08_smarter_ai_patterns_short.py](08_smarter_ai_patterns_short.py) — minimal demo

---

## Part 1 — What is OpenRouter?

[openrouter.ai](https://openrouter.ai) is a single service that gives you **one API key** to talk to dozens of models — GPT-4, Claude, Llama, Mistral, Gemini, and more. They all use the same OpenAI SDK shape you already know.

Why bother?
- Your local model isn't strong enough for a hard task.
- You want to A/B compare two models on the same prompt — change one env var.
- You don't have a powerful laptop but still want to follow along.

The only differences vs Video 6:

| Setting    | LM Studio (Video 6)            | OpenRouter (now)                   |
| ---------- | ------------------------------ | ---------------------------------- |
| `base_url` | `http://localhost:1234/v1`     | `https://openrouter.ai/api/v1`     |
| `api_key`  | any string                     | your key from `openrouter.ai/keys` |
| `model`    | LM Studio model id             | e.g. `openai/gpt-4o-mini`          |

Add to `.env`:

```
OPENROUTER_API_KEY=sk-or-v1-...
OPENROUTER_MODEL=openai/gpt-4o-mini
```

The full file picks OpenRouter automatically when the key is set, else falls back to LM Studio. Same trick we'll use for Azure in Video 10.

---

## Part 2 — Basic Python debugging

You don't need fancy tools. Four moves cover almost everything:

1. **`print()`** — print the variable. Works every time, costs nothing.
2. **`type(x)` and `len(x)`** — when code "doesn't make sense," your variable usually isn't what you think it is. Check.
3. **`breakpoint()`** — built-in. When Python hits this line it pauses and drops you into an interactive prompt where you can type any variable name to inspect it. `c` to continue, `q` to quit.
4. **`try` / `except`** — catch the error, print `type(e).__name__` and `e`, keep the program alive.

In VS Code you can also click the gutter to set a breakpoint visually and press **F5** to run with the debugger attached. Same idea as `breakpoint()`, nicer UI.

---

## Part 3 — A real chat loop, with new parameters

Video 7 hard-coded the questions. Real chats keep going until the user quits. We wrap the API call in a function so we can reuse it cleanly:

```python
def ask(history, user_text, **params):
    history.append({"role": "user", "content": user_text})
    response = client.chat.completions.create(
        model=model, messages=history, **params,
    )
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    return reply
```

Two new Python ideas here:
- **Functions** keep the loop body short and readable.
- **`**params`** lets the caller pass any tuning knob without us listing them all.

### The parameters worth knowing

| Parameter           | What it does                                                          | Typical value   |
| ------------------- | --------------------------------------------------------------------- | --------------- |
| `temperature`       | Randomness. 0 = same answer every time, 1 = creative.                 | 0.2 – 0.7       |
| `max_tokens`        | Hard cap on reply length (1 token ≈ 4 characters).                    | 200 – 800       |
| `top_p`             | Sample only from the top X% most-likely next tokens.                  | 1.0 (default)   |
| `presence_penalty`  | Push the model to bring up **new** topics. Range -2.0 to +2.0.        | 0 – 0.5         |
| `frequency_penalty` | Push the model to **not repeat** the same words. Range -2.0 to +2.0.  | 0 – 0.5         |
| `stop`              | List of strings. Generation stops if any appears.                     | `["\n\n"]` etc. |

The loop:

```python
while True:
    user_text = input("👤 You: ").strip()
    if user_text.lower() in {"quit", "exit", "q"}:
        break
    reply = ask(history, user_text, temperature=0.5, max_tokens=300)
    print(f"🤖 Tutor: {reply}")
```

That's a full multi-turn chat in eight lines.

---

## Try it yourself

1. Run it locally first:
   ```
   python 08_smarter_ai_patterns.py
   ```
2. Get a key from [openrouter.ai/keys](https://openrouter.ai/keys), add the two env vars, run again. Notice that **only** the banner changes.
3. Inside `chat_loop()`, uncomment `presence_penalty=0.3` and `frequency_penalty=0.3`. Ask the same 3 questions twice — once with, once without — and see how repetitive the model gets without them.
4. Replace one of the `print` calls in Part 2 with `breakpoint()` and explore what's in scope.

---

Next: [Video 9](09_copilot_for_devs_README.md) — extend the chat with GitHub Copilot at your side.
