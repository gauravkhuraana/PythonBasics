import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
print(f"Endpoint: {endpoint}")
print(f"Deployment: {deployment}")

try:
    credential = DefaultAzureCredential()
    token_provider = get_bearer_token_provider(
        credential, "https://cognitiveservices.azure.com/.default"
    )
    client = AzureOpenAI(
        azure_endpoint=endpoint,
        azure_ad_token_provider=token_provider,
        api_version="2024-12-01-preview"
    )
    response = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": "Say hello"}],
        max_completion_tokens=10
    )
    print("SUCCESS:", response.choices[0].message.content)
except Exception as e:
    print(f"ERROR: {type(e).__name__}: {e}")
