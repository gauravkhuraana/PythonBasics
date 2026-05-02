import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

model = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "user", "content": "In 3 bullets: why is Python great for AI?"}
    ],
    temperature=0.7,
    max_tokens=200,
)

print(response.choices[0].message.content)