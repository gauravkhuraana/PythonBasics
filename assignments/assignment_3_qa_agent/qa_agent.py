"""
================================================================
🧪 LAB ASSIGNMENT 3 — HARD LEVEL
   Build a Multi-Skill Project Manager Agent
================================================================

⏱️  Estimated time: 30-45 minutes
🎯  Difficulty: ⭐⭐⭐ Hard (Agent with tools & memory)

SCENARIO:
   Build a Project Manager Agent that can handle MULTIPLE types
   of requests through different "skills" (tools). The agent
   should detect what the user needs and route to the right skill.

   Skills:
   1. 📋 Agenda Creator   — Build meeting agendas
   2. 📝 Notes Summarizer — Summarize meeting notes + action items
   3. 📧 Email Drafter    — Write follow-up emails from meetings
   4. ⚠️  Risk Analyzer   — Identify project risks from discussion

SKILLS TESTED (from Files 01-05):
   ✅ Python classes and methods
   ✅ System prompts & role-based messages
   ✅ Multi-turn conversation with memory
   ✅ Building an agent architecture
   ✅ Tool/skill routing logic
   ✅ Prompt engineering for different tasks

Prerequisites:
   - All previous files completed
   - .env file configured
   - Logged in via 'az login'

================================================================
📋 INSTRUCTIONS — Complete the TODOs below!
================================================================

Run when done:  python lab_hard_project_manager_agent.py

EXPECTED BEHAVIOR:
   Agent detects what you need and uses the right skill:
   
   You: "I have a meeting tomorrow with 5 people about Q2 planning"
   Agent: [Uses Agenda Creator skill] → Generates structured agenda
   
   You: "Here are my notes from today's standup: ..."
   Agent: [Uses Notes Summarizer skill] → Summary + action items
   
   You: "Draft a follow-up email to the team about what we discussed"
   Agent: [Uses Email Drafter skill] → Professional email using context
   
   You: "What risks did you notice in our discussion?"
   Agent: [Uses Risk Analyzer skill] → Risk assessment from context

================================================================
"""

import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# Load credentials and create client
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

print("=" * 60)
print("🧪 LAB: Multi-Skill Project Manager Agent")
print("=" * 60)


# ============================================================
# TASK 1: Define the Skill Prompts (5 points)
# ============================================================
# TODO: Write specialized system prompts for each skill.
#       Each prompt should clearly instruct the AI on:
#       - What role it plays for this skill
#       - What format to use for output
#       - Any rules or constraints
#
# HINT: Think about what makes a good agenda vs. a good
#       summary vs. a good email. Each needs different rules!
# ============================================================

SKILL_PROMPTS = {
    "agenda": """You are an expert Meeting Agenda Creator.
# TODO: Complete this prompt. Tell the AI:
#   - To create structured, time-boxed agendas
#   - Include agenda item, duration, and owner
#   - Always add a "parking lot" for off-topic items
#   - Format as a clean, numbered list
""",
    
    "summarize": """You are an expert Meeting Notes Summarizer.
# TODO: Complete this prompt. Tell the AI:
#   - To extract key decisions, action items, and follow-ups
#   - Action items must have: task, owner, deadline
#   - Include a "TL;DR" at the top (3 sentences max)
#   - Flag any unresolved items
""",
    
    "email": """You are an expert Follow-Up Email Drafter.
# TODO: Complete this prompt. Tell the AI:
#   - To write professional follow-up emails
#   - Include: Subject line, greeting, recap, action items, sign-off
#   - Reference specific discussion points from context
#   - Keep it concise (under 200 words for the body)
""",
    
    "risk": """You are an expert Project Risk Analyzer.
# TODO: Complete this prompt. Tell the AI:
#   - To identify risks from meeting discussions
#   - Categorize: Timeline, Resource, Technical, Scope risks
#   - Rate each risk: High / Medium / Low
#   - Suggest mitigation actions
#   - Format as a risk register table
"""
}


# ============================================================
# TASK 2: Build the ProjectManagerAgent class (8 points)
# ============================================================
# TODO: Complete the agent class below.
#       Key requirements:
#       - Has a main system prompt (the "manager" personality)
#       - Maintains conversation history across all messages
#       - Can detect which skill to use based on user input
#       - Routes to the right skill prompt for specialized tasks
#
# HINT: Look at MeetingAssistant in 05_meeting_assistant_agent.py
#       for the basic pattern, then ADD skill detection on top.
# ============================================================

