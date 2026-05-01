"""
================================================================
07_chat_with_memory.py
MULTI-TURN CHAT WITH MEMORY (against your local LLM)
================================================================

🎯 GOAL:
   Hold a conversation where the model REMEMBERS what was
   said earlier — using a system prompt + a growing message list.

This file covers:
  ✅ The three roles: system / user / assistant
  ✅ Why the LLM has no memory between API calls
  ✅ How YOU give it memory by sending the full history
  ✅ A practical "summarize my notes" example

Prerequisites:
  - LM Studio is running with a model loaded (Video 5)
  - .env has LOCAL_LLM_BASE_URL and LOCAL_LLM_MODEL

Run this file:  python 07_chat_with_memory.py
================================================================
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("LOCAL_LLM_BASE_URL", "http://localhost:1234/v1"),
    api_key="lm-studio",
)
model = os.getenv("LOCAL_LLM_MODEL", "local-model")

print("=" * 60)
print("MULTI-TURN CHAT WITH MEMORY")
print("=" * 60)


# ============================================================
# PART 1: The three message roles
# ============================================================
print("""
📝 THREE ROLES IN A CHAT MESSAGE LIST:

   1. "system"    — Instructions for the model (personality,
                    rules, output format). Sent once at the start.

   2. "user"      — What the human says.

   3. "assistant" — What the model said previously. Including
                    these is how you give the model "memory."
""")


# ============================================================
# PART 2: System prompt → personality
# ============================================================
system_prompt = """You are a friendly Python + AI tutor.
- Answer in 3-4 short bullets unless asked for more.
- Use plain English.
- Always end with one practical "try it now" suggestion."""

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "Hi! What's a list comprehension in Python?"},
]

print("⏳ First turn...\n")
r1 = client.chat.completions.create(
    model=model, messages=messages, max_tokens=250, temperature=0.4
)
reply1 = r1.choices[0].message.content
print(f"🤖 Tutor:\n{reply1}\n")


# ============================================================
# PART 3: Multi-turn — append, then resend EVERYTHING
# ============================================================
# The model is stateless. To make it "remember", we append its
# previous reply to our list and send the whole thing back.
messages.append({"role": "assistant", "content": reply1})
messages.append({"role": "user", "content": "Cool. Show me one that filters even numbers."})

print("⏳ Second turn (model remembers turn 1)...\n")
r2 = client.chat.completions.create(
    model=model, messages=messages, max_tokens=250, temperature=0.4
)
reply2 = r2.choices[0].message.content
print(f"🤖 Tutor:\n{reply2}\n")


# ============================================================
# PART 4: One more turn that REQUIRES memory
# ============================================================
messages.append({"role": "assistant", "content": reply2})
messages.append({"role": "user", "content": "What was my very first question?"})

print("⏳ Third turn (testing memory)...\n")
r3 = client.chat.completions.create(
    model=model, messages=messages, max_tokens=120, temperature=0.2
)
print(f"🤖 Tutor:\n{r3.choices[0].message.content}\n")

print(f"📊 Conversation length: {len(messages)} messages "
      f"({len(messages) - 1} excluding system).")


# ============================================================
# PART 5: A practical use — summarize a test run
# ============================================================
print("\n" + "-" * 40)
print("PRACTICAL: Summarize a test run")
print("-" * 40)

meeting_notes = """
Test run report — Release 4.21.0 — 2026-04-29
Suite: end-to-end regression
Results: 28 passed, 5 failed, 2 skipped (35 total)

Failures:
- login_with_plus_alias_email   (mobile-ios)     crash on tap Login
- login_with_plus_alias_email   (mobile-android) same crash
- cart_remove_last_item         (web)            UI shows ghost row after remove
- checkout_paypal_redirect      (web)            timeout after 30s
- profile_avatar_upload_large   (web)            413 from API

Skipped:
- search_voice_input            (no test data)
- referral_share_link           (feature-flagged off)
"""

summary_messages = [
    {"role": "system",
     "content": "You are an SDET. Reply with two sections: 'Headline' "
                "(1 line: green/amber/red + reason) and 'Top issues' "
                "(bullets with module + 1-line cause)."},
    {"role": "user",
     "content": f"Summarize this test run:\n\n{meeting_notes}"},
]

r = client.chat.completions.create(
    model=model, messages=summary_messages, max_tokens=400, temperature=0.3
)
print(r.choices[0].message.content)


print("\n" + "=" * 60)
print("🎯 KEY TAKEAWAYS")
print("=" * 60)
print("""
   • The model has NO memory between calls. You provide it.
   • Pattern: append the model's reply, append the next user
     message, send the full list again.
   • System prompt = behaviour. Set once, reuse across turns.
   • Lower temperature for "stick to the facts" tasks.

🚀 Next: Video 8 — wrap all this in a class and build a real
   personal Life Assistant.
""")
