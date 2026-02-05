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
  - Agent: Memory is built-in via "threads"!

Run this file: python 05_meeting_assistant_agent.py
================================================================
"""

import os
import time
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load credentials
load_dotenv()

# Create Azure OpenAI client for Assistants API
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-08-01-preview",  # Latest stable version for Assistants
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

print("=" * 60)
print("🎯 FINALE: Building Your AI Meeting Assistant Agent!")
print("=" * 60)


# ============================================================
# STEP 1: CREATE THE AGENT (Like hiring a specialist)
# ============================================================
print("\n" + "-" * 40)
print("STEP 1: Creating the Meeting Assistant Agent")
print("-" * 40)

print("""
📝 AGENT CONCEPTS:

   🤖 Agent (Assistant)
      • Has a name and personality
      • Follows instructions you define
      • Persists until you delete it
   
   💬 Thread
      • A conversation session
      • Stores all messages automatically
      • YOU don't manage history anymore!
   
   ▶️  Run
      • When the agent processes and responds
      • You create a run, wait for it, get the response
""")

# Create our Meeting Assistant with detailed instructions
assistant = client.beta.assistants.create(
    name="Meeting Assistant",
    instructions="""You are a professional Meeting Assistant called "Meeting Assistant".

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
Reference previous messages to show you remember what we discussed.""",
    model=deployment
)

print(f"\n✅ Created Agent: {assistant.name}")
print(f"   ID: {assistant.id}")


# ============================================================
# STEP 2: CREATE A THREAD (Conversation with memory)
# ============================================================
print("\n" + "-" * 40)
print("STEP 2: Creating Conversation Thread")
print("-" * 40)

thread = client.beta.threads.create()

print(f"\n✅ Created Thread (conversation)")
print(f"   ID: {thread.id}")
print("   This thread will remember everything we discuss!")


# ============================================================
# STEP 3: HELPER FUNCTION - Chat with Agent
# ============================================================
def chat(user_message):
    """Send a message to the agent and get the response."""
    
    # Add user message to the thread
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_message
    )
    
    # Create a run (agent processes the thread)
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id
    )
    
    # Wait for completion (poll every 1 second)
    while run.status not in ["completed", "cancelled", "expired", "failed"]:
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
    
    # Check for failure
    if run.status == "failed":
        return f"Error: Run failed - {run.last_error}"
    
    if run.status == "completed":
        # Get the latest message (agent's response)
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        
        # Extract text from the first (most recent) assistant message
        for msg in messages.data:
            if msg.role == "assistant":
                for content_block in msg.content:
                    if content_block.type == "text":
                        return content_block.text.value
        return "Error: No response found"
    else:
        return f"Error: Run ended with status {run.status}"


# ============================================================
# STEP 4: HAVE A CONVERSATION (The "Wow" Moment!)
# ============================================================
print("\n" + "-" * 40)
print("STEP 4: Conversation with Meeting Assistant")
print("-" * 40)

print("\n🌟 Watch how the agent REMEMBERS context automatically!\n")
print("=" * 60)

# Message 1: Introduction
print("\n👤 You: Hi! I need help preparing for a team standup meeting tomorrow.")
print("   (The meeting is at 10 AM with 4 team members)")
response = chat("Hi! I need help preparing for a team standup meeting tomorrow. The meeting is at 10 AM with 4 team members.")
print(f"\n🤖 Meeting Assistant:\n{response}")

print("\n" + "-" * 40)

# Message 2: Add more context (agent should remember previous info!)
print("\n👤 You: The team is working on a mobile app launch. We're 2 weeks from release.")
response = chat("The team is working on a mobile app launch. We're 2 weeks from release.")
print(f"\n🤖 Meeting Assistant:\n{response}")

print("\n" + "-" * 40)

# Message 3: Ask for agenda (agent should use ALL context!)
print("\n👤 You: Based on what I told you, create a 15-minute agenda for me.")
response = chat("Based on what I told you, create a 15-minute agenda for me.")
print(f"\n🤖 Meeting Assistant:\n{response}")

print("\n" + "-" * 40)

# Message 4: Reference earlier context
print("\n👤 You: What did I say about the timeline?")
response = chat("What did I say about the timeline?")
print(f"\n🤖 Meeting Assistant:\n{response}")

print("\n" + "=" * 60)


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
   The Thread stores everything automatically!
   The Agent remembers and uses all context!
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
# response = chat("Your message here - try asking about the agenda!")
# print(f"\n🤖 Meeting Assistant:\n{response}")


# ============================================================
# CLEANUP (Optional)
# ============================================================
# In a real app, you might want to keep the assistant
# For this demo, let's clean up

try:
    client.beta.assistants.delete(assistant.id)
    print("\n🧹 Cleanup: Agent deleted (demo complete)")
except:
    pass


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
