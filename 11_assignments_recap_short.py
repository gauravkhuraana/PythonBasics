"""
11_assignments_recap_short.py — Core patterns at a glance
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# ----- PATTERN 1: Dict + list (Assignment 1) -----
catalog = [
    {"id": "TC-001", "title": "Login valid creds", "module": "login", "status": "pass"},
    {"id": "TC-002", "title": "Login invalid creds", "module": "login", "status": "fail"},
]
for tc in catalog:
    print(f"{'✅' if tc['status']=='pass' else '❌'} [{tc['id']}] {tc['title']}")

# ----- PATTERN 2: LLM call (Assignment 2) -----
client = OpenAI(
    base_url=os.getenv("LOCAL_LLM_BASE_URL", "http://localhost:1234/v1"),
    api_key="lm-studio",
)
model = os.getenv("LOCAL_LLM_MODEL", "local-model")

# response = client.chat.completions.create(
#     model=model,
#     messages=[
#         {"role": "system", "content": "You are a QA engineer. Write a formal bug report."},
#         {"role": "user",   "content": "login crashes on iPhone when email has a + sign"},
#     ],
# )
# print(response.choices[0].message.content)

# ----- PATTERN 3: Class agent (Assignment 3) -----
class QAAgent:
    SKILLS = {
        "test_plan": "You are a senior QA engineer. Write a structured test plan.",
        "triage":    "You are a triage expert. Assess severity and owner.",
        "summary":   "You are a test lead. Write a release-ready summary.",
        "risk":      "You are a release manager. Identify quality risks.",
    }

    def __init__(self, c, m):
        self.client  = c
        self.model   = m
        self.history = [{"role": "system", "content": "You are a QA assistant."}]

    def _skill(self, t):
        t = t.lower()
        if any(w in t for w in ["test plan", "test cases"]): return "test_plan"
        if any(w in t for w in ["bug", "crash", "defect"]):  return "triage"
        if any(w in t for w in ["passed", "failed", "run"]): return "summary"
        if any(w in t for w in ["risk", "release"]):         return "risk"
        return "general"

    def chat(self, msg):
        skill = self._skill(msg)
        msgs  = self.history.copy()
        if skill in self.SKILLS:
            msgs.insert(1, {"role": "system", "content": self.SKILLS[skill]})
        msgs.append({"role": "user", "content": msg})
        r = self.client.chat.completions.create(model=self.model, messages=msgs)
        reply = r.choices[0].message.content
        self.history += [{"role": "user", "content": msg}, {"role": "assistant", "content": reply}]
        return reply

print("\n✅ Short recap loaded. Uncomment the LLM call block to run live.")
