"""
lab_hard_project_manager_agent_short.py - Multi-Skill PM Agent Lab (Condensed)
Agent with skill routing and conversation memory.
"""

import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

load_dotenv()

credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")

client = AzureOpenAI(
    azure_ad_token_provider=token_provider,
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

print("🧪 LAB: Multi-Skill Project Manager Agent\n")

# TASK 1: Define skill-specific system prompts
SKILL_PROMPTS = {
    "agenda": """You are an expert Meeting Agenda Creator.
# TODO: Add rules for creating structured, time-boxed agendas
""",
    "summarize": """You are an expert Meeting Notes Summarizer.
# TODO: Add rules for extracting decisions, action items, follow-ups
""",
    "email": """You are an expert Follow-Up Email Drafter.
# TODO: Add rules for writing professional follow-up emails
""",
    "risk": """You are an expert Project Risk Analyzer.
# TODO: Add rules for identifying and categorizing risks
"""
}


# TASK 2: Build the agent class
class ProjectManagerAgent:
    def __init__(self, client, model):
        self.client = client
        self.model = model
        self.history = [
            {"role": "system", "content": """You are PM Agent, a professional Project Manager AI.
Detect what the user needs and use the right skill:
- agenda/meeting prep → agenda skill
- meeting notes → summarizer skill
- draft email → email skill
- risks/concerns → risk analyzer skill
Be concise, use bullet points, remember full context."""}
        ]
        self.skills_used = []

    def detect_skill(self, user_message):
        """Detect which skill to use based on keywords."""
        msg = user_message.lower()
        # TODO: Implement keyword detection
        # if any(word in msg for word in ["agenda", "prepare", "plan meeting"]):
        #     return "agenda"
        # elif any(word in msg for word in ["summarize", "notes", "recap"]):
        #     return "summarize"
        # elif any(word in msg for word in ["email", "draft", "write to"]):
        #     return "email"
        # elif any(word in msg for word in ["risk", "concern", "issue"]):
        #     return "risk"
        return None

    def chat(self, user_message):
        """Process message: detect skill, route, respond, remember."""
        skill = self.detect_skill(user_message)

        if skill:
            print(f"  🔧 [Using skill: {skill.upper()}]")
            self.skills_used.append(skill)
            # TODO: Build skill-specific messages with context
            # skill_messages = [
            #     {"role": "system", "content": SKILL_PROMPTS[skill]},
            #     *self.history[1:],  # include conversation context
            #     {"role": "user", "content": user_message}
            # ]
            # response = self.client.chat.completions.create(
            #     model=self.model, messages=skill_messages, max_completion_tokens=500
            # )
            # reply = response.choices[0].message.content
            reply = "TODO: Implement skill-based response"
        else:
            # TODO: Handle general conversation
            # self.history.append({"role": "user", "content": user_message})
            # response = self.client.chat.completions.create(
            #     model=self.model, messages=self.history, max_completion_tokens=300
            # )
            # reply = response.choices[0].message.content
            reply = "TODO: Implement general chat"

        # TODO: Save to history for memory
        # self.history.append({"role": "user", "content": user_message})
        # self.history.append({"role": "assistant", "content": reply})
        return reply


# TASK 3: Test the agent
agent = ProjectManagerAgent(client, deployment)
print(f"✅ PM Agent ready!\n")

# TODO: Uncomment to test
# print("👤 You: Hi! I'm managing a new e-commerce project, launching in 8 weeks.")
# print(f"🤖 {agent.chat('Hi! I'm managing a new e-commerce project with a team of 6. We launch in 8 weeks.')}\n")
#
# print("👤 You: Create an agenda for our kickoff meeting tomorrow.")
# print(f"🤖 {agent.chat('Create an agenda for our kickoff meeting tomorrow. 1 hour, 6 people.')}\n")
#
# print("👤 You: What risks do you see?")
# print(f"🤖 {agent.chat('What risks do you see based on everything we discussed?')}\n")
#
# print("👤 You: Draft a follow-up email to the team.")
# print(f"🤖 {agent.chat('Draft a follow-up email to the team.')}\n")
#
# agent.get_stats()
