"""
SOLUTION — Capstone: Defect Triage Assistant
Interactive triage with cross-bug memory. Reference implementation.
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


SYSTEM_PROMPT = """You are "Triage Assistant" — a senior SDET on bug-triage rotation.

For every bug the user pastes, output **markdown** with EXACTLY these sections:

## Severity
Critical / High / Medium / Low + one short justification.

## Owner area
A single component name (auth, payments, mobile-ios, infra, ui-cart, ...).

## Duplicate likelihood
Low / Medium / High. If Medium or High, reference the BUG-N IDs you suspect.

## Clarifying questions
2-3 short questions, OR "None — report is complete." if info is sufficient.

## Suggested next step
One sentence: assign / merge / request-info / hotfix / schedule.

Rules: be concise, use only conversation context, no invented detail.
If the user just chats (not a bug), respond as a friendly QA peer.
"""


class TriageAssistant:
    def __init__(self, client, model):
        self.client = client
        self.model = model
        self.history = [{"role": "system", "content": SYSTEM_PROMPT}]
        self.bugs_seen = []

    def add_bug(self, raw_text):
        bug_id = f"BUG-{len(self.bugs_seen) + 1}"
        self.bugs_seen.append({"id": bug_id, "text": raw_text})

        prior_ids = ", ".join(b["id"] for b in self.bugs_seen[:-1]) or "(none yet)"
        user_msg = (
            f"New bug to triage — ID {bug_id}.\n"
            f"Previously seen IDs: {prior_ids}.\n\n"
            f"Raw report:\n{raw_text}"
        )

        self.history.append({"role": "user", "content": user_msg})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.history,
            temperature=0.2,
            max_tokens=500,
        )
        reply = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": reply})
        return bug_id, reply

    def chat(self, msg):
        self.history.append({"role": "user", "content": msg})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.history,
            temperature=0.5,
            max_tokens=400,
        )
        reply = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": reply})
        return reply


def main():
    print("═" * 60)
    print("   🐞 DEFECT TRIAGE ASSISTANT — SOLUTION")
    print("   Paste a bug, 'list', 'chat <text>', or 'quit'.")
    print("═" * 60)

    agent = TriageAssistant(client, model)

    while True:
        try:
            raw = input("\n📝 Bug / command > ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not raw:
            continue

        cmd = raw.lower()
        if cmd in {"quit", "exit", "q"}:
            break

        if cmd == "list":
            if not agent.bugs_seen:
                print("   (no bugs yet)")
                continue
            for b in agent.bugs_seen:
                preview = b["text"].splitlines()[0][:80]
                print(f"   {b['id']}: {preview}")
            continue

        if cmd.startswith("chat "):
            print(f"\n🤖 {agent.chat(raw[5:].strip())}")
            continue

        try:
            bug_id, reply = agent.add_bug(raw)
        except Exception as e:
            print(f"\n❌ {type(e).__name__}: {e}")
            print("   (Is LM Studio still running?)")
            continue

        print(f"\n🤖 Triage for {bug_id}:\n{reply}")

    print("\n" + "═" * 60)
    print(f"📊 Session done. Triaged {len(agent.bugs_seen)} bug(s).")
    print("═" * 60)


if __name__ == "__main__":
    main()
