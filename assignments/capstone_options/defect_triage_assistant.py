"""
================================================================
🏆 CAPSTONE OPTION — Defect Triage Assistant
   A persistent, conversational triage buddy on your local LLM
================================================================

WHO THIS IS FOR:
   SDETs, QA leads, or developers swamped by raw bug reports
   who want an AI that consistently asks the right questions
   and assigns severity, owner area, and dup-likelihood —
   while remembering every bug it has seen this session.

WHAT IT DOES:
   • Loops over incoming raw bug texts.
   • For each one, returns a structured triage decision:
       - Severity (Critical / High / Medium / Low) + reason
       - Likely owner area
       - Duplicate-likelihood + which earlier bug(s) it might dupe
       - 2-3 clarifying questions if info is thin
   • Maintains memory of all bugs seen this session, so it can
     spot duplicates across the conversation.

This is the ⭐⭐⭐ capstone version of Assignment 3's "triage"
skill — same idea, but a real interactive loop with persistent
memory and dup-detection across the session.

Run this file:  python defect_triage_assistant.py
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


SYSTEM_PROMPT = """You are "Triage Assistant" — a senior SDET on bug-triage rotation.

For every bug the user pastes, output **markdown** with EXACTLY these sections:

## Severity
One of: Critical / High / Medium / Low — followed by one short sentence justifying it.

## Owner area
A single component name (e.g., auth, payments, mobile-ios, infra, ui-cart).

## Duplicate likelihood
Low / Medium / High. If Medium or High, reference the bug ID(s) you suspect
it duplicates (e.g., "possibly duplicates BUG-3 — same crash on +alias email").

## Clarifying questions
2-3 short questions you would ask the reporter, only if information is thin.
If the report is already complete, write: "None — report is complete."

## Suggested next step
One sentence: assign / merge / request-info / hotfix / schedule.

Rules:
- Be concise. No fluff.
- Use ONLY information from the conversation so far.
- If the user just chats (not a bug), respond normally as a friendly QA peer.
"""


class TriageAssistant:
    """Conversational triage with cross-bug memory."""

    def __init__(self, client, model):
        self.client = client
        self.model = model
        self.history = [{"role": "system", "content": SYSTEM_PROMPT}]
        self.bugs_seen = []   # list of {"id": "BUG-1", "text": "..."}

    def add_bug(self, raw_text):
        """Record a new bug under a sequential ID and ask the model to triage."""
        bug_id = f"BUG-{len(self.bugs_seen) + 1}"
        self.bugs_seen.append({"id": bug_id, "text": raw_text})

        # Tell the model the new bug + remind it of previously-seen IDs
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
            temperature=0.2,   # triage should be consistent
            max_tokens=500,
        )
        reply = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": reply})
        return bug_id, reply

    def chat(self, msg):
        """General conversation (not a bug)."""
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


# ============================================================
# Interactive loop
# ============================================================
def main():
    print("═" * 60)
    print("   🐞 DEFECT TRIAGE ASSISTANT")
    print("   Paste a bug, type 'list' to see seen bugs,")
    print("   'chat <text>' to ask a non-bug question, 'quit' to exit.")
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

    # Wrap-up
    print("\n" + "═" * 60)
    print(f"📊 Session done. Triaged {len(agent.bugs_seen)} bug(s).")
    print("═" * 60)


if __name__ == "__main__":
    main()
