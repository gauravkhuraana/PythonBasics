"""
02_environment_setup_short.py - Environment Setup (Condensed)
Virtual Environments, Secrets & .gitignore
"""

# --- venv commands (run in terminal, not here) ---
# python -m venv venv
# .\venv\Scripts\Activate        # Windows
# source venv/bin/activate        # Mac/Linux
# pip install -r requirements.txt

# --- Loading secrets from .env ---
import os
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
url = os.getenv("AZURE_OPENAI_URL")


# --- Credential health check ---
print("\n🔍 Checking environment setup...\n")

checks = {
    "AZURE_OPENAI_ENDPOINT": endpoint,
    "AZURE_OPENAI_API_KEY": api_key,
    "AZURE_OPENAI_DEPLOYMENT_NAME": deployment,
    "AZURE_OPENAI_URL": url,
}

def check_env(key, value):
    if value:
        print(f"  ✅ {key} is set")
    else:
        print(f"  ❌ {key} is missing — check your .env file")


for key, value in checks.items():
    check_env(key, value)

print("\n✅ Next: python 03_azure_openai_simple.py")
