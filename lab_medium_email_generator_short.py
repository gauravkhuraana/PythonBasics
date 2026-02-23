"""
lab_medium_email_generator_short.py - Email Draft Generator Lab (Condensed)
Uses Azure OpenAI to generate emails from parameters.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# TASK 1: Set up the Azure OpenAI client
# TODO: Uncomment and complete
# from openai import AzureOpenAI
# from azure.identity import DefaultAzureCredential, get_bearer_token_provider
#
# credential = DefaultAzureCredential()
# token_provider = get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")
#
# client = AzureOpenAI(
#     azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
#     azure_ad_token_provider=token_provider,
#     api_version="2024-12-01-preview"
# )
# deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

print("🧪 LAB: Email Draft Generator\n")

# TASK 2: Email parameters
recipient = "Sarah"
purpose = "Follow up after project kickoff meeting"
tone = "professional"
key_points = [
    "Thank her for attending the meeting",
    "Recap the 3 main decisions we made",
    "Remind about the next meeting on Friday"
]

# TASK 3: Write a system prompt
# TODO: Replace with a proper email assistant prompt
system_prompt = "You are a helpful assistant."

# TASK 4: Build the user message
# TODO: Combine parameters into a prompt
# points_text = "\n".join(f"- {point}" for point in key_points)
# user_message = f"""Write an email to {recipient} about {purpose}.
# Tone: {tone}
# Key points:
# {points_text}"""

# TASK 5: Make the API call
# TODO: Uncomment when ready
# messages = [
#     {"role": "system", "content": system_prompt},
#     {"role": "user", "content": user_message}
# ]
#
# response = client.chat.completions.create(
#     model=deployment,
#     messages=messages,
#     max_completion_tokens=400
# )
#
# print("📧 Email Draft:")
# print(response.choices[0].message.content)
# print(f"\n📊 Tokens used: {response.usage.total_tokens}")
