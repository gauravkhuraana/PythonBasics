"""
================================================================
10_life_assistant.py — Your Personal Life Assistant 🌟
THE FLAGSHIP: Everything from this course in one program.
================================================================

🎯 GOAL:
   A menu-driven, persona-switching, memory-keeping AI assistant
   running entirely on your laptop via LM Studio.

This file ties together:
  ✅ Python fundamentals (lists, dicts, classes)         ← Video 3
  ✅ .env configuration                                   ← Video 4
  ✅ Local LLM (LM Studio + OpenAI SDK)                   ← Videos 5-6
  ✅ Multi-turn chat with memory                          ← Video 7
  ✅ Personas via system prompts                          ← NEW
  ✅ A class-based agent wrapper                          ← NEW

Prerequisites:
  - LM Studio running with a model loaded (Video 5)
  - .env has LOCAL_LLM_BASE_URL and LOCAL_LLM_MODEL

Run this file:  python 10_life_assistant.py
================================================================
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# ============================================================
# Setup — connect to your local LLM
# ============================================================
load_dotenv()

client = OpenAI(
    base_url=os.getenv("LOCAL_LLM_BASE_URL", "http://localhost:1234/v1"),
    api_key="lm-studio",  # local server ignores the value
)
model = os.getenv("LOCAL_LLM_MODEL", "local-model")


# ============================================================
# Persona library — same model, different experts
# ============================================================
categories = {
    "1": {
        "name": "🥗 Diet & Nutrition",
        "prompt": """You are a practical Indian diet and nutrition coach.
- Give advice based on Indian food (dal, roti, sabzi, rice, etc.)
- Suggest realistic meals for working professionals
- Include protein, fiber, and calorie awareness
- Keep it simple — no fancy superfoods, use what's in every Indian kitchen""",
    },
    "2": {
        "name": "💪 Fitness & Exercise",
        "prompt": """You are a no-nonsense fitness coach for busy professionals.
- Suggest workouts that fit in 20-30 minutes
- Include home workouts (no gym needed)
- Be practical: morning routines, desk stretches, walk goals
- Motivate without being preachy — facts over fluff""",
    },
    "3": {
        "name": "🤖 AI & Tech Learning",
        "prompt": """You are an AI learning mentor for software professionals.
- Recommend practical learning paths (not just theory)
- Focus on Python, LLMs, and prompt engineering
- Suggest weekend projects and hands-on labs
- Give honest career advice about AI skills that actually matter""",
    },
    "4": {
        "name": "🧘 Motivation & Mindset",
        "prompt": """You are a wise and warm motivational coach.
- Draw wisdom from Bhagavad Gita, Stoicism, and modern psychology
- Give practical mindset shifts, not generic "believe in yourself" advice
- Help with imposter syndrome, burnout, and career growth anxiety
- Keep it real — acknowledge struggles before offering solutions""",
    },
    "5": {
        "name": "💰 Personal Finance",
        "prompt": """You are a practical personal finance advisor for Indian professionals.
- Cover SIPs, mutual funds, PPF, NPS, tax saving (80C, 80D)
- Explain in simple terms — no jargon without explanation
- Help with budgeting, emergency funds, and salary negotiation
- Be honest about risks — no "get rich quick" nonsense""",
    },
    "6": {
        "name": "📚 Book & Learning Recommendations",
        "prompt": """You are a thoughtful book curator and learning guide.
- Recommend books based on what the person is going through
- Mix genres: self-help, tech, fiction, biography, philosophy
- Give a 2-line reason WHY each book matters right now
- Suggest podcasts, YouTube channels, and courses too""",
    },
    "7": {
        "name": "⏰ Productivity & Time Management",
        "prompt": """You are a productivity coach who respects work-life balance.
- Suggest realistic routines (not 4 AM wake-up cult)
- Help with meeting overload, focus time, and deep work
- Tools and techniques: Pomodoro, time-blocking, 2-minute rule
- Help say NO to things that don't matter""",
    },
}


# ============================================================
# The agent — wraps the chat loop, history, and stats
# ============================================================
class LifeAssistant:
    """A persona-driven assistant with conversation memory."""

    def __init__(self, client, model, system_prompt, category_name):
        self.client = client
        self.model = model
        self.category = category_name
        self.history = [{"role": "system", "content": system_prompt}]
        self.question_count = 0

    def chat(self, user_message):
        """Send a message, get a reply, remember both."""
        self.history.append({"role": "user", "content": user_message})
        self.question_count += 1

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=self.history,
            max_tokens=800,
            temperature=0.7,
        )
        reply = completion.choices[0].message.content
        if not reply:
            reply = "(The model returned an empty response — try a simpler question.)"

        self.history.append({"role": "assistant", "content": reply})
        return reply

    @property
    def message_count(self):
        return len(self.history) - 1  # exclude the system prompt


# ============================================================
# Farewell — a one-shot completion outside the main thread
# ============================================================
def get_farewell(client, model, category, question_count):
    """Generate a thoughtful sign-off using a fresh prompt."""
    farewell_prompt = f"""The user just finished a {category} conversation
({question_count} questions). Give them a farewell that includes:

1. One practical tip relevant to {category}.
2. An encouraging one-liner.
3. A light closing emoji.

Keep it under 80 words."""

    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": farewell_prompt}],
        max_tokens=300,
        temperature=0.8,
    )
    return completion.choices[0].message.content


# ============================================================
# Main flow
# ============================================================
def main():
    print("═" * 50)
    print("   🌟 YOUR PERSONAL LIFE ASSISTANT 🌟")
    print("   Built with Python + a local LLM")
    print("═" * 50)

    print("\nHow can I help you today?\n")
    for key, cat in categories.items():
        print(f"  {key}. {cat['name']}")

    choice = input("\nPick a number (1-7): ").strip()
    if choice not in categories:
        print("Invalid choice — defaulting to Motivation 🧘")
        choice = "4"

    selected = categories[choice]
    print(f"\n✅ Loading: {selected['name']}")
    print("─" * 50)
    print("Ask me anything! Type 'quit' to exit.\n")

    assistant = LifeAssistant(client, model, selected["prompt"], selected["name"])

    while True:
        try:
            user_input = input("👤 You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not user_input:
            continue
        if user_input.lower() in {"quit", "exit", "q"}:
            break

        try:
            reply = assistant.chat(user_input)
        except Exception as e:
            print(f"\n❌ {type(e).__name__}: {e}")
            print("   (Is LM Studio still running?)\n")
            continue

        print(f"\n🤖 Assistant: {reply}\n")

    # ----- Farewell + stats -----
    if assistant.question_count == 0:
        print("\n👋 Talk to you soon!")
        return

    print("\n" + "═" * 50)
    print("   🙏 BEFORE YOU GO...")
    print("═" * 50 + "\n")

    try:
        print(get_farewell(client, model, selected["name"], assistant.question_count))
    except Exception as e:
        print(f"(farewell skipped — {e})")

    print("\n" + "─" * 50)
    print("📊 Session Stats")
    print(f"   Category:           {selected['name']}")
    print(f"   Questions asked:    {assistant.question_count}")
    print(f"   Messages in memory: {assistant.message_count}")
    print("─" * 50)

    print("""
🎯 What you just used:
   ✅ Python — lists, dicts, classes, loops
   ✅ A local LLM via the OpenAI SDK (no cloud!)
   ✅ Personas via system prompts
   ✅ Multi-turn memory in a class wrapper

🚀 Next up: Video 9 — supercharge your edits with GitHub Copilot.
""")


if __name__ == "__main__":
    main()
