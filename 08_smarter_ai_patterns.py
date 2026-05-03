"""
================================================================
08_smarter_ai_patterns.py
GO BEYOND VIDEO 7 — Cloud, Debugging, and a Real Chat Loop
================================================================

🎯 GOAL:
   Three small upgrades to what you already know:
     1. Use a cloud model via OpenRouter (when LM Studio isn't enough)
     2. Learn basic Python debugging (the same tricks pro devs use)
     3. Wrap your chat in a loop and explore the parameters
        that control how the model behaves

This file covers:
  ✅ PART 1 — What is OpenRouter and how to connect to it
  ✅ PART 2 — Basic debugging: print, type, breakpoint(), VS Code
  ✅ PART 3 — A real chat loop (ask → reply → ask → ... → quit),
              wrapped in a function, with new tuning parameters

Prerequisites:
  - You've completed Videos 6 & 7 (local LLM + chat memory)
  - .env contains EITHER:
        LOCAL_LLM_BASE_URL  +  LOCAL_LLM_MODEL    (Video 5)
    OR (and this is the new bit):
        OPENROUTER_API_KEY  +  OPENROUTER_MODEL

Run this file:  python 08_smarter_ai_patterns.py
================================================================
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

print("=" * 60)
print("VIDEO 8 — Cloud, Debugging, and a Real Chat Loop")
print("=" * 60)


# ============================================================
# PART 1: What is OpenRouter — and how to connect to it
# ============================================================
# OpenRouter is a single website (openrouter.ai) that gives you
# ONE API key to talk to dozens of models — GPT-4, Claude, Llama,
# Mistral, Gemini... — all using the SAME OpenAI SDK shape.
#
# Why it's useful:
#   • Your laptop model isn't strong enough for a hard task?
#     Switch to a bigger one with one line of config.
#   • You want to compare two models for the same prompt?
#     Just change OPENROUTER_MODEL.
#
# The ONLY thing that changes vs Video 6:
#       base_url    → https://openrouter.ai/api/v1
#       api_key     → your OpenRouter key (from openrouter.ai/keys)
#       model name  → e.g. "openai/gpt-4o-mini"
#
# Everything else (messages, response.choices[0]...) is identical.
print("\n" + "-" * 60)
print("PART 1 — Connect to OpenRouter")
print("-" * 60)

if os.getenv("OPENROUTER_API_KEY"):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
    )
    model = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")
    where = "CLOUD (OpenRouter)"
else:
    # Fall back to LM Studio so the file still works offline.
    client = OpenAI(
        base_url=os.getenv("LOCAL_LLM_BASE_URL", "http://localhost:1234/v1"),
        api_key="lm-studio",
    )
    model = os.getenv("LOCAL_LLM_MODEL", "local-model")
    where = "LOCAL (LM Studio)"

print(f"✅ Using {where}")
print(f"   model = {model}")

# Tiny "hello" call to prove the connection works.
hello = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Reply with the single word: OK."}],
    max_tokens=10,
    temperature=0,
)
print(f"   Connection test → {hello.choices[0].message.content.strip()!r}")


# ============================================================
# PART 2: Basic Python debugging
# ============================================================
# When something goes wrong, you don't need fancy tools. Three
# techniques cover 90% of what professional devs do:
#
#   1. PRINT DEBUGGING
#      Just print the variable. Sounds silly, works every time.
#
#   2. type() and len()
#      "Why did my code break?" — usually because the variable
#      isn't what you THINK it is. Check it.
#
#   3. breakpoint()
#      A built-in Python function that PAUSES execution and drops
#      you into an interactive prompt. You can inspect anything.
#      In VS Code you can also click the gutter to set one
#      visually and hit F5 to start debugging.
print("\n" + "-" * 60)
print("PART 2 — Three debugging techniques")
print("-" * 60)

# Suppose this list comes from somewhere and you're not sure
# what's inside.
mystery = [42, "hello", {"role": "user", "content": "hi"}, None]

# Technique 1 — print
print("\n[print]      mystery =", mystery)

# Technique 2 — type() and len()
print(f"[type/len]   type(mystery)={type(mystery).__name__}, len={len(mystery)}")
for i, item in enumerate(mystery):
    print(f"             [{i}] type={type(item).__name__:<5} value={item!r}")

# Technique 3 — breakpoint()
# Uncomment the next line to try it: when Python hits it, you'll
# get a (Pdb) prompt where you can type variable names to inspect
# them. Type 'c' to continue, 'q' to quit.
#
# breakpoint()
print("[breakpoint] Uncomment the line in source to try it. (Skipped here.)")

# Bonus — try / except is your safety net. Print the error
# instead of letting the program crash.
print("\n[try/except] safe division demo:")
for x in (10, 0, "five"):
    try:
        result = 100 / x
        print(f"   100 / {x!r:<6} = {result}")
    except Exception as e:
        # type(e).__name__ tells you WHICH error — very useful.
        print(f"   100 / {x!r:<6} → {type(e).__name__}: {e}")


# ============================================================
# PART 3: A real chat loop, with new model parameters
# ============================================================
# In Video 7 we hard-coded the questions. A real chat asks the
# user repeatedly until they type 'quit'. We'll wrap the API
# call in a FUNCTION so we can reuse it cleanly.
#
# We'll also explore parameters of chat.completions.create that
# you haven't seen yet:
#
#   temperature   — randomness (0 = same answer every time, 1 = creative)
#   max_tokens    — hard cap on the reply length (1 token ≈ 4 chars)
#   top_p         — alternative to temperature (sample from top X%
#                   of probable next tokens). Leave at 1.0 unless
#                   you specifically need it.
#   presence_penalty  — push the model to bring up NEW topics
#                       (range -2.0 to +2.0, 0 = off)
#   frequency_penalty — push it to NOT repeat the same words
#                       (same range, 0 = off)
#   stop          — list of strings; the model stops if it
#                   generates any of them.
print("\n" + "-" * 60)
print("PART 3 — Chat loop + parameter tour")
print("-" * 60)


def ask(client, model, history, user_text, **params):
    """
    Send one user turn, return the assistant's reply.
    `history` is a list of {role, content} dicts; we APPEND
    the new user message and the assistant reply to it.

    `**params` lets the caller pass any of the tuning knobs
    (temperature, max_tokens, top_p, etc.) without us having
    to list them all here.
    """
    history.append({"role": "user", "content": user_text})

    response = client.chat.completions.create(
        model=model,
        messages=history,
        **params,
    )

    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    return reply


def chat_loop(client, model):
    """A simple REPL: ask → reply → ask → ... until 'quit'."""
    history = [
        {"role": "system",
         "content": "You are a friendly, concise tutor. 3 short bullets max."}
    ]

    print("\nType your question. Type 'quit' to exit.\n")
    while True:
        try:
            user_text = input("👤 You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not user_text:
            continue
        if user_text.lower() in {"quit", "exit", "q"}:
            print("👋 Bye!")
            break

        try:
            reply = ask(
                client, model, history, user_text,
                temperature=0.5,
                max_tokens=300,
                # Try uncommenting these to feel their effect:
                # top_p=0.9,
                # presence_penalty=0.3,
                # frequency_penalty=0.3,
                # stop=["\n\n"],
            )
        except Exception as e:
            print(f"❌ {type(e).__name__}: {e}")
            continue

        print(f"\n🤖 Tutor: {reply}\n")

    print(f"📊 Conversation length: {len(history)} messages "
          f"(including system prompt).")


# Run the loop. Comment this out if you just want to read the file.
chat_loop(client, model)


# ============================================================
# Key takeaways
# ============================================================
print("\n" + "=" * 60)
print("🎯 KEY TAKEAWAYS")
print("=" * 60)
print("""
   PART 1 — OpenRouter is one key, one URL, dozens of models.
            Same SDK as LM Studio — only base_url + api_key change.

   PART 2 — When stuck: print it, check type()/len(), drop a
            breakpoint(). 90% of bugs solved without fancy tools.

   PART 3 — Wrap repeated calls in a function. Use **kwargs so
            the caller can pass any tuning parameter. The big
            knobs are temperature, max_tokens, top_p, and the
            presence/frequency penalties.

🚀 Next: Video 9 — pair with GitHub Copilot to extend the
   Life Assistant we'll build in Video 11.
""")
