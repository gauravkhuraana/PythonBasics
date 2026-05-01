"""
================================================================
04_azure_openai_chat.py
AZURE OPENAI: Chat with Message History
================================================================

🎯 LAB GOAL REMINDER:
Building toward your AI Meeting Assistant!
Now let's add system prompts and conversation history.

This file covers:
  ✅ System prompts - Setting AI behavior/personality
  ✅ Multi-turn conversations - Chat history
  ✅ Message roles: system, user, assistant
  ✅ Meeting-themed examples

Prerequisites:
  - Completed 03_azure_openai_simple.py
  - Credentials configured in .env

Run this file: python 04_azure_openai_chat.py
================================================================
"""

import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# Load credentials and create client
load_dotenv()

# Use Azure AD authentication (key-based auth is disabled by org policy)
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

print("=" * 60)
print("AZURE OPENAI: Chat with Message History")
print("=" * 60)


# ============================================================
# PART 1: UNDERSTANDING MESSAGE ROLES
# ============================================================
print("\n" + "-" * 40)
print("PART 1: Message Roles Explained")
print("-" * 40)

print("""
📝 THREE ROLES IN AZURE OPENAI CHAT:

   1. "system" - Instructions for the AI
      • Sets personality, rules, and behavior
      • Only seen by the AI, not the user
      • Example: "You are a helpful meeting assistant."
   
   2. "user" - What the human says
      • Your questions and requests
      • Example: "Summarize these meeting notes."
   
   3. "assistant" - What the AI responds
      • The AI's previous answers
      • Used to maintain conversation history
      • Example: "Here's the summary: ..."
""")


# ============================================================
# PART 2: SYSTEM PROMPT - Setting AI Behavior
# ============================================================
print("-" * 40)
print("PART 2: System Prompt Example")
print("-" * 40)

# A good system prompt for our Meeting Assistant
system_prompt = """You are a professional Meeting Assistant AI.

Your responsibilities:
- Help create meeting agendas
- Summarize meeting notes concisely
- Extract action items and assign owners
- Suggest follow-up topics

Your style:
- Be concise and use bullet points
- Stay professional but friendly
- Always ask if the user needs anything else"""

print(f"\n📋 System Prompt:\n{system_prompt}")

# Make a request with the system prompt
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "Hi! Can you help me prepare for my team meeting?"}
]

print("\n⏳ Sending request with system prompt...")

response = client.chat.completions.create(
    model=deployment,
    messages=messages,
    max_completion_tokens=200
)

print("\n🤖 AI Response (notice the Meeting Assistant personality):")
print("-" * 40)
print(response.choices[0].message.content)
print("-" * 40)


# ============================================================
# PART 3: MULTI-TURN CONVERSATION
# ============================================================
print("\n" + "-" * 40)
print("PART 3: Multi-Turn Conversation")
print("-" * 40)

print("""
💡 KEY INSIGHT:
   The AI has no memory between API calls!
   YOU must send the entire conversation history each time.
   
   Call 1: [system, user1]              → assistant1
   Call 2: [system, user1, assistant1, user2] → assistant2
   Call 3: [system, user1, assistant1, user2, assistant2, user3] → assistant3
""")

# Build a conversation about a meeting
conversation = [
    {"role": "system", "content": "You are a helpful meeting assistant. Be concise."},
    {"role": "user", "content": "I have a project kickoff meeting tomorrow with 5 people."}
]

print("\n🗣️  CONVERSATION START")
print("-" * 40)
print(f"👤 User: {conversation[1]['content']}")

# First response
response1 = client.chat.completions.create(
    model=deployment,
    messages=conversation,
    max_completion_tokens=150
)
assistant_msg1 = response1.choices[0].message.content
print(f"\n🤖 Assistant: {assistant_msg1}")

# Add assistant's response to history and continue
conversation.append({"role": "assistant", "content": assistant_msg1})
conversation.append({"role": "user", "content": "The meeting is about launching a new mobile app."})

print(f"\n👤 User: {conversation[3]['content']}")

# Second response (includes full history!)
response2 = client.chat.completions.create(
    model=deployment,
    messages=conversation,
    max_completion_tokens=200
)
assistant_msg2 = response2.choices[0].message.content
print(f"\n🤖 Assistant: {assistant_msg2}")

# Add to history and ask for action items
conversation.append({"role": "assistant", "content": assistant_msg2})
conversation.append({"role": "user", "content": "Based on our discussion, what should be on the agenda?"})

print(f"\n👤 User: {conversation[5]['content']}")

# Third response
response3 = client.chat.completions.create(
    model=deployment,
    messages=conversation,
    max_completion_tokens=300
)
print(f"\n🤖 Assistant: {response3.choices[0].message.content}")
print("-" * 40)

print(f"\n📊 Conversation length: {len(conversation)} messages")
print("   Notice: The AI remembered 'project kickoff' and 'mobile app'!")


# ============================================================
# PART 4: MEETING NOTES EXAMPLE
# ============================================================
print("\n" + "-" * 40)
print("PART 4: Practical Example - Meeting Notes Summary")
print("-" * 40)

meeting_notes = """
Meeting: Q1 Planning - Jan 15, 2026
Attendees: Sarah (PM), John (Dev), Lisa (Design), Mike (QA)

Discussion:
- Sarah presented Q1 roadmap, targeting 3 major features
- John raised concerns about timeline for Feature A, needs 2 extra weeks
- Lisa showed mockups for new dashboard, team approved with minor changes
- Mike suggested adding automated testing before each release
- Budget discussion postponed to next week

Decisions:
- Feature A deadline extended to Feb 28
- Dashboard design approved
- Mike to create automated testing proposal
"""

print(f"📝 Meeting Notes:\n{meeting_notes}")

summary_request = [
    {"role": "system", "content": "You are a meeting assistant. Extract key information concisely."},
    {"role": "user", "content": f"Please summarize these meeting notes and list action items:\n\n{meeting_notes}"}
]

print("\n⏳ Asking AI to summarize and extract action items...")

response = client.chat.completions.create(
    model=deployment,
    messages=summary_request,
    max_completion_tokens=300
)

print("\n🤖 AI Summary & Action Items:")
print("-" * 40)
print(response.choices[0].message.content)
print("-" * 40)


print("\n" + "=" * 60)
print("🎯 KEY TAKEAWAYS")
print("=" * 60)
print("""
   1. System prompt → Set AI personality (do this once)
   2. User message → Your questions and input
   3. Assistant message → AI's previous responses
   
   4. For multi-turn chat:
      • Store ALL messages in a list
      • Send the FULL list with each API call
      • Append new messages after each response
   
   5. The AI doesn't remember - YOU manage the history!
   
   🚀 NEXT: We'll build an Agent that handles memory for us!
""")


print("\n" + "=" * 60)
print("✅ COMPLETE! Next: python 05_meeting_assistant_agent.py")
print("=" * 60)


# ============================================================
# 🧪 TRY IT YOURSELF!
# ============================================================
# Try changing the meeting notes above and run again!
# Or add your own meeting notes to summarize.

# your_notes = """
# Your meeting notes here...
# """
# 
# response = client.chat.completions.create(
#     model=deployment,
#     messages=[
#         {"role": "system", "content": "Summarize meeting notes and extract action items."},
#         {"role": "user", "content": your_notes}
#     ],
#     max_completion_tokens=300
# )
# print(response.choices[0].message.content)
