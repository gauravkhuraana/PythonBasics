"""
08_smarter_ai_patterns_short.py — three small upgrades to Video 7
   1. Connect to OpenRouter (cloud) — same SDK, different URL
   2. Basic Python debugging: print, type(), breakpoint(), try/except
   3. A chat loop in a function, with new tuning parameters
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# --- 1. Connect: cloud if key is set, otherwise LM Studio -----
if os.getenv("OPENROUTER_API_KEY"):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
    )
    model = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")
    print("Using OpenRouter (cloud):", model)
else:
    client = OpenAI(
        base_url=os.getenv("LOCAL_LLM_BASE_URL", "http://localhost:1234/v1"),
        api_key="lm-studio",
    )
    model = os.getenv("LOCAL_LLM_MODEL", "local-model")
    print("Using LM Studio (local):", model)


# --- 2. Tiny debugging warm-up --------------------------------
mystery = [42, "hello", None]
print("\nDEBUG demo:")
print("  print →", mystery)
print(f"  type → {type(mystery).__name__}, len → {len(mystery)}")
for i, x in enumerate(mystery):
    print(f"  [{i}] {type(x).__name__:<5} {x!r}")

# breakpoint()   # uncomment to drop into Pdb here
try:
    100 / 0
except Exception as e:
    print(f"  caught {type(e).__name__}: {e}")


# --- 3. Chat loop in a function -------------------------------
def ask(history, user_text, **params):
    """Send one user turn, append reply to history, return reply text."""
    history.append({"role": "user", "content": user_text})
    response = client.chat.completions.create(
        model=model,
        messages=history,
        **params,
    )
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    return reply


def chat_loop():
    history = [{"role": "system", "content": "You are a concise tutor. 3 bullets max."}]
    print("\nAsk anything. Type 'quit' to exit.\n")
    while True:
        user_text = input("👤 You: ").strip()
        if user_text.lower() in {"quit", "exit", "q"}:
            print("👋 Bye!")
            break
        if not user_text:
            continue
        reply = ask(
            history, user_text,
            temperature=0.5,        # 0 = focused, 1 = creative
            max_tokens=300,         # cap reply length
            # top_p=0.9,            # try these too:
            # presence_penalty=0.3, # encourage NEW topics
            # frequency_penalty=0.3,# discourage REPETITION
        )
        print(f"\n🤖 Tutor: {reply}\n")
    print(f"messages in memory: {len(history)}")


chat_loop()
