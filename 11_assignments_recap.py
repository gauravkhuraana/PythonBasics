"""
================================================================
11_assignments_recap.py — Key Patterns from All Assignments
================================================================

This file is a living cheatsheet. It shows the core code
pattern from each assignment side-by-side so you can see
how they build on each other.

Run this file:  python 11_assignments_recap.py
================================================================
"""

# ============================================================
# PATTERN 1 (Assignment 1) — Dict as a data model
# ============================================================

test_case = {
    "id":        "TC-001",
    "title":     "Login with valid credentials",
    "module":    "login",
    "priority":  "High",
    "status":    "pass",
    "automated": True,
}

catalog = [test_case]  # list of dicts — same shape as LLM message history

# Display
for tc in catalog:
    icon = "✅" if tc["status"] == "pass" else "❌"
    print(f"{icon} [{tc['id']}] {tc['title']} | {tc['module']} | {tc['priority']}")

# Filter
login_cases = [tc for tc in catalog if tc["module"] == "login"]

# Summarise
statuses    = [tc["status"] for tc in catalog]
pass_count  = statuses.count("pass")
fail_count  = statuses.count("fail")
print(f"\n📊 pass={pass_count}, fail={fail_count}")


# ============================================================
# PATTERN 2 (Assignment 2) — Secure config + LLM call
# ============================================================

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # reads .env into environment variables

client = OpenAI(
    base_url=os.getenv("LOCAL_LLM_BASE_URL", "http://localhost:1234/v1"),
    api_key="lm-studio",  # local server ignores this value
)
model = os.getenv("LOCAL_LLM_MODEL", "local-model")

# The four-line LLM call pattern (uncomment to run):
# system_prompt = "You are a QA engineer. Write a formal bug report."
# user_input    = "login crashes on iPhone when email has a + sign"
# response = client.chat.completions.create(
#     model=model,
#     messages=[
#         {"role": "system", "content": system_prompt},
#         {"role": "user",   "content": user_input},
#     ],
# )
# result = response.choices[0].message.content
# print(result)
# print(response.usage)   # always check token usage while developing


# ============================================================
# PATTERN 3 (Assignment 3) — Class-based agent with history
# ============================================================

class QAAgent:
    """A multi-skill QA agent that keeps conversation memory."""

    SKILLS = {
        "test_plan": "You are a senior QA engineer. Write a detailed, structured test plan.",
        "triage":    "You are a triage expert. Assess severity, affected area, and likely owner.",
        "summary":   "You are a test lead. Summarise the run results in a release-ready format.",
        "risk":      "You are a release manager. Identify the top quality risks for this release.",
    }

    def __init__(self, openai_client, model_name: str):
        self.client  = openai_client
        self.model   = model_name
        self.history = [
            {"role": "system", "content": "You are a helpful QA assistant."}
        ]

    def _detect_skill(self, text: str) -> str:
        t = text.lower()
        if any(w in t for w in ["test plan", "test cases", "scenarios"]):
            return "test_plan"
        if any(w in t for w in ["bug", "crash", "issue", "defect"]):
            return "triage"
        if any(w in t for w in ["passed", "failed", "skipped", "results"]):
            return "summary"
        if any(w in t for w in ["risk", "release", "ready", "quality"]):
            return "risk"
        return "general"

    def chat(self, user_message: str) -> str:
        skill = self._detect_skill(user_message)
        print(f"  🔧 [{skill}]")

        messages = self.history.copy()
        if skill in self.SKILLS:
            messages.insert(1, {"role": "system", "content": self.SKILLS[skill]})
        messages.append({"role": "user", "content": user_message})

        response = self.client.chat.completions.create(
            model=self.model, messages=messages
        )
        reply = response.choices[0].message.content

        # Keep running history for cross-turn memory
        self.history.append({"role": "user",      "content": user_message})
        self.history.append({"role": "assistant",  "content": reply})
        return reply


# ============================================================
# DEMO — Run the agent loop (uncomment to test)
# ============================================================

# agent = QAAgent(client, model)
# print("\n🤖 QA Agent ready. Type 'quit' to exit.\n")
# while True:
#     user_input = input("You: ").strip()
#     if user_input.lower() in {"quit", "exit", "q"}:
#         break
#     print(f"\nAgent: {agent.chat(user_input)}\n")

print("\n✅ Pattern file loaded — uncomment the demo sections to run each pattern.")
