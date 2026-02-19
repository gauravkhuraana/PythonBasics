"""
================================================================
05_meeting_assistant_agent.py
🎯 FINALE: Build Your AI Meeting Assistant Agent!
================================================================

🎉 CONGRATULATIONS! You've reached the final exercise!

In this file, you'll build a Meeting Assistant AGENT that:
  ✅ Has a defined personality and instructions
  ✅ Remembers your ENTIRE conversation automatically
  ✅ Helps with agendas, action items, and follow-ups
  ✅ No manual history management needed!

AGENT vs CHAT COMPLETION:
  - Chat: You manage message history yourself
  - Agent: Memory is built-in — the class handles it for you!

Run this file: python 05_meeting_assistant_agent.py
================================================================
"""

import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# Load credentials
load_dotenv()

# Use Azure AD authentication (key-based auth is disabled by org policy)
credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(
    credential, "https://cognitiveservices.azure.com/.default"
)

# Create Azure OpenAI client
client = AzureOpenAI(
    azure_ad_token_provider=token_provider,
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

print("=" * 60)
print("🎯 FINALE: Building Your AI Meeting Assistant Agent!")
print("=" * 60)


# ============================================================
# STEP 1: DEFINE THE AGENT CLASS (Like hiring a specialist)
# ============================================================
print("\n" + "-" * 40)
print("STEP 1: Creating the Meeting Assistant Agent")
print("-" * 40)

print("""
📝 AGENT CONCEPTS:

   🤖 Agent (MeetingAssistant class)
      • Has a name and personality (system prompt)
      • Follows instructions you define
      • Remembers your entire conversation automatically
   
   💬 Conversation History (managed internally)
      • Stores all messages automatically
      • YOU don't manage history anymore!
   
   ▶️  chat() method
      • Send a message, get a response
      • History is tracked behind the scenes
""")


class MeetingAssistant:
    """An AI Meeting Assistant agent with built-in conversation memory."""
    
    def __init__(self, client, model, name="Meeting Assistant"):
        self.client = client
        self.model = model
        self.name = name
        # The system prompt gives the agent its personality
        self.system_prompt = """You are a professional Meeting Assistant called "Meeting Assistant".

YOUR RESPONSIBILITIES:
1. Help prepare meeting agendas
2. Summarize meeting notes concisely  
3. Extract action items with owners and deadlines
4. Suggest follow-up topics and next steps
5. Remember all context from our conversation

YOUR STYLE:
- Be concise and use bullet points
- Stay professional but friendly
- Proactively offer helpful suggestions
- Always ask if there's anything else you can help with

REMEMBER: You maintain context across our entire conversation. 
Reference previous messages to show you remember what we discussed."""

        # Conversation history — managed automatically!
        self.history = [
            {"role": "system", "content": self.system_prompt}
        ]
    
    def chat(self, user_message):
        """Send a message and get a response. History is tracked automatically."""
        # Add user message to history
        self.history.append({"role": "user", "content": user_message})
        
        # Call Azure OpenAI with FULL history
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.history,
            max_completion_tokens=300
        )
        
        # Extract assistant reply
        assistant_reply = response.choices[0].message.content
        
        # Save assistant reply to history (so the agent remembers!)
        self.history.append({"role": "assistant", "content": assistant_reply})
        
        return assistant_reply
    
    @property
    def message_count(self):
        """How many messages in the conversation (excluding system prompt)."""
        return len(self.history) - 1


# Create our Meeting Assistant agent
agent = MeetingAssistant(client, deployment)
print(f"\n✅ Created Agent: {agent.name}")
print(f"   Model: {agent.model}")
print("   Conversation memory is managed automatically!")


# ============================================================
# STEP 2: HAVE A CONVERSATION (The "Wow" Moment!)
# ============================================================
print("\n" + "-" * 40)
print("STEP 2: Conversation with Meeting Assistant")
print("-" * 40)