class ProjectManagerAgent:
    """A multi-skill Project Manager Agent with conversation memory."""
    
    def __init__(self, client, model):
        self.client = client
        self.model = model
        self.name = "PM Agent"
        
        # The manager's core personality
        self.system_prompt = """You are a professional Project Manager AI called "PM Agent".

You have multiple skills and should use the most appropriate one:
- When asked about agendas or meeting preparation → use agenda skill
- When given meeting notes to process → use summarizer skill  
- When asked to draft emails → use email skill
- When asked about risks or concerns → use risk analyzer skill

For general questions, respond helpfully using your PM expertise.
Always remember our full conversation context.
Be concise, use bullet points, and stay professional."""

        # Conversation history — the agent's memory!
        self.history = [
            {"role": "system", "content": self.system_prompt}
        ]
        
        # Track which skills have been used
        self.skills_used = []
    
    
    def detect_skill(self, user_message):
        """
        Detect which skill to use based on the user's message.
        Returns: "agenda", "summarize", "email", "risk", or None
        
        TODO: Implement skill detection logic (4 points)
        
        HINT: Check if certain keywords appear in the message.
              Use .lower() for case-insensitive matching.
        
        Examples:
          "Create an agenda for..."      → "agenda"
          "Summarize these notes..."     → "summarize"
          "Draft a follow-up email..."   → "email"
          "What risks do you see..."     → "risk"
          "Hello, how are you?"          → None (general chat)
        """
        msg = user_message.lower()
        
        # TODO: Add keyword detection for each skill
        # if any(word in msg for word in ["agenda", "prepare", "plan meeting"]):
        #     return "agenda"
        # elif ...
        #     return "summarize"
        # elif ...
        #     return "email"
        # elif ...
        #     return "risk"
        
        return None  # General conversation (no specific skill)
    
    
    def chat(self, user_message):
        """
        Process a user message: detect skill, route, and respond.
        
        TODO: Implement the chat method (4 points)
        
        Steps:
          1. Detect which skill to use
          2. If a skill is detected:
             - Build a messages list with the SKILL prompt as system
             - Include recent conversation context
             - Make the API call with the skill prompt
          3. If no skill detected:
             - Use the regular conversation (self.history)
             - Make a normal API call
          4. Save the exchange to self.history (for memory!)
          5. Return the assistant's response
        
        HINT: For skill-based calls, you want to temporarily use the
              skill-specific system prompt, but still include context
              from self.history so the AI knows what was discussed.
        """
        
        # Detect skill
        skill = self.detect_skill(user_message)
        
        if skill:
            print(f"   🔧 [Using skill: {skill.upper()}]")
            self.skills_used.append(skill)
            
            # TODO: Build skill-specific messages
            # Include the skill system prompt + conversation context + new message
            # 
            # skill_messages = [
            #     {"role": "system", "content": SKILL_PROMPTS[skill]},
            #     # Include last few messages from self.history for context
            #     # (skip the system message at index 0)
            #     ...
            #     {"role": "user", "content": user_message}
            # ]
            # 
            # response = self.client.chat.completions.create(
            #     model=self.model,
            #     messages=skill_messages,
            #     max_completion_tokens=500
            # )
            # 
            # assistant_reply = response.choices[0].message.content
            
            assistant_reply = "TODO: Implement skill-based response"
        else:
            # TODO: Handle general conversation
            # self.history.append({"role": "user", "content": user_message})
            # 
            # response = self.client.chat.completions.create(
            #     model=self.model,
            #     messages=self.history,
            #     max_completion_tokens=300
            # )
            # 
            # assistant_reply = response.choices[0].message.content
            
            assistant_reply = "TODO: Implement general chat response"
        
        # TODO: Save to history (for memory across turns)
        # self.history.append({"role": "user", "content": user_message})
        # self.history.append({"role": "assistant", "content": assistant_reply})
        
        return assistant_reply
    
    
    def get_stats(self):
        """Show agent usage statistics."""
        total_messages = len(self.history) - 1  # exclude system prompt
        print(f"\n📊 Agent Stats:")
        print(f"   Total messages: {total_messages}")
        print(f"   Skills used: {', '.join(self.skills_used) if self.skills_used else 'None yet'}")
        unique_skills = set(self.skills_used)
        print(f"   Unique skills: {len(unique_skills)}/4")


