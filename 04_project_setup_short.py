"""
04_project_setup_short.py — Project Setup (Condensed)
Virtual environments, .env, .gitignore.
"""

# --- venv commands (run in terminal, not here) ---
# python -m venv venv
# .\venv\Scripts\Activate        # Windows
# source venv/bin/activate        # Mac/Linux
# pip install -r requirements.txt

# --- Loading config from .env ---
import os
from dotenv import load_dotenv

load_dotenv()

base_url   = os.getenv("LOCAL_LLM_BASE_URL")
model      = os.getenv("LOCAL_LLM_MODEL")
endpoint   = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

print("\nEnvironment health check\n")
for key, val, required in [
    ("LOCAL_LLM_BASE_URL", base_url, True),
    ("LOCAL_LLM_MODEL", model, True),
    ("AZURE_OPENAI_ENDPOINT", endpoint, False),
    ("AZURE_OPENAI_DEPLOYMENT_NAME", deployment, False),
]:
    if val:
        print(f"  [ok]   {key} is set")
    elif required:
        print(f"  [miss] {key} missing (needed for Videos 6-9)")
    else:
        print(f"  [skip] {key} not set (only needed for Video 10 bonus)")

print("\nNext: Video 5 (LM Studio), then python 06_first_local_ai_call_short.py")
