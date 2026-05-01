"""
05_meeting_assistant_agent_short.py - AI Personal Assistant Agent (Condensed)
Agent class with built-in conversation memory
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
    azure_ad_token_provider=token_provider,
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")


# --- The Agent class: handles memory automatically ---
class PersonalAssistant:
    def __init__(self, client, deployment, system_prompt):
        self.client = client
        self.deployment = deployment
        self.history = [
            {"role": "system", "content": system_prompt}
        ]

    def chat(self, user_message):
        self.history.append({"role": "user", "content": user_message})

        response_object = self.client.chat.completions.create(
            model=self.deployment,
            messages=self.history,
            max_completion_tokens=500
        )

        response = response_object.choices[0].message.content
        self.history.append({"role": "assistant", "content": response})
        return response


# --- Interactive conversation ---
print("Enter a system prompt (defines the AI's role/personality):")
system_prompt = input("📝 System Prompt: ")

agent = PersonalAssistant(client, deployment, system_prompt)
print("\n--- Personal Assistant (type 'quit' to stop) ---\n")

while True:
    user_input = input("👤 You: ")
    if user_input.lower() == "quit":
        break

    response = agent.chat(user_input)
    print(f"🤖 Assistant: {response}\n")

print(f"\n📊 Messages in memory: {len(agent.history) - 1}")
print("   Agent remembered everything — no manual history management!")

print("\n✅ Session complete!")