# ============================================================
# TASK 3: Test the Agent (3 points)
# ============================================================
# TODO: Uncomment the test conversation below once you've
#       completed Tasks 1 and 2. Verify each message uses
#       the correct skill.
# ============================================================

# Create the agent
agent = ProjectManagerAgent(client, deployment)
print(f"\n✅ {agent.name} is ready!")
print("=" * 60)

# --- Test Conversation ---

# TODO: Uncomment this test conversation:

# # Message 1: General greeting (should use NO skill)
# print("\n👤 You: Hi! I'm managing a new e-commerce project.")
# response = agent.chat("Hi! I'm managing a new e-commerce project with a team of 6. We launch in 8 weeks.")
# print(f"\n🤖 PM Agent:\n{response}")
# print("\n" + "-" * 40)
# 
# # Message 2: Agenda request (should use AGENDA skill)
# print("\n👤 You: Create an agenda for our kickoff meeting tomorrow. 1 hour, 6 people.")
# response = agent.chat("Create an agenda for our kickoff meeting tomorrow. 1 hour, 6 people.")
# print(f"\n🤖 PM Agent:\n{response}")
# print("\n" + "-" * 40)
# 
# # Message 3: Meeting notes (should use SUMMARIZE skill)
# meeting_notes = """Here are the notes from today's standup:
# - Frontend team completed the login page, starting on product catalog
# - Backend API is behind schedule, need 3 extra days for payment integration
# - Design team waiting on brand assets from marketing (blocked)
# - QA found 12 bugs in the last sprint, 4 are critical
# - Marketing wants to add a referral feature (scope creep?)
# """
# print(f"\n👤 You: Summarize these meeting notes:\n{meeting_notes}")
# response = agent.chat(f"Summarize these meeting notes and extract action items:\n{meeting_notes}")
# print(f"\n🤖 PM Agent:\n{response}")
# print("\n" + "-" * 40)
# 
# # Message 4: Risk analysis (should use RISK skill)
# print("\n👤 You: What risks do you see based on everything we discussed?")
# response = agent.chat("What risks do you see based on everything we discussed so far?")
# print(f"\n🤖 PM Agent:\n{response}")
# print("\n" + "-" * 40)
# 
# # Message 5: Email draft (should use EMAIL skill)
# print("\n👤 You: Draft a follow-up email to the team about today's standup.")
# response = agent.chat("Draft a follow-up email to the team summarizing today's standup results and the risks we identified.")
# print(f"\n🤖 PM Agent:\n{response}")
# print("\n" + "-" * 40)
# 
# # Message 6: Memory test (should remember everything!)
# print("\n👤 You: How many weeks do we have until launch?")
# response = agent.chat("How many weeks do we have until launch? And what's our biggest risk?")
# print(f"\n🤖 PM Agent:\n{response}")
# 
# # Show stats
# agent.get_stats()


# ============================================================
# BONUS TASK: Add a "priority matrix" skill (3 points)
# ============================================================
# TODO: Add a 5th skill that creates an Eisenhower Priority
#       Matrix (Urgent+Important, Important, Urgent, Neither)
#       from the action items discussed in the conversation.
#
# Steps:
#   1. Add "priority" to SKILL_PROMPTS with a good prompt
#   2. Add detection keywords in detect_skill()
#   3. Test with: "Prioritize all the action items we discussed"
# ============================================================


# ============================================================
# BONUS TASK 2: Conversation export (2 points)
# ============================================================
# TODO: Add a method to the agent that exports the full
#       conversation to a formatted text file.
#
# def export_conversation(self, filename="meeting_log.txt"):
#     with open(filename, "w") as f:
#         for msg in self.history:
#             if msg["role"] != "system":
#                 f.write(f"[{msg['role'].upper()}]\n{msg['content']}\n\n")
#     print(f"📁 Conversation exported to {filename}")
# ============================================================


print("\n" + "=" * 60)
print("💡 CONCEPTS USED IN THIS LAB")
print("=" * 60)
print("""
   🤖 Agent architecture → Class with memory + skills
   🧠 Conversation memory → self.history list persists context
   🔧 Skill routing      → Detect intent → pick right prompt
   📝 Prompt engineering  → Different system prompts per skill
   🔗 Context passing     → Skills receive conversation history
   📊 State tracking      → skills_used, message_count
   
   This is how REAL AI agents work:
   detect intent → route to skill → generate with context → remember
   
   🏆 CHALLENGE: Can you get the agent to use all 4 skills
      in a single conversation and have it remember everything?
""")
