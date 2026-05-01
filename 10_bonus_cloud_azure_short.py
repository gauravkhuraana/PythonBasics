"""
03_azure_openai_simple_short.py - First Azure OpenAI API Call (Condensed)
"""

import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# Load credentials
load_dotenv()
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

if not all([endpoint, deployment]):
    print("❌ Missing credentials! Check your .env file.")
    exit(1)

# Create Azure OpenAI client (using Azure AD auth)
credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(
    credential, "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
    api_version="2024-12-01-preview",
    #api_key=os.getenv("AZURE_OPENAI_API_KEY")  # Optional if using Azure AD auth
)

# Make API call
prompt = "What are 3 tips for running effective meetings? "
print(f"🗣️  Prompt: \"{prompt}\"\n")

try:
    response_object = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": prompt}],
        max_completion_tokens=200,
    )

    # Get the response
    response = response_object.choices[0].message.content
    print("🤖 Response:")
    print(response)

    # Token usage
    print(f"\n📊 Tokens — prompt: {response_object.usage.prompt_tokens}, "
          f"completion: {response_object.usage.completion_tokens}, "
          f"total: {response_object.usage.total_tokens}")
    

except Exception as e:
    print(f"❌ {type(e).__name__}: {e}")

print("\n✅ Next: python 04_azure_openai_chat_short.py")
