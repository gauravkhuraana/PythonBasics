"""
defect_triage_assistant_short.py — Capstone (Condensed)
Interactive defect triage with cross-bug memory on local LLM.
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

SYSTEM = ("You are a senior triage SDET. For each bug, output markdown with: "
          "Severity (Critical/High/Medium/Low + reason), Owner area, "
          "Duplicate likelihood (reference prior BUG-N if any), "
          "2-3 clarifying questions, and suggested next step.")

history = [{"role": "system", "content": SYSTEM}]
seen = []

print("Paste a bug (one per line), 'quit' to exit.")
while True:
    raw = input("\n📝 > ").strip()
    if not raw or raw.lower() in {"quit", "exit", "q"}:
        break

    bug_id = f"BUG-{len(seen) + 1}"
    seen.append(bug_id)
    prior = ", ".join(seen[:-1]) or "(none)"
    history.append({"role": "user",
                    "content": f"New bug {bug_id}. Prior IDs: {prior}.\n{raw}"})
    r = client.chat.completions.create(
        model=model, messages=history, temperature=0.2, max_tokens=500,
    )
    reply = r.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    print(f"\n🤖 {bug_id}:\n{reply}")
