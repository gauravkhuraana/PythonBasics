"""
================================================================
10_bonus_cloud_azure.py
BONUS: Connect to Azure OpenAI — same code, different client
================================================================

🎯 GOAL:
   Show that going from local to cloud is a 2-line change:
     1. Use AzureOpenAI() instead of OpenAI()
     2. Pass endpoint + auth instead of base_url + dummy key

Everything else (messages, response parsing) is identical to
Video 6's local example.

Prerequisites:
  - An Azure OpenAI resource + a deployment (e.g., gpt-4o)
  - .env has AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_DEPLOYMENT_NAME
  - Run `az login` first (we use Azure AD auth — no API key in code)

Run this file:  python 10_bonus_cloud_azure.py
================================================================
"""

import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

load_dotenv()

endpoint   = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

if not all([endpoint, deployment]):
    print("❌ Missing AZURE_OPENAI_ENDPOINT or AZURE_OPENAI_DEPLOYMENT_NAME in .env")
    raise SystemExit(1)

# Azure AD auth — no API key in code or .env.
# (You can also use api_key=... if your org allows key-based auth.)
credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(
    credential, "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
    api_version="2024-12-01-preview",
)

print("=" * 60)
print("BONUS: Same prompt, but in the cloud (Azure OpenAI)")
print("=" * 60)
print(f"\n📡 Endpoint:   {endpoint}")
print(f"🤖 Deployment: {deployment}")

prompt = "In 3 short bullets, what makes Python a great language for AI?"
print(f"\n🗣️  Prompt: {prompt}")
print("⏳ Calling Azure OpenAI...\n")

response = client.chat.completions.create(
    model=deployment,  # for AzureOpenAI, "model" = your deployment name
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=200,
    temperature=0.7,
)

print("🤖 Response")
print("-" * 40)
print(response.choices[0].message.content)
print("-" * 40)

usage = response.usage
if usage:
    print(f"\n📊 Tokens — prompt: {usage.prompt_tokens}, "
          f"completion: {usage.completion_tokens}, "
          f"total: {usage.total_tokens}")

print("""
🎯 KEY TAKEAWAY
   The only meaningful difference vs Video 6 is the client setup.
   Once you have a `client`, the rest of the OpenAI SDK API is
   the same — which is why the apps you built in Videos 7 & 8
   can be ported to the cloud by swapping the constructor.

🚀 Wrap-up next: Video 11.
""")
