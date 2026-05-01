"""
================================================================
🧪 ASSIGNMENT 3 — HARD LEVEL
   Build a Multi-Skill QA Agent (uses your local LLM)
================================================================

⏱️  Estimated time: 30-45 minutes
🎯  Difficulty: ⭐⭐⭐ Hard

SCENARIO:
   You're the lone SDET on a small team and you want an AI
   pair that can switch hats: write a test plan one minute,
   triage a bug the next, summarize a test run, and call out
   release risks. Build a single agent class that detects
   WHICH skill the user is asking for and uses the right prompt.

   Skills:
   1. 📋 Test Plan Author     — Build a structured test plan
                                 from a feature description.
   2. 🐞 Bug Triager          — Suggest severity, owner area,
                                 and likely duplicates from a
                                 raw bug description.
   3. 📊 Test Run Summarizer  — Turn a list of test results
                                 into a clean release-ready
                                 status summary.
   4. ⚠️  Release Risk Analyzer— Identify quality risks for an
                                 upcoming release based on
                                 conversation context.

SKILLS TESTED (from Videos 3-9):
   ✅ Python classes and methods
   ✅ System prompts & role-based messages
   ✅ Multi-turn conversation with memory
   ✅ Building an agent architecture
   ✅ Skill / tool routing logic
   ✅ Prompt engineering for different tasks

Prerequisites:
   - Videos 1-9 complete
   - LM Studio running with a model loaded
   - .env has LOCAL_LLM_BASE_URL and LOCAL_LLM_MODEL

================================================================
📋 INSTRUCTIONS — Complete the TODOs below!
================================================================

Run when done:  python qa_agent.py

EXPECTED BEHAVIOR:
   The agent picks the right skill based on what you ask:

   You: "Write a test plan for the new password reset flow"
   Agent: 🔧 [test_plan]   → structured plan w/ scope, scenarios, data

   You: "Bug: app crashes on iPhone when email has a + sign"
   Agent: 🔧 [triage]      → severity, area, likely duplicates

   You: "Summarize: 12 passed, 3 failed (login,cart,checkout), 1 skipped"
   Agent: 🔧 [summary]     → release-ready status with red flags

   You: "What risks do you see for tomorrow's release?"
   Agent: 🔧 [risk]        → categorised risk register

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
print("🧪 ASSIGNMENT 3: Multi-Skill QA Agent")
print("=" * 60)


# ============================================================
# TASK 1: Define the skill prompts (5 points)
# ============================================================
# TODO: Flesh out each system prompt. Each one should clearly
#       say what role the AI plays, what to output, and the
#       format. Specificity beats word count.
# ============================================================

SKILL_PROMPTS = {
    "test_plan": """You are a Senior SDET writing test plans.
# TODO: complete this. Tell the model to output:
#   - Scope (what's covered + what isn't)
#   - Test scenarios as a numbered list, each with:
#       title, type (functional/negative/edge/perf/security),
#       steps, expected result
#   - Required test data
#   - Suggested automation candidates
#   - Use markdown.
""",

    "triage": """You are a triage engineer for incoming bug reports.
# TODO: complete this. The model should output:
#   - Suggested severity (Critical/High/Medium/Low) + 1-line reason
#   - Likely owner area (auth, payments, ui, infra, ...)
#   - Duplicate-likelihood (Low/Medium/High) + what to search for
#   - 3 clarifying questions to ask the reporter
""",

    "summary": """You are an SDET writing a release-status summary
from raw test-run data.
# TODO: complete this. Output:
#   - One-line headline (✅ green / ⚠️ amber / 🛑 red) with reason
#   - Pass/fail/skip counts and pass rate
#   - Top 3 areas of concern (which modules failed, why it matters)
#   - Recommendation: ship / hold / hotfix
""",

    "risk": """You are a Release Risk Analyzer for QA.
# TODO: complete this. Output a markdown table with columns:
#   Risk | Category (timeline/scope/quality/infra) | Likelihood (L/M/H)
#   | Impact (L/M/H) | Mitigation
# Use ONLY information from the prior conversation context.
""",
}


# ============================================================
# TASK 2: Build the QAAgent class (8 points)
# ============================================================
# Requirements:
#   - Has a base "manager" personality for general chat
#   - Maintains conversation history across turns (memory!)
#   - Detects which skill to use from the user's message
#   - Routes to the right skill prompt for specialized tasks
#
# HINT: Start from the LifeAssistant pattern in
#       08_life_assistant.py and ADD skill detection.
# ============================================================

class QAAgent:
    """A multi-skill QA Agent with conversation memory."""

    def __init__(self, client, model):
        self.client = client
        self.model = model
        self.name = "QA Agent"

        self.system_prompt = """You are an experienced QA / SDET assistant called "QA Agent".

