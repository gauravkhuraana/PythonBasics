"""
================================================================
🧪 ASSIGNMENT 2 — MEDIUM LEVEL
   Build a Bug Report Generator (uses your local LLM)
================================================================

⏱️  Estimated time: 20-30 minutes
🎯  Difficulty: ⭐⭐ Medium

SCENARIO:
   Engineers and testers often capture bug context as a quick
   one-liner ("login crashes on iPhone with weird email") plus
   a few rough repro steps. Build a tool that turns those
   scrappy notes into a polished, consistent bug report that
   any developer can act on.

SKILLS TESTED (from Videos 3-7):
   ✅ Variables, lists, dictionaries
   ✅ Loading config with python-dotenv
   ✅ Creating an OpenAI-compatible client (LM Studio)
   ✅ Crafting system prompts
   ✅ Making chat completion calls
   ✅ Reading the response object

Prerequisites:
   - LM Studio running with a model loaded (Video 5)
   - .env has LOCAL_LLM_BASE_URL and LOCAL_LLM_MODEL
   - Virtual environment activated, requirements installed

================================================================
📋 INSTRUCTIONS — Complete the TODOs below!
================================================================

Run when done:  python bug_report_generator.py

EXPECTED OUTPUT (example):
   🐞 Generating bug report...
   ──────────────────────────
   ## Title
   [iOS][Auth] App crashes on login when email contains '+' alias

   ## Severity
   High

   ## Environment
   - iOS 17.4 / iPhone 13
   - App build 4.21.0

   ## Steps to Reproduce
   1. Open the app
   2. Tap "Sign in"
   3. Enter `gaurav+test@example.com` as email
   4. Enter the password and tap Login

   ## Expected
   User is signed in successfully.

   ## Actual
   App crashes immediately on tap.

   ## Suggested Severity / Notes
   Likely a regex issue in the email validator.
   ──────────────────────────
   📊 Tokens used: 412
================================================================
"""

import os
from dotenv import load_dotenv

# ============================================================
# TASK 1: Set up the local LLM client (3 points)
# ============================================================
# TODO: Import the OpenAI SDK, create the client pointed at
#       LM Studio's local server, and read the model name.
#
# HINT: Look at how 06_first_local_ai_call.py does it!
#   from openai import OpenAI
#   client = OpenAI(base_url=os.getenv("LOCAL_LLM_BASE_URL"),
#                   api_key="lm-studio")
#   model = os.getenv("LOCAL_LLM_MODEL")
# ============================================================

load_dotenv()

# TODO: import + client setup here

print("=" * 60)
print("🐞 ASSIGNMENT 2: Bug Report Generator")
print("=" * 60)


# ============================================================
# TASK 2: Define the bug inputs (2 points)
# ============================================================
# These are the rough notes a tester would jot down. The AI
# will turn them into a structured report.
# TODO: Tweak these to match a real bug you've seen. Add at
#       least one more repro step.
# ============================================================

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
    "Enter 'gaurav+test@example.com' as email",
    "Enter password and tap Login",
]
expected = "User is signed in successfully."
actual   = "App crashes immediately."

# TODO: add one more repro step above to confirm you've read the data


# ============================================================
# TASK 3: Craft a system prompt (4 points)
# ============================================================
# TODO: Write a system prompt that instructs the model to be
#       a senior QA engineer who writes excellent bug reports.
#
# Your prompt should mention:
#   - It is a senior QA / SDET writing for a developer audience
#   - The required output sections (Title, Severity, Environment,
#     Steps to Reproduce, Expected, Actual, Notes)
#   - Title format:  [Platform][Area] short imperative description
#   - Severity scale: Critical / High / Medium / Low
#   - Be specific, no fluff, use markdown headings
#
# HINT: Look at how system prompts are used in 07_chat_with_memory.py
# ============================================================

# TODO: Replace this with your real system prompt
system_prompt = "You are a helpful assistant."


# ============================================================
# TASK 4: Build the user message (3 points)
# ============================================================
# TODO: Combine all the bug inputs into one structured user
#       message the model can work from.
#
# HINT:
#   steps_text = "\n".join(f"{i}. {s}" for i, s in enumerate(repro_steps, 1))
#   env_text   = "\n".join(f"- {k}: {v}" for k, v in environment.items())
#   user_message = f\"\"\"Bug summary: {bug_summary}
#   Tester-suggested severity: {severity_hint}
#   ...
#   Steps:
#   {steps_text}
#   ...
#   \"\"\"
# ============================================================

# TODO: build user_message


# ============================================================
# TASK 5: Make the API call & print the report (4 points)
# ============================================================
# Steps:
#   1. messages = [system, user]
#   2. response = client.chat.completions.create(...)
#   3. Print response.choices[0].message.content
#   4. Print response.usage.total_tokens
#
# Use temperature=0.3 — bug reports should be consistent, not creative.
# ============================================================

# TODO: uncomment and complete
# print("\n🐞 Generating bug report...")
# print("─" * 40)
#
# response = client.chat.completions.create(
#     model=model,
#     messages=[
#         {"role": "system", "content": system_prompt},
#         {"role": "user",   "content": user_message},
#     ],
#     temperature=0.3,
#     max_tokens=600,
# )
#
# print(response.choices[0].message.content)
# print("─" * 40)
# if response.usage:
#     print(f"📊 Tokens used: {response.usage.total_tokens}")


# ============================================================
# BONUS TASK: Try multiple severity hints (3 points)
# ============================================================
# TODO: Loop through ["Low", "Medium", "High", "Critical"] as
#       severity_hint and regenerate the report. Compare how
#       (or whether) the model adjusts its tone and severity
#       choice. This is a great prompt-engineering exercise.
# ============================================================
