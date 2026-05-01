"""
06_first_local_ai_call_short.py — Demo version
First Python → Local LLM (LM Studio) call.
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

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "user", "content": "In 3 bullets: why is Python great for AI?"}
    ],
    temperature=0.7,
    max_tokens=200,
)

print(response.choices[0].message.content)
