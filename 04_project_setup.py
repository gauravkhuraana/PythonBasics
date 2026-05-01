"""
================================================================
04_project_setup.py — Video 4
PRO PROJECT SETUP: venv, requirements, .env, .gitignore
================================================================

🎯 GOAL:
   Set the project up the way real Python+AI projects are
   structured — so secrets stay out of git and packages stay
   isolated to this project.

This file covers:
  ✅ What a virtual environment (venv) is and why
  ✅ Storing config in a .env file
  ✅ Loading config with python-dotenv
  ✅ Why .gitignore matters
  ✅ A health check for the variables Video 6 will need

Run this file:  python 04_project_setup.py
================================================================
"""

print("=" * 60)
print("PART 1: VIRTUAL ENVIRONMENT (venv)")
print("=" * 60)

print("""
📦 WHAT IS A VIRTUAL ENVIRONMENT?

Think of it as a "container" for your project's packages:

   Your Computer
   ├── Project A (venv) → openai 1.0, pandas 2.0
   ├── Project B (venv) → openai 0.28, pandas 1.5
   └── Project C (venv) → Different packages entirely

WHY USE IT?
   ✅ Each project has its own packages (no conflicts!)
   ✅ Easy to share: just share requirements.txt
   ✅ Clean uninstall: delete the venv folder
   ✅ Matches production environments

COMMANDS TO REMEMBER:
   
   # Create virtual environment (do this ONCE per project)
   python -m venv venv
   
   # Activate it (do this EVERY TIME you open terminal)
   .\\venv\\Scripts\\Activate     # Windows PowerShell
   source venv/bin/activate      # Mac/Linux
   
   # You'll see (venv) at the start of your prompt when active!
   
   # Install packages
   pip install -r requirements.txt
   
   # Deactivate when done
   deactivate
""")


print("=" * 60)
print("PART 2: SECRETS WITH .env FILES")
print("=" * 60)

print("""
🔐 WHY USE .env FILES?

NEVER put secrets directly in your code!

   ❌ BAD (secret in code - anyone can see it!):
   api_key = "sk-abc123secretkey456"
   
   ✅ GOOD (secret in .env file):
   api_key = os.getenv("AZURE_OPENAI_API_KEY")

HOW IT WORKS:
   1. Create a file named: .env (just ".env", no other name)
   2. Add your secrets as KEY=VALUE pairs
   3. Use python-dotenv to load them
   4. Access with os.getenv("KEY_NAME")

YOUR .env FILE SHOULD LOOK LIKE:
   
   AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
   AZURE_OPENAI_API_KEY=your-secret-key-here
   AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
""")


print("=" * 60)
print("PART 3: LOADING SECRETS IN PYTHON")
print("=" * 60)

# ============================================================
# This is how you load secrets from .env
# ============================================================

import os
from dotenv import load_dotenv

# Load environment variables from .env file
# This reads your .env file and makes values available
load_dotenv()

# Now retrieve your config safely.
# For Videos 6-9 we use the LOCAL_* variables (LM Studio).
# AZURE_* are only needed for the bonus Video 10.
base_url = os.getenv("LOCAL_LLM_BASE_URL")
model    = os.getenv("LOCAL_LLM_MODEL")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

print("""
📝 CODE TO LOAD CONFIG:

   import os
   from dotenv import load_dotenv

   load_dotenv()

   # Local LLM (LM Studio) — main path for this course
   base_url = os.getenv("LOCAL_LLM_BASE_URL")
   model    = os.getenv("LOCAL_LLM_MODEL")

   # Azure OpenAI — only used in the Video 10 bonus
   endpoint   = os.getenv("AZURE_OPENAI_ENDPOINT")
   deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
""")


print("=" * 60)
print("PART 4: WHY .gitignore MATTERS")
print("=" * 60)

print("""
🛡️  .gitignore PROTECTS YOUR SECRETS

When you use Git, .gitignore tells it which files to IGNORE.

YOUR .gitignore SHOULD INCLUDE:

   # Secrets - NEVER commit!
   .env
   
   # Virtual environment - each dev creates their own
   venv/
   
   # Python cache - auto-generated junk
   __pycache__/
   *.pyc

WHAT HAPPENS WITHOUT .gitignore?
   
   ❌ You accidentally commit .env
   ❌ Your API key is now PUBLIC on GitHub
   ❌ Hackers find it within minutes (they scan for this!)
   ❌ Your Azure bill goes through the roof 💸

ALWAYS CHECK before committing:
   git status  # Make sure .env is NOT listed!
""")


print("=" * 60)
print("PART 5: CREDENTIAL HEALTH CHECK")
print("=" * 60)

# ============================================================
# Let's verify your setup is correct!
# ============================================================

print("\n🔍 Checking your environment setup...\n")

print("   --- Local LLM (required for Videos 6-9) ---")
local_ok = True
if base_url:
    print(f"   ✅ LOCAL_LLM_BASE_URL: {base_url}")
else:
    print("   ❌ LOCAL_LLM_BASE_URL not set (default http://localhost:1234/v1 will be used)")
    local_ok = False
if model:
    print(f"   ✅ LOCAL_LLM_MODEL: {model}")
else:
    print("   ❌ LOCAL_LLM_MODEL not set — see Video 5 for where to find it")
    local_ok = False

print("\n   --- Azure OpenAI (only for Video 10 bonus) ---")
for name, val in (("AZURE_OPENAI_ENDPOINT", endpoint),
                  ("AZURE_OPENAI_API_KEY", api_key),
                  ("AZURE_OPENAI_DEPLOYMENT_NAME", deployment)):
    if val:
        masked = val[:6] + "…" if name == "AZURE_OPENAI_API_KEY" and len(val) > 6 else val
        print(f"   ✅ {name}: {masked}")
    else:
        print(f"   ⚪ {name}: not set (skip if you're not doing Video 10)")

print("\n" + "-" * 40)
if local_ok:
    print("🎉 Local LLM config looks good — you're ready for Video 6!")
else:
    print("⚠️  Local LLM config incomplete.")
    print("   1. Copy .env.example to .env")
    print("   2. Fill in LOCAL_LLM_BASE_URL and LOCAL_LLM_MODEL (see Video 5)")
    print("   3. Run this file again")


print("\n" + "=" * 60)
print("🎯 KEY TAKEAWAYS")
print("=" * 60)
print("""
   1. venv = Isolated package environment per project
   2. .env = Store secrets as KEY=VALUE pairs
   3. load_dotenv() = Load .env into your Python code
   4. os.getenv("KEY") = Retrieve secret values
   5. .gitignore = Prevent .env from being committed
   
   🔐 GOLDEN RULE: Never hardcode secrets in your code!
""")


print("=" * 60)
print("✅ COMPLETE! Next: Video 5 (LM Studio walkthrough), then 06_first_local_ai_call.py")
print("=" * 60)


# ============================================================
# 🧪 TRY IT YOURSELF!
# ============================================================
# Add a custom environment variable to your .env file:
#
# MY_NAME=YourNameHere
#
# Then uncomment below to read it:

# my_name = os.getenv("MY_NAME")
# print(f"\nHello, {my_name}! Your custom variable works!")
