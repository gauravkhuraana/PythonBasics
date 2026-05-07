"""
SOLUTION — Assignment 3: QA Agent
Multi-skill QA agent on local LLM. Reference implementation.
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


SKILL_PROMPTS = {
    "test_plan": """You are a Senior SDET writing a test plan.

Output markdown with these sections:
## Scope
What's covered and (briefly) what isn't.

## Scenarios
Numbered list. Each item:
- **Title** — one line
- **Type:** functional | negative | edge | performance | security
- **Steps:** short numbered list
- **Expected:** one line

## Test data
Bullets of required test data / fixtures / accounts.

## Automation candidates
Bullets, with rationale (stable / high-value / repeatable).

Be concrete. No filler.""",

    "triage": """You are a triage engineer for incoming bug reports.

Output markdown with these sections:
## Severity
Critical / High / Medium / Low + one-line reason.

## Owner area
A single component (auth, payments, ui-cart, mobile-ios, infra, ...).

## Duplicate likelihood
Low / Medium / High. If Medium or High, name what to search for.

## Clarifying questions
3 short questions for the reporter.""",

    "summary": """You are an SDET writing a release-status summary
from raw test-run data.

Output markdown:
## Headline
One line: ✅ green / ⚠️ amber / 🛑 red — plus the reason.

## Numbers
Pass / fail / skip counts and pass rate.

## Top concerns
Top 3 areas of concern. For each: module + 1-line cause + 1-line impact.

## Recommendation
Ship / hold / hotfix — one sentence justification.""",

    "risk": """You are a Release Risk Analyzer for QA.

Output a markdown table with columns:
| Risk | Category | Likelihood | Impact | Mitigation |

Category is one of: timeline / scope / quality / infra.
Likelihood and Impact are L / M / H.

Use ONLY information from the prior conversation context. Do not invent risks.""",
}


class QAAgent:
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

    def detect_skill(self, user_message):
        msg = user_message.lower()
        if any(kw in msg for kw in ["test plan", "coverage for",
                                     "test cases for", "test scenarios for"]):
            return "test_plan"
        if any(kw in msg for kw in ["bug:", "crash", "stack trace",
                                     "triage", "defect:"]):
            return "triage"
        if any(kw in msg for kw in ["passed", "failed", "test run",
                                     "summarize", "summarise"]):
            return "summary"
        if any(kw in msg for kw in ["risk", "release readiness", "go/no-go",
                                     "go-no-go"]):
            return "risk"
        return None

    def chat(self, user_message):
        skill = self.detect_skill(user_message)

        if skill:
            print(f"   🔧 [{skill}]")
            self.skills_used.append(skill)

            context = self.history[1:][-6:]   # last 6 turns, skip system
            messages = (
                [{"role": "system", "content": SKILL_PROMPTS[skill]}]
                + context
                + [{"role": "user", "content": user_message}]
            )
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.3,
                max_tokens=700,
            )
            reply = response.choices[0].message.content
        else:
            messages = self.history + [{"role": "user", "content": user_message}]
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.5,
                max_tokens=400,
            )
            reply = response.choices[0].message.content

        self.history.append({"role": "user", "content": user_message})
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def stats(self):
        total = len(self.history) - 1
        unique = sorted(set(self.skills_used))
        print("\n📊 Agent Stats")
        print(f"   Total messages: {total}")
        print(f"   Skills used:    {self.skills_used or '—'}")
        print(f"   Unique skills:  {len(unique)}/4 ({', '.join(unique) or '—'})")


if __name__ == "__main__":
    print("=" * 60)
    print("🧪 ASSIGNMENT 3 — SOLUTION")
    print("=" * 60)

    agent = QAAgent(client, model)
    print(f"\n✅ {agent.name} is ready!\n")

    turns = [
        "Write a test plan for the new password reset flow on web.",
        "Bug: on iPhone 13 the login button is unresponsive when keyboard is open.",
        "Summarize this test run: 28 passed, 5 failed (login=2, cart=2, checkout=1), 2 skipped.",
        "Given everything above, what risks do you see for tomorrow's release?",
    ]

    for t in turns:
        print(f"\n👤 You: {t}")
        print(f"\n🤖 Agent:\n{agent.chat(t)}\n")
        print("─" * 60)

    agent.stats()
