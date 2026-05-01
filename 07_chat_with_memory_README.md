# Module 4: Chat Conversations with Message History

## Companion Reference for `04_azure_openai_chat.py`

### Overview

This module builds on the single API call from Module 3 by introducing two powerful concepts: **system prompts** that control the AI's personality and behavior, and **multi-turn conversations** that maintain chat history across multiple exchanges. You will also work through a practical example -- summarizing real meeting notes and extracting action items.

The critical lesson of this module: the AI has **no memory** between calls. You must send the entire conversation history every time.

**Duration:** ~8 minutes

---

### Prerequisites

- Completed Module 3 (`03_azure_openai_simple.py`) -- made a successful API call
- Credentials configured in `.env`
- Virtual environment activated with packages installed

---

### Concepts Covered

#### 1. Message Roles -- Deep Dive

In Module 1 you learned that messages have three roles. Now you will see each role in action:

| Role | Purpose | Analogy | Example |
|------|---------|---------|---------|
| `"system"` | Instructions for the AI -- sets personality, rules, and behavior | A job description given to a new employee | `"You are a professional Meeting Assistant. Be concise and use bullet points."` |
| `"user"` | What the human says -- your questions, requests, and input | The customer talking to the employee | `"Summarize these meeting notes."` |
| `"assistant"` | What the AI previously responded -- used to maintain history | The employee's previous answers | `"Here's the summary: ..."` |

**Key points:**
- The `"system"` message is set once, at the start of the conversation
- It is only visible to the AI, never shown to end users
- The `"assistant"` role is how you "remind" the AI what it previously said
- Without assistant messages in the history, the AI has no memory of prior turns

---

#### 2. System Prompts -- Shaping AI Behavior

A **system prompt** is the `"system"` role message that defines how the AI should behave. It is the single most powerful tool for controlling the AI's personality and output quality.

Here is the system prompt used in this module:

```python
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
```

**Anatomy of a good system prompt:**

1. **Identity** -- Who the AI is: `"You are a professional Meeting Assistant AI."`
2. **Responsibilities** -- What the AI should do: a list of specific tasks
3. **Style** -- How the AI should communicate: tone, format, behavior

**The same AI model behaves completely differently based on the system prompt.** Change the system prompt from "meeting assistant" to "pirate captain" and the same model will respond in pirate language.

---

#### 3. Multi-Turn Conversations with Manual History

This is the most important concept in this module.

**The key insight:** The AI has no memory between API calls. Each call is completely independent. To create the illusion of a conversation, **you** must send the entire message history with every request.

**How it works -- the growing message list:**

```
Call 1: [system, user1]                                         → assistant1
Call 2: [system, user1, assistant1, user2]                      → assistant2
Call 3: [system, user1, assistant1, user2, assistant2, user3]   → assistant3
```

Each call sends every previous message plus the new one. The AI reads the full list and responds based on all the context.

**The code pattern:**

```python
# Start the conversation
conversation = [
    {"role": "system", "content": "You are a helpful meeting assistant. Be concise."},
    {"role": "user", "content": "I have a project kickoff meeting tomorrow with 5 people."}
]

# First API call
response1 = client.chat.completions.create(
    model=deployment,
    messages=conversation,
    max_tokens=150
)
assistant_msg1 = response1.choices[0].message.content

# APPEND the assistant's response to the history
conversation.append({"role": "assistant", "content": assistant_msg1})

# APPEND the next user message
conversation.append({"role": "user", "content": "The meeting is about launching a new mobile app."})

# Second API call -- includes FULL history
response2 = client.chat.completions.create(
    model=deployment,
    messages=conversation,    # Now contains: system, user1, assistant1, user2
    max_tokens=200
)
```

**The `.append()` pattern is critical:** After each API response, you must:
1. Append the `"assistant"` response to the conversation list
2. Append the next `"user"` message
3. Send the entire list in the next API call

If you forget to append, the AI will not know what it previously said and the conversation will break.

---

#### 4. The `temperature` Parameter

This module introduces `temperature` as an API parameter:

```python
response = client.chat.completions.create(
    model=deployment,
    messages=messages,
    max_tokens=200,
    temperature=0.7    # Controls creativity
)
```

