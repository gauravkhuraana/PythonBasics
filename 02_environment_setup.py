"""
================================================================
02_environment_setup.py
ENVIRONMENT SETUP: Virtual Environments, Secrets & .gitignore
================================================================

🎯 LAB GOAL REMINDER:
Building toward your AI Meeting Assistant!
Now let's set up the environment properly and securely.

This file covers:
  ✅ What is a Virtual Environment (venv)?
  ✅ How to use .env files for secrets
  ✅ Loading secrets with python-dotenv
  ✅ Why .gitignore matters
  ✅ Credential health check

Run this file: python 02_environment_setup.py
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

# Now retrieve your secrets safely
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

print("""
📝 CODE TO LOAD SECRETS:

   import os
   from dotenv import load_dotenv
   
   # Load the .env file
   load_dotenv()
   
   # Get values (returns None if not found)
   endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
   api_key = os.getenv("AZURE_OPENAI_API_KEY")
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

checks_passed = 0
total_checks = 3

# Check 1: Endpoint
if endpoint:
    print(f"   ✅ AZURE_OPENAI_ENDPOINT: Loaded")
    print(f"      Value: {endpoint[:30]}..." if len(str(endpoint)) > 30 else f"      Value: {endpoint}")
    checks_passed += 1
else:
    print(f"   ❌ AZURE_OPENAI_ENDPOINT: Not found!")
    print(f"      → Make sure you copied .env.example to .env")
    print(f"      → Fill in the URL provided by your instructor")

# Check 2: API Key
if api_key:
    # Only show first/last few characters for security
    masked_key = api_key[:4] + "..." + api_key[-4:] if len(api_key) > 8 else "***"
    print(f"\n   ✅ AZURE_OPENAI_API_KEY: Loaded")
    print(f"      Value: {masked_key} (masked for security)")
    checks_passed += 1
else:
    print(f"\n   ❌ AZURE_OPENAI_API_KEY: Not found!")
    print(f"      → Add your API key to the .env file")

# Check 3: Deployment Name
if deployment:
    print(f"\n   ✅ AZURE_OPENAI_DEPLOYMENT_NAME: Loaded")
    print(f"      Value: {deployment}")
    checks_passed += 1
else:
    print(f"\n   ❌ AZURE_OPENAI_DEPLOYMENT_NAME: Not found!")
    print(f"      → Add your deployment name (e.g., gpt-4o)")


# Summary
print("\n" + "-" * 40)
if checks_passed == total_checks:
    print(f"🎉 ALL CHECKS PASSED ({checks_passed}/{total_checks})")
    print("   You're ready for the Azure OpenAI examples!")
else:
    print(f"⚠️  {checks_passed}/{total_checks} checks passed")
    print("\n   TO FIX:")
    print("   1. Copy .env.example to .env")
    print("   2. Fill in credentials from your instructor")
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
print("✅ COMPLETE! Next: python 03_azure_openai_simple.py")
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
