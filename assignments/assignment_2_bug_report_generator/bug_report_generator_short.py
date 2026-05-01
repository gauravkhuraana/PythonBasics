"""
bug_report_generator_short.py — Assignment 2 (Condensed)
Turn rough bug notes into a polished bug report using your local LLM.
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

# --- bug inputs ---
bug_summary   = "App crashes on login when email contains a + alias on iOS"
severity_hint = "High"
environment   = {"platform": "iOS 17.4", "device": "iPhone 13", "build": "4.21.0"}
repro_steps   = [
    "Open the app",
    "Tap Sign in",
    "Enter gaurav+test@example.com as email",
    "Enter password and tap Login",
]
expected = "User is signed in."
actual   = "App crashes immediately."

# --- TODO: write a strong system prompt for a senior QA engineer ---
system_prompt = (
    "You are a senior QA engineer who writes crisp bug reports for developers. "
    "Output markdown with sections: Title, Severity, Environment, "
    "Steps to Reproduce, Expected, Actual, Notes. "
    "Title format: [Platform][Area] short imperative description."
)

steps_text = "\n".join(f"{i}. {s}" for i, s in enumerate(repro_steps, 1))
env_text   = "\n".join(f"- {k}: {v}" for k, v in environment.items())

user_message = f"""Bug summary: {bug_summary}
Tester-suggested severity: {severity_hint}

Environment:
{env_text}

Steps to reproduce:
{steps_text}

Expected: {expected}
Actual:   {actual}
"""

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user",   "content": user_message},
    ],
    temperature=0.3,
    max_tokens=600,
)

print(response.choices[0].message.content)
