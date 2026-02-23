"""
04_azure_openai_chat_short.py - Chat with Message History (Condensed)
System prompts, roles, multi-turn conversations
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
    api_version="2024-12-01-preview"
)
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

# --- System prompt sets AI personality ---
print("Enter a system prompt (defines the AI's role/personality):")
system_prompt = input("📝 System Prompt: ")

conversation = [{"role": "system", "content": system_prompt}]

print("\n--- Multi-Turn Conversation (type 'quit' to stop) ---\n")

while True:
    user_input = input("👤 You: ")
    if user_input.lower() == "quit":
        break

    conversation.append({"role": "user", "content": user_input})

    response_object = client.chat.completions.create(model=deployment, messages=conversation, max_completion_tokens=500)
    response = response_object.choices[0].message.content
    print(f"🤖 Assistant: {response}\n")

    conversation.append({"role": "assistant", "content": response})

print(f"\n📊 Conversation length: {len(conversation)} messages")
print("   Key: AI has NO memory — we send full history each time!")

