"""
================================================================
06_first_local_ai_call.py
YOUR FIRST PYTHON → LOCAL LLM PROGRAM
================================================================

🎯 GOAL:
   Send your first prompt to a model running on YOUR laptop
   (via LM Studio's OpenAI-compatible server).

This file covers:
  ✅ Pointing the OpenAI SDK at a local server
  ✅ Sending a chat completion request
  ✅ Reading the response and token usage
  ✅ Tweaking temperature for creativity

Prerequisites (from Video 5):
  - LM Studio installed
  - A model downloaded and loaded
  - "Start Server" clicked → server running on http://localhost:1234

Run this file:  python 06_first_local_ai_call.py
================================================================
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# ============================================================
# STEP 1: Load configuration from .env
# ============================================================
# We put two values in .env:
#   LOCAL_LLM_BASE_URL = http://localhost:1234/v1
#   LOCAL_LLM_MODEL    = <model id shown in LM Studio Server tab>
load_dotenv()

base_url = os.getenv("LOCAL_LLM_BASE_URL", "http://localhost:1234/v1")
model = os.getenv("LOCAL_LLM_MODEL", "local-model")

print("=" * 60)
print("YOUR FIRST PYTHON → LOCAL LLM PROGRAM")
print("=" * 60)
print(f"\n📡 Base URL: {base_url}")
print(f"🤖 Model:    {model}")


# ============================================================
# STEP 2: Create the client
# ============================================================
# The OpenAI SDK will happily talk to ANY OpenAI-compatible
# server. LM Studio exposes one at /v1.
#
# api_key is required by the SDK but the local server ignores
# it — pass any non-empty string.
client = OpenAI(
    base_url=base_url,
    api_key="lm-studio",  # value doesn't matter for local server
)
print("\n✅ Client created.")


# ============================================================
# STEP 3: Send your first prompt
# ============================================================
prompt = "In 3 short bullets, what makes Python a great language for AI?"

print(f"\n🗣️  Prompt: {prompt}")
print("⏳ Asking the local model...\n")

try:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,   # 0 = focused, 1 = creative
        max_tokens=200,
    )

    answer = response.choices[0].message.content
    print("🤖 Response")
    print("-" * 40)
    print(answer)
    print("-" * 40)

    # Token usage (most local servers report this)
    usage = response.usage
    if usage:
        print(f"\n📊 Tokens — prompt: {usage.prompt_tokens}, "
              f"completion: {usage.completion_tokens}, "
              f"total: {usage.total_tokens}")

except Exception as e:
    print(f"❌ ERROR: {type(e).__name__}: {e}")
    print("\n🔧 Quick checks:")
    print("   • Is LM Studio open?")
    print("   • Is a model loaded in the Server tab?")
    print("   • Is the server started? (URL printed in LM Studio)")
    print("   • Does LOCAL_LLM_BASE_URL in .env match the server URL?")


# ============================================================
# STEP 4: Try a different temperature
# ============================================================
print("\n" + "=" * 60)
print("BONUS: Same prompt, two temperatures")
print("=" * 60)

creative_prompt = "Write a one-sentence motto for a Python + AI bootcamp."

for temp in (0.2, 1.0):
    print(f"\n🌡️  temperature={temp}")
    try:
        r = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": creative_prompt}],
            temperature=temp,
            max_tokens=80,
        )
        print(f"   → {r.choices[0].message.content.strip()}")
    except Exception as e:
        print(f"   (skipped: {e})")


print("\n" + "=" * 60)
print("🎯 KEY TAKEAWAYS")
print("=" * 60)
print("""
   1. The OpenAI SDK works with ANY OpenAI-compatible server.
   2. base_url + api_key is all that changes between local & cloud.
   3. messages = list of dicts (you saw this in Video 3!).
   4. temperature controls creativity (0 = boring, 1 = wild).
   5. response.choices[0].message.content has the answer.

🚀 Next: Video 7 — multi-turn chat with memory.
""")
