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
or_key     = os.getenv("OPENROUTER_API_KEY")
or_model   = os.getenv("OPENROUTER_MODEL")

print("\nEnvironment health check\n")
for key, val, required in [
    ("LOCAL_LLM_BASE_URL", base_url, True),
    ("LOCAL_LLM_MODEL", model, True),
    ("OPENROUTER_API_KEY", or_key, False),
    ("OPENROUTER_MODEL", or_model, False),
]:
    if val:
        print(f"  [ok]   {key} is set")
    elif required:
        print(f"  [miss] {key} missing (needed for Videos 6-10)")
    else:
        print(f"  [skip] {key} not set (only needed for OpenRouter in Video 8)")

print("\nNext: Video 5 (LM Studio), then python 06_first_local_ai_call_short.py")
