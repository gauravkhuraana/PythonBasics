"""
06_life_assistant_short.py - Your Personal Life Assistant 🌟
The Grand Finale: Everything from this session in one program
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


# --- Life categories with expert system prompts ---
categories = {
    "1": {
        "name": "🥗 Diet & Nutrition",
        "prompt": """You are a practical Indian diet and nutrition coach.
- Give advice based on Indian food (dal, roti, sabzi, rice, etc.)
- Suggest realistic meals for working professionals
- Include protein, fiber, and calorie awareness
- Keep it simple — no fancy superfoods, use what's in every Indian kitchen"""
    },
    "2": {
        "name": "💪 Fitness & Exercise",
        "prompt": """You are a no-nonsense fitness coach for busy professionals.
- Suggest workouts that fit in 20-30 minutes
- Include home workouts (no gym needed)
- Be practical: morning routines, desk stretches, walk goals
- Motivate without being preachy — facts over fluff"""
    },
    "3": {
        "name": "🤖 AI & Tech Learning",
        "prompt": """You are an AI learning mentor for software professionals.
- Recommend practical learning paths (not just theory)
- Focus on Azure AI, Python, LLMs, and prompt engineering
- Suggest weekend projects and hands-on labs
- Give honest career advice about AI skills that actually matter"""
    },
    "4": {
        "name": "🧘 Motivation & Mindset",
        "prompt": """You are a wise and warm motivational coach.
- Draw wisdom from Bhagavad Gita, Stoicism, and modern psychology
- Give practical mindset shifts, not generic "believe in yourself" advice
- Help with imposter syndrome, burnout, and career growth anxiety
- Keep it real — acknowledge struggles before offering solutions"""
    },
    "5": {
        "name": "💰 Personal Finance",
        "prompt": """You are a practical personal finance advisor for Indian professionals.
- Cover SIPs, mutual funds, PPF, NPS, tax saving (80C, 80D)
- Explain in simple terms — no jargon without explanation
- Help with budgeting, emergency funds, and salary negotiation
- Be honest about risks — no "get rich quick" nonsense"""
    },
    "6": {
        "name": "📚 Book & Learning Recommendations",
        "prompt": """You are a thoughtful book curator and learning guide.
- Recommend books based on what the person is going through
- Mix genres: self-help, tech, fiction, biography, philosophy
- Give a 2-line reason WHY each book matters right now
- Suggest podcasts, YouTube channels, and courses too"""
    },
    "7": {
        "name": "⏰ Productivity & Time Management",
        "prompt": """You are a productivity coach who respects work-life balance.
- Suggest realistic routines (not 4 AM wake-up cult)
- Help with meeting overload, focus time, and deep work
- Tools and techniques: Pomodoro, time-blocking, 2-minute rule
- Help say NO to things that don't matter"""
    }
}


# --- The Assistant class (everything from session, wrapped up) ---
class LifeAssistant:
    def __init__(self, client, deployment, system_prompt, category_name):
        self.client = client
        self.deployment = deployment
        self.category = category_name
        self.history = [{"role": "system", "content": system_prompt}]
        self.question_count = 0

    def chat(self, user_message):
        self.history.append({"role": "user", "content": user_message})
        self.question_count += 1

        response_object = self.client.chat.completions.create(
            model=self.deployment,
            messages=self.history,
            max_completion_tokens=4000
        )

        response = response_object.choices[0].message.content
        if not response:
            response = "(Model used all tokens for thinking. Try a simpler question.)"
        self.history.append({"role": "assistant", "content": response})
        return response


# --- Exit messages ---
def get_farewell(client, deployment, category, question_count):
    farewell_prompt = f"""The user just finished a {category} conversation ({question_count} questions).
Give them a farewell that includes:
1. A relevant shloka from Bhagavad Gita that connects to {category}:
   - Chapter name and number (e.g., Chapter 2 - Sankhya Yoga)
   - Shloka number (e.g., Verse 47)
   - Sanskrit text
   - English translation
   - One line on why it's relevant to {category}
2. Then a light testing/QA/developer joke to end on a fun note
3. End with an encouraging one-liner

Keep it impactful."""

    response_object = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": farewell_prompt}],
        max_completion_tokens=4000
    )
    return response_object.choices[0].message.content


# ═══════════════════════════════════════════════
#                  🚀 SHOWTIME
# ═══════════════════════════════════════════════

print("═" * 50)
print("   🌟 YOUR PERSONAL LIFE ASSISTANT 🌟")
print("   Built with Python + Azure OpenAI")
print("   (Everything you learned today, in action)")
print("═" * 50)

print("\nHow can I help you today?\n")
for key, cat in categories.items():
    print(f"  {key}. {cat['name']}")

print()
choice = input("Pick a number (1-7): ").strip()

if choice not in categories:
    print("Invalid choice. Let's go with Motivation! 🧘")
    choice = "4"

selected = categories[choice]
print(f"\n✅ Loading: {selected['name']}")
print(f"{'─' * 50}")
print("Ask me anything! Type 'quit' when done.\n")

assistant = LifeAssistant(client, deployment, selected["prompt"], selected["name"])

while True:
    user_input = input("👤 You: ")
    if user_input.lower() == "quit":
        break

    response = assistant.chat(user_input)
    print(f"\n🤖 Assistant: {response}\n")

# --- The Grand Exit ---
print("\n" + "═" * 50)
print("   🙏 BEFORE YOU GO...")
print("═" * 50 + "\n")

farewell = get_farewell(client, deployment, selected["name"], assistant.question_count)
print(farewell)

print(f"\n{'─' * 50}")
print(f"📊 Session Stats:")
print(f"   Category: {selected['name']}")
print(f"   Questions asked: {assistant.question_count}")
print(f"   Messages in memory: {len(assistant.history)}")
print(f"{'─' * 50}")

print("""
🎯 WHAT YOU JUST SAW (built in ~50 lines of logic):
   ✅ Python fundamentals — lists, dicts, classes, loops
   ✅ Azure OpenAI — authentication, API calls
   ✅ System prompts — personality per category
   ✅ Multi-turn memory — it remembered your conversation
   ✅ Class-based agent — clean, reusable structure

💡 Now imagine: add a database, a web UI, more categories...
   You just built the foundation of a real AI product.

🚀 Go build yours!
""")
