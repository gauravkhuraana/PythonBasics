"""
================================================================
🧪 LAB ASSIGNMENT 2 — MEDIUM LEVEL
   Build an Email Draft Generator (Azure OpenAI API)
================================================================

⏱️  Estimated time: 20-30 minutes
🎯  Difficulty: ⭐⭐ Medium (Uses Azure OpenAI API)

SCENARIO:
   You're a busy professional who needs to write emails quickly.
   Build a tool that takes basic inputs (recipient, purpose, tone)
   and uses Azure OpenAI to generate a polished email draft.

SKILLS TESTED (from Files 01-04):
   ✅ Variables, lists, dictionaries
   ✅ Loading credentials with dotenv
   ✅ Creating the Azure OpenAI client
   ✅ Crafting system prompts
   ✅ Making API calls with messages
   ✅ Working with the response object

Prerequisites:
   - .env file configured with credentials
   - Virtual environment activated
   - Packages installed (pip install -r requirements.txt)
   - Logged in via 'az login'

================================================================
📋 INSTRUCTIONS — Complete the TODOs below!
================================================================

Run when done:  python lab_medium_email_generator.py

EXPECTED OUTPUT (example):
   📧 Generating email draft...
   ──────────────────────────
   Subject: Follow-up: Project Kickoff Discussion
   
   Hi Sarah,
   
   Thank you for taking the time to meet today...
   ...
   
   Best regards,
   [Your Name]
   ──────────────────────────
   📊 Tokens used: 245

================================================================
"""

import os
from dotenv import load_dotenv

# ============================================================
# TASK 1: Set up the Azure OpenAI client (3 points)
# ============================================================
# TODO: Import the required modules and create the client
#
# HINT: Look at how 03_azure_openai_simple.py does it!
#   1. Import AzureOpenAI from openai
#   2. Import DefaultAzureCredential, get_bearer_token_provider 
#      from azure.identity
#   3. Load .env with load_dotenv()
#   4. Create credential and token_provider
#   5. Create the client with AzureOpenAI(...)
#   6. Get the deployment name from environment
# ============================================================

load_dotenv()

# TODO: Import and set up Azure OpenAI client here
# from openai import AzureOpenAI
# from azure.identity import DefaultAzureCredential, get_bearer_token_provider
# 
# credential = DefaultAzureCredential()
# token_provider = get_bearer_token_provider(
#     credential, "https://cognitiveservices.azure.com/.default"
# )
# 
# client = AzureOpenAI(
#     azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
#     azure_ad_token_provider=token_provider,
#     api_version="2024-12-01-preview"
# )
# 
# deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

print("=" * 60)
print("🧪 LAB: Email Draft Generator")
print("=" * 60)


# ============================================================
# TASK 2: Define the email parameters (2 points)
# ============================================================
# TODO: Fill in these variables with your own values
# ============================================================

recipient = "Sarah"                        # Who is the email to?
purpose = "Follow up after project kickoff meeting"  # What's it about?
tone = "professional"                      # professional / casual / formal
key_points = [                             # What to include?
    "Thank her for attending the meeting",
    "Recap the 3 main decisions we made",
    "Remind about the next meeting on Friday"
]

# TODO: Add at least one more key point to the list above


# ============================================================
# TASK 3: Craft a system prompt (4 points)
# ============================================================
# TODO: Write a system prompt that instructs the AI to be an
#       email writing assistant.
#
# Your system prompt should tell the AI:
#   - What it is (an email drafting assistant)
#   - Its writing rules (clear, concise, appropriate tone)
#   - Output format (include Subject line, greeting, body, sign-off)
#   - Any constraints (keep it under 200 words)
#
# HINT: Look at how system prompts are used in 04_azure_openai_chat.py
# ============================================================

# TODO: Replace this with your own system prompt
system_prompt = "You are a helpful assistant."


# ============================================================
# TASK 4: Build the user message (3 points)
# ============================================================
# TODO: Create a user message that includes all the email
#       parameters (recipient, purpose, tone, key_points)
#
# HINT: Use an f-string to combine the variables:
#   user_message = f"""
#   Write an email to {recipient} about {purpose}.
#   Tone: {tone}
#   Key points to cover:
#   {build the list here}
#   """
#
# TIP: To turn key_points list into readable text:
#   points_text = "\n".join(f"- {point}" for point in key_points)
# ============================================================

# TODO: Build the user message
# points_text = "\n".join(f"- {point}" for point in key_points)
# user_message = f"""..."""


# ============================================================
# TASK 5: Make the API call (4 points)
# ============================================================
# TODO: Build the messages list and call the API
#
# Steps:
#   1. Create messages list with system prompt + user message
#   2. Call client.chat.completions.create(...)
#   3. Extract the response text
#   4. Print the email draft
#   5. Print token usage
#
# HINT: Use max_completion_tokens (not max_tokens) for this model
#       messages = [
#           {"role": "system", "content": system_prompt},
#           {"role": "user", "content": user_message}
#       ]
# ============================================================

# TODO: Uncomment and complete the API call
# print("\n📧 Generating email draft...")
# print("─" * 40)
# 
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
# # Extract and print the email
# email_draft = response.choices[0].message.content
# print(email_draft)
# print("─" * 40)
# print(f"📊 Tokens used: {response.usage.total_tokens}")


# ============================================================
# BONUS TASK: Generate multiple tones (3 points)
# ============================================================
# TODO: Loop through different tones and generate an email
#       for each one. Compare how the AI adjusts its writing!
#
# tones = ["professional", "casual", "formal"]
# for tone in tones:
#     # Rebuild user_message with new tone
#     # Make API call
#     # Print result with tone label
#     pass
# ============================================================


# ============================================================
# BONUS TASK 2: Add error handling (2 points)
# ============================================================
# TODO: Wrap the API call in a try/except block
#       Handle at least these errors:
#       - Missing credentials (check before calling)
#       - API errors (catch openai exceptions)
#
# HINT: Look at how 03_azure_openai_simple.py handles errors
# ============================================================


print("\n" + "=" * 60)
print("💡 CONCEPTS USED IN THIS LAB")
print("=" * 60)
print("""
   📝 System prompts → Control AI behavior & output format
   📋 Message format  → [{"role": "...", "content": "..."}]
   🔧 f-strings      → Build dynamic prompts from variables
   📊 Token usage     → Understand API cost
   🔐 Credentials     → Secure access with DefaultAzureCredential
   
   This is the SAME pattern used in real-world apps:
   user input → build prompt → call API → show result
""")