This was introduced as a float concept in Module 1. Here it is used in practice:

| Temperature | Best For |
|-------------|----------|
| 0.0 - 0.3 | Factual summaries, data extraction, consistent outputs |
| 0.4 - 0.7 | General conversation, balanced responses |
| 0.8 - 1.0 | Creative writing, brainstorming, varied responses |

For meeting summaries, a lower temperature (0.3-0.5) is typically better since you want consistent, accurate extraction of information.

---

#### 5. Practical Example -- Meeting Notes Summarization

The final part of this module demonstrates a real-world use case: feeding meeting notes to the AI and asking it to summarize them and extract action items.

**Input meeting notes:**

```
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
```

**The API call:**

```python
summary_request = [
    {"role": "system", "content": "You are a meeting assistant. Extract key information concisely."},
    {"role": "user", "content": f"Please summarize these meeting notes and list action items:\n\n{meeting_notes}"}
]

response = client.chat.completions.create(
    model=deployment,
    messages=summary_request,
    max_tokens=300
)
```

The AI will return a structured summary with bullet points and clearly listed action items with owners -- exactly what a Meeting Assistant should do.

---

#### 6. Authentication Note

This file uses **API key authentication** (line 34):

```python
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-10-21"
)
```

This is simpler than the Azure AD token-based authentication used in Module 3. Both methods are valid. Your organization may require one or the other. The rest of the code works identically regardless of which authentication method you use.

---

### Code Walkthrough

The file is organized into 4 parts:

| Part | What It Does |
|------|-------------|
| Part 1 | Explains the three message roles (`system`, `user`, `assistant`) with descriptions |
| Part 2 | Demonstrates a system prompt that gives the AI a "Meeting Assistant" personality, then makes a request |
| Part 3 | Builds a 3-turn conversation showing the `.append()` pattern for manual history management |
| Part 4 | Practical example: feeds real meeting notes and asks for a summary plus action items |

Run the file:

```bash
python 04_azure_openai_chat.py
```

You will see the three-turn conversation unfold, with the AI remembering context from earlier messages (because you are sending the full history each time). Then the meeting notes summary demonstrates a practical use case.

---

### Key Takeaways

1. **System prompt** -- set AI personality and behavior (done once at the start)
2. **User message** -- your questions and input
3. **Assistant message** -- AI's previous responses (included for history)
4. For multi-turn chat:
   - Store ALL messages in a list
   - Send the FULL list with each API call
   - Append new messages after each response
5. The AI doesn't remember anything -- **you** manage the history!
6. In the next module, agents will handle this memory problem automatically

---

### Common Mistakes and Troubleshooting

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Forgetting to append the assistant's response | The AI doesn't know what it just said -- conversation breaks | Always append `{"role": "assistant", "content": response_text}` after each call |
| Forgetting to append the next user message | The new question is never sent | Append `{"role": "user", "content": new_question}` before the next call |
| Conversation list growing too large | Token limit exceeded, or very expensive calls | For long conversations, consider summarizing older messages or removing them |
| System prompt too vague | AI gives generic, unhelpful responses | Be specific: define identity, responsibilities, and style |
| System prompt too restrictive | AI refuses reasonable requests | Find a balance -- give guidelines, not rigid rules |

---

### Try It Yourself

Replace the meeting notes with your own and run the file:

```python
your_notes = """
Your meeting notes here...
"""

response = client.chat.completions.create(
    model=deployment,
    messages=[
        {"role": "system", "content": "Summarize meeting notes and extract action items."},
        {"role": "user", "content": your_notes}
    ],
    max_tokens=300
)
print(response.choices[0].message.content)
```

Experiment ideas:
- Paste notes from a real meeting you attended
- Try different system prompts (e.g., "Extract only deadlines and dates")
- Change the `temperature` to 0.2 and then 0.9 and compare the summaries

---

### What's Next

In **Module 5 (05_meeting_assistant_agent.py)** you will build an AI Agent that handles conversation memory automatically using threads. No more manual `.append()` calls -- the agent remembers everything on its own. This is the final project and the "wow moment" of the session.