print("\n🌟 Watch how the agent REMEMBERS context automatically!\n")
print("=" * 60)

# Message 1: Introduction
print("\n👤 You: Hi! I need help preparing for a team standup meeting tomorrow.")
print("   (The meeting is at 10 AM with 4 team members)")
response = agent.chat("Hi! I need help preparing for a team standup meeting tomorrow. The meeting is at 10 AM with 4 team members.")
print(f"\n🤖 Meeting Assistant:\n{response}")

print("\n" + "-" * 40)

# Message 2: Add more context (agent should remember previous info!)
print("\n👤 You: The team is working on a mobile app launch. We're 2 weeks from release.")
response = agent.chat("The team is working on a mobile app launch. We're 2 weeks from release.")
print(f"\n🤖 Meeting Assistant:\n{response}")

print("\n" + "-" * 40)

# Message 3: Ask for agenda (agent should use ALL context!)
print("\n👤 You: Based on what I told you, create a 15-minute agenda for me.")
response = agent.chat("Based on what I told you, create a 15-minute agenda for me.")
print(f"\n🤖 Meeting Assistant:\n{response}")

print("\n" + "-" * 40)

# Message 4: Reference earlier context
print("\n👤 You: What did I say about the timeline?")
response = agent.chat("What did I say about the timeline?")
print(f"\n🤖 Meeting Assistant:\n{response}")

print("\n" + "=" * 60)

print(f"\n📊 Conversation length: {agent.message_count} messages")
print("   The agent remembered everything without you resending history!")


# ============================================================
# THE WOW MOMENT!
# ============================================================
print("\n" + "=" * 60)
print("🌟 THE WOW MOMENT - What Just Happened?")
print("=" * 60)

print("""
Notice how the Meeting Assistant:

   ✅ Remembered "10 AM" and "4 team members" from message 1
   ✅ Combined it with "mobile app" and "2 weeks" from message 2  
   ✅ Created an agenda using ALL the context in message 3
   ✅ Correctly recalled the timeline in message 4

YOU DIDN'T:
   ❌ Manually track message history
   ❌ Resend all previous messages
   ❌ Remind the AI what you said before

THIS IS THE POWER OF AGENTS:
   The MeetingAssistant class handles memory for you!
   Just call agent.chat() and it remembers everything!
""")


# ============================================================
# BONUS: TRY YOUR OWN MEETING SCENARIO
# ============================================================
print("\n" + "=" * 60)
print("🧪 BONUS: Try Your Own Conversation!")
print("=" * 60)

print("""
The agent is still running! Uncomment the code below to continue
the conversation with your own messages.

Ideas to try:
- "Add a 5-minute buffer for questions"
- "Who should I send the agenda to?"
- "Help me write a meeting invite email"
""")

# Uncomment to try:
# print("\n👤 You: [Your message here]")
# response = agent.chat("Your message here - try asking about the agenda!")
# print(f"\n🤖 Meeting Assistant:\n{response}")


# ============================================================
# FINAL SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("🎉 CONGRATULATIONS! You Built an AI Meeting Assistant!")
print("=" * 60)

print("""
📚 WHAT YOU LEARNED TODAY:

   File 01: Python fundamentals (str, int, list, dict)
   File 02: Environment setup (venv, .env, .gitignore)
   File 03: First Azure OpenAI API call
   File 04: Chat with message history
   File 05: Building an AI Agent with memory!

🔑 KEY CONCEPTS:

   • Variables & types → Building blocks
   • .env files → Keep secrets safe  
   • API calls → Talk to AI
   • Agents → AI with memory and personality

🚀 WHAT'S NEXT?

   • Add tools (code interpreter, file search)
   • Build a web interface (Streamlit, Gradio)
   • Connect to your real meeting data
   • Explore RAG (AI + your documents)
""")

print("\n" + "=" * 60)
print("✅ SESSION COMPLETE! Great job! 🎉")
print("=" * 60)
