"""
qa_agent_short.py — Assignment 3 (Condensed)
A multi-skill QA agent (test plan / triage / summary / risk) on local LLM.
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
    "test_plan": "You are a Senior SDET. Output a markdown test plan with: Scope, Scenarios (title/type/steps/expected), Test data, Automation candidates.",
    "triage":    "You are a bug triage engineer. Output: severity + reason, owner area, duplicate likelihood, 3 clarifying questions.",
    "summary":   "You are an SDET. Output: traffic-light headline (green/amber/red), counts + pass rate, top 3 concerns, ship/hold/hotfix recommendation.",
    "risk":      "You are a release risk analyzer. Output a markdown table: Risk | Category | Likelihood | Impact | Mitigation. Use only prior context.",
}


class QAAgent:
    def __init__(self, client, model):
        self.client, self.model = client, model
        self.history = [{"role": "system",
                         "content": "You are a concise QA/SDET assistant with skills: "
                                    "test_plan, triage, summary, risk."}]
        self.skills_used = []

    def detect(self, msg):
        m = msg.lower()
        if any(k in m for k in ["test plan", "coverage for", "test cases for"]): return "test_plan"
        if any(k in m for k in ["bug:", "crash", "stack trace", "triage"]):       return "triage"
        if any(k in m for k in ["passed", "failed", "test run", "summarize"]):    return "summary"
        if any(k in m for k in ["risk", "release readiness", "go/no-go"]):        return "risk"
        return None

    def chat(self, msg):
        skill = self.detect(msg)
        if skill:
            print(f"   🔧 [{skill}]")
            self.skills_used.append(skill)
            messages = ([{"role": "system", "content": SKILL_PROMPTS[skill]}]
                        + self.history[1:][-6:]
                        + [{"role": "user", "content": msg}])
        else:
            messages = self.history + [{"role": "user", "content": msg}]

        r = self.client.chat.completions.create(
            model=self.model, messages=messages,
            temperature=0.3, max_tokens=700,
        )
        reply = r.choices[0].message.content
        self.history.append({"role": "user", "content": msg})
        self.history.append({"role": "assistant", "content": reply})
        return reply


agent = QAAgent(client, model)

for turn in [
    "Write a test plan for the new password reset flow on web.",
    "Bug: on iPhone 13 the login button is unresponsive when keyboard is open.",
    "Summarize this test run: 28 passed, 5 failed (login=2, cart=2, checkout=1), 2 skipped.",
    "Given everything above, what risks do you see for tomorrow's release?",
]:
    print(f"\n👤 {turn}\n🤖 {agent.chat(turn)}\n" + "─" * 60)
