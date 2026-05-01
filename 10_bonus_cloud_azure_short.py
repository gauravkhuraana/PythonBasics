"""
10_bonus_cloud_azure_short.py — Demo version
The same first-call prompt as Video 6, but against Azure OpenAI.
"""

import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

load_dotenv()

credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(
    credential, "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_ad_token_provider=token_provider,
    api_version="2024-12-01-preview",
)

response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    messages=[{"role": "user",
               "content": "In 3 bullets, why is Python great for AI?"}],
    max_completion_tokens=200,
    temperature=0.7,
)

print(response.choices[0].message.content)
