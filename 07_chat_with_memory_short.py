"""
07_chat_with_memory_short.py — Demo version
Multi-turn chat against a local LLM (LM Studio).
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

messages = [
    {"role": "system", "content": "You are a SDET tutor."},
    {"role": "user",   "content": "What libraries can be used for UI Automation?"},
]

for follow_up in ["Show me the one which can do API Testing as well ",
                  "What was my first question?"]:
    r = client.chat.completions.create(model=model, messages=messages,
                                       max_tokens=200, temperature=0.4)
    reply = r.choices[0].message.content
    print(f"\n🤖 {reply}")
    messages.append({"role": "assistant", "content": reply})
    messages.append({"role": "user", "content": follow_up})
    print(f"\n👤 {follow_up}")

# final turn
r = client.chat.completions.create(model=model, messages=messages,
                                   max_tokens=200, temperature=0.4)
print(f"\n🤖 {r.choices[0].message.content}")