You have several skills:
- When asked to plan tests / scope coverage / list scenarios → use test_plan
- When given a raw bug description that needs triaging      → use triage
- When given test-run results to summarize                  → use summary
- When asked about release / quality risks                  → use risk

For everything else (questions, brainstorming, follow-ups) respond
helpfully using your QA expertise. Be concise. Use bullets and tables.
Always remember the full conversation context."""

        self.history = [{"role": "system", "content": self.system_prompt}]
        self.skills_used = []

    # ------------------------------------------------------------
    def detect_skill(self, user_message):
        """Return one of: 'test_plan', 'triage', 'summary', 'risk', or None."""
        msg = user_message.lower()

        # TODO: Implement keyword-based skill detection (4 points)
        #
        # Examples:
        #   "test plan", "test cases for", "coverage for"  → "test_plan"
        #   "bug:", "crash", "stack trace", "triage"       → "triage"
        #   "passed", "failed", "test run", "summarize"    → "summary"
        #   "risk", "release readiness", "go/no-go"        → "risk"
        #
        # if any(kw in msg for kw in ["test plan", "coverage for", "test cases for"]):
        #     return "test_plan"
        # elif ...
        return None

    # ------------------------------------------------------------
    def chat(self, user_message):
        """Process a user turn: detect skill → call model → remember."""

        skill = self.detect_skill(user_message)

        if skill:
            print(f"   🔧 [{skill}]")
            self.skills_used.append(skill)

            # TODO: Build skill-specific messages.
            # Include the skill prompt as system, then the last
            # few turns of self.history (skip the original system
            # message), then this user message.
            #
            # context = [m for m in self.history[1:][-6:]]  # last 6 turns
            # skill_messages = (
            #     [{"role": "system", "content": SKILL_PROMPTS[skill]}]
            #     + context
            #     + [{"role": "user", "content": user_message}]
            # )
            #
            # response = self.client.chat.completions.create(
            #     model=self.model,
            #     messages=skill_messages,
            #     temperature=0.3,
            #     max_tokens=700,
            # )
            # reply = response.choices[0].message.content

            reply = "TODO: implement skill-based response"
        else:
            # General chat — use the regular history
            self.history.append({"role": "user", "content": user_message})
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.history,
                temperature=0.5,
                max_tokens=400,
            )
            reply = response.choices[0].message.content

            # remove the user msg we just appended; we'll re-append
            # below alongside the assistant reply for consistency
            self.history.pop()

        # TODO: Save BOTH user and assistant messages to history
        # self.history.append({"role": "user", "content": user_message})
        # self.history.append({"role": "assistant", "content": reply})

        return reply

    # ------------------------------------------------------------
    def stats(self):
        total = len(self.history) - 1  # exclude initial system prompt
        unique = sorted(set(self.skills_used))
        print("\n📊 Agent Stats")
        print(f"   Total messages: {total}")
        print(f"   Skills used:    {self.skills_used or '—'}")
        print(f"   Unique skills:  {len(unique)}/4 ({', '.join(unique) or '—'})")


# ============================================================
# TASK 3: Drive the agent through a realistic test (3 points)
# ============================================================
# TODO: Uncomment the test conversation below once you've
#       finished Tasks 1 and 2. Watch the [skill] tags fire.
# ============================================================

agent = QAAgent(client, model)
print(f"\n✅ {agent.name} is ready!\n")

# turns = [
#     "Write a test plan for the new password reset flow on web.",
#     "Bug: on iPhone 13 the login button is unresponsive when keyboard is open.",
#     "Summarize this test run: 28 passed, 5 failed (login=2, cart=2, checkout=1), 2 skipped.",
#     "Given everything above, what risks do you see for tomorrow's release?",
# ]
#
# for t in turns:
#     print(f"\n👤 You: {t}")
#     print(f"\n🤖 Agent:\n{agent.chat(t)}\n")
#     print("─" * 60)
#
# agent.stats()
