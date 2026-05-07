"""
SOLUTION — Assignment 2: Bug Report Generator
Uses local LLM via LM Studio. Reference implementation.
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


# Bug inputs
bug_summary = "App crashes on login when email contains a + alias on iOS"
severity_hint = "High"
environment = {
    "platform": "iOS 17.4",
    "device":   "iPhone 13",
    "build":    "4.21.0",
}
repro_steps = [
    "Open the app",
    "Tap 'Sign in'",
    "Enter 'gaurav+test@example.com' as the email",
    "Enter the password",
    "Tap Login",
]
expected = "User is signed in successfully."
actual   = "App crashes immediately on tap."


# System prompt
system_prompt = """You are a senior QA / SDET engineer who writes excellent
bug reports for a developer audience.

Output the report as **markdown** with EXACTLY these sections, in this order:

## Title
Format: [Platform][Area] short imperative description (max 12 words).

## Severity
One of: Critical / High / Medium / Low. Use the tester's hint as a starting
point, but adjust if the symptoms warrant it. Add a one-line justification.

## Environment
Bullet list of the relevant environment data.

## Steps to Reproduce
Numbered list. Each step is one short sentence in the imperative.

## Expected
One sentence.

## Actual
One sentence.

## Notes
Optional. Hypotheses about cause, affected versions, related areas.

Rules:
- Be specific. No fluff. No filler phrases.
- Do NOT invent details that aren't in the input.
"""


def build_user_message():
    steps = "\n".join(f"{i}. {s}" for i, s in enumerate(repro_steps, 1))
    env = "\n".join(f"- {k}: {v}" for k, v in environment.items())
    return f"""Bug summary: {bug_summary}
Tester-suggested severity: {severity_hint}

Environment:
{env}

Steps to reproduce:
{steps}

Expected: {expected}
Actual:   {actual}
"""


def generate_report(severity_hint_override=None):
    hint = severity_hint_override or severity_hint
    user_message = build_user_message().replace(
        f"Tester-suggested severity: {severity_hint}",
        f"Tester-suggested severity: {hint}",
    )
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_message},
        ],
        temperature=0.3,
        max_tokens=600,
    )
    return response.choices[0].message.content, response.usage


if __name__ == "__main__":
    print("=" * 60)
    print("🐞 ASSIGNMENT 2 — SOLUTION")
    print("=" * 60)
    print("\n🐞 Generating bug report...")
    print("─" * 40)

    report, usage = generate_report()
    print(report)
    print("─" * 40)
    if usage:
        print(f"📊 Tokens used: {usage.total_tokens}")

    # Bonus: severity sweep — see how the model reacts to different hints
    print("\n" + "=" * 60)
    print("🎁 BONUS: severity-hint sweep")
    print("=" * 60)
    for hint in ["Low", "Medium", "High", "Critical"]:
        print(f"\n--- hint = {hint} ---")
        report, _ = generate_report(severity_hint_override=hint)
        # Pull and print only the Severity section
        lines = report.splitlines()
        for i, line in enumerate(lines):
            if line.strip().lower().startswith("## severity"):
                # Print the heading and the next non-blank line
                print(line)
                for nxt in lines[i + 1:]:
                    if nxt.strip():
                        print(f"  → {nxt.strip()}")
                        break
                break
