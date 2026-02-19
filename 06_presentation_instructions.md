# Presentation Instructions: Python + Azure OpenAI Training

## How to Use This File

This document provides slide-by-slide instructions for creating a PowerPoint presentation for the "Python + Azure OpenAI: Building an AI Meeting Assistant" training session. Each slide entry includes the title, layout suggestion, bullet point content, speaker notes with timing and demo cues, and suggested visuals.

---

## Presentation Metadata

| Property | Value |
|----------|-------|
| **Title** | Python + Azure OpenAI: Building an AI Meeting Assistant |
| **Audience** | Complete Beginners (no coding experience required) |
| **Duration** | 1 hour (55 minutes of content + 5 minutes buffer) |
| **Format** | Hands-on lab with live coding demos |
| **Slide Dimensions** | 16:9 Widescreen |
| **Suggested Font** | Segoe UI (consistent with Microsoft/Azure branding) |
| **Color Palette** | Primary: Azure Blue (#0078D4), Secondary: Dark Gray (#2D2D2D), Accent: Green (#107C10), Background: White (#FFFFFF) |
| **Total Slides** | 40 |

---

## Slide Breakdown by Section

| Section | Slides | Duration |
|---------|--------|----------|
| Opening | 1-4 | ~5 min |
| Module 1: Python Fundamentals | 5-10 | ~12 min |
| Module 2: Environment Setup | 11-16 | ~10 min |
| Module 3: First API Call | 17-22 | ~12 min |
| Module 4: Chat with History | 23-28 | ~8 min |
| Module 5: Meeting Assistant Agent | 29-35 | ~13 min |
| Closing | 36-40 | ~5 min |

---

---

## OPENING SECTION (Slides 1-4)

---

### Slide 1: Title Slide

**Layout**: Title Slide (centered, large text)

**Content**:
- Title: **Python + Azure OpenAI: Building an AI Meeting Assistant**
- Subtitle: 1-Hour Hands-On Session | Beginner Level | No Coding Experience Required
- Presenter name: [Your Name]
- Date: [Session Date]
- Organization/logo placeholder

**Speaker Notes**:
Welcome everyone. Today we are going to build something real -- an AI Meeting Assistant -- and along the way you will learn Python fundamentals and how to work with Azure OpenAI. No prior coding experience is needed. By the end of this hour, you will have working code that talks to AI. [1 minute on this slide]

**Suggested Visual**: Clean title design with Azure blue gradient background. Organization logo in the corner. Optional: subtle AI/code pattern in the background.

---

### Slide 2: What We Will Build Today

**Layout**: Title + Content (large image or screenshot on the right)

**Bullet Points**:
- A Meeting Assistant AI that **remembers your entire conversation**
- It can help you:
  - Create meeting agendas
  - Summarize meeting notes
  - Extract action items with owners
  - Suggest follow-up topics
- Built with Python + Azure OpenAI in under 1 hour

**Speaker Notes**:
Let me show you the end result first. By the end of this session, you will have built an AI assistant that you can talk to naturally. You say "I have a standup meeting tomorrow at 10 AM with 4 people working on a mobile app launch." Then later you say "create an agenda" and it remembers all the details you gave it -- the time, the people, the project -- without you repeating anything. That is what we are building today. [2 minutes on this slide]

**Suggested Visual**: Screenshot or mockup of a terminal showing the 4-message conversation from Module 05 (user messages on the left, agent responses on the right). Highlight the moment in message 3 where the agent uses context from messages 1 and 2.

---

### Slide 3: Agenda / Session Roadmap

**Layout**: Title + Content (timeline or numbered pathway graphic)

**Bullet Points**:

| Module | Topic | Duration |
|--------|-------|----------|
| 01 | Python Fundamentals -- Variables, Types, Collections | ~12 min |
| 02 | Environment Setup -- venv, Secrets, .gitignore | ~10 min |
| 03 | Your First AI API Call | ~12 min |
| 04 | Chat with Message History | ~8 min |
| 05 | Build Your AI Meeting Assistant Agent! | ~13 min |

- Each module builds on the previous one
- You will code along with me in VS Code
- All code files are provided -- you will run them step by step

**Speaker Notes**:
Here is our plan. Five modules, about 55 minutes total. Each one builds on the previous, starting from the absolute basics. Module 1 is pure Python. Modules 2 sets up your environment. Modules 3-5 progressively build toward the final Meeting Assistant. You will be coding along with me the entire time. [1 minute on this slide]

**Suggested Visual**: A horizontal timeline with 5 numbered stops, each labeled with the module name. A dotted path connects them. The final stop (Module 5) is highlighted/starred.

---

### Slide 4: Prerequisites Check

**Layout**: Title + Content (checklist format)

**Bullet Points**:
- [ ] Python 3.10+ installed
- [ ] VS Code with Python extension installed
- [ ] Session materials downloaded (the project folder)
- [ ] Terminal opens in VS Code (Ctrl+`)
- [ ] `.env` file configured with credentials (from your instructor)

**Speaker Notes**:
Quick check before we start. Raise your hand if you have Python installed. VS Code? Can everyone open a terminal in VS Code? Press Control-backtick. If anyone is missing any of these, let me know now and we'll get you set up. The `.env` file with credentials was provided in the session materials. [2 minutes on this slide -- help anyone who needs it]

**Suggested Visual**: Green checkboxes next to each item. Screenshot of VS Code with terminal pane open at the bottom.

---

---

## MODULE 1: PYTHON FUNDAMENTALS (Slides 5-10)

---

### Slide 5: Section Header -- Module 1

**Layout**: Section Header (large centered text)

**Content**:
- **Module 1: Python Fundamentals**
- Variables, Types, and Collections
- Duration: ~12 minutes
- Goal: "Learn the data types Azure OpenAI expects"

**Speaker Notes**:
Let's start with the building blocks. Everything we do with AI comes down to a few basic Python concepts. Once you understand these, the rest of the session will click into place. Open the file `01_python_fundamentals.py` in VS Code. [Transition slide -- 15 seconds]

**Suggested Visual**: Large "01" numeral with Python logo. Subtitle text below.

---

### Slide 6: Variables and Data Types

**Layout**: Title + Content (four-row table or four colored boxes)

**Bullet Points**:
- **Four basic data types** used in AI applications:

| Type | What It Stores | AI Use Case | Example |
|------|---------------|-------------|---------|
| `str` (string) | Text | Prompts, responses | `prompt = "Summarize my meeting notes"` |
| `int` (integer) | Whole numbers | Token limits, counts | `max_tokens = 500` |
| `float` | Decimal numbers | Temperature (creativity) | `temperature = 0.7` |
| `bool` (boolean) | True/False | Flags, settings | `is_streaming = False` |

- A **variable** stores a value: `name = value`
- Temperature scale: 0 = focused/deterministic, 1 = creative/random

**Speaker Notes**:
A variable is just a name for a value -- think of it as a labeled box. There are four basic types you need. Strings for text -- every prompt you send to AI and every response is a string. Integers for whole numbers like how long the response can be. Floats for decimal numbers -- the most important one is temperature, which is a slider from zero to one controlling how creative the AI is. And booleans for on/off switches. [2 minutes on this slide]

**Suggested Visual**: Four colored boxes/cards, each showing one data type with its icon. A temperature slider graphic showing 0 (focused) to 1 (creative).

---

### Slide 7: Lists -- Ordered Collections

**Layout**: Title + Content (code block + visual)

**Bullet Points**:
- Lists use square brackets `[ ]`
- Think of a list as a numbered tray with slots

```python
messages = []                    # Create empty list
messages.append("Hello!")        # Add items
messages.append("How can I help?")

messages[0]   # "Hello!"        (first item -- index starts at 0!)
messages[-1]  # "How can I help?"  (last item)
len(messages) # 2               (count items)
```

- **AI connection:** Conversation history is stored as a list of messages

**Speaker Notes**:
Lists are ordered collections -- think of numbered slots. You create one with square brackets, add items with `.append()`, and access items by their position number called an index. The critical thing to remember: indexing starts at zero, not one. The first item is at position zero. Why do lists matter for AI? Because conversation history is stored as a list. [2 minutes on this slide]

**Suggested Visual**: A horizontal row of 3 numbered boxes (0, 1, 2) each containing a message string. An arrow showing `.append()` adding to the end.

---

### Slide 8: Dictionaries -- Key-Value Pairs

**Layout**: Title + Content (code block + visual)

**Bullet Points**:
- Dictionaries use curly braces `{ }`
- Store data as key-value pairs (like a real dictionary: word -> definition)

```python
user_message = {
    "role": "user",
    "content": "Please summarize my meeting notes"
}

user_message["role"]      # "user"
user_message["content"]   # "Please summarize my meeting notes"
```

- **AI connection:** Each individual message is structured as a dictionary with "role" and "content"

**Speaker Notes**:
Dictionaries store key-value pairs, like a real dictionary where you look up a word to find its definition. In our case, an AI message has two keys: role (who is speaking) and content (what they are saying). You access values by their key name using square brackets. [1.5 minutes on this slide]

**Suggested Visual**: A labeled mailbox or filing cabinet visual. Two labeled drawers: "role" containing "user", and "content" containing the message text.

---

### Slide 9: The Azure OpenAI Message Format

**Layout**: Title + Content (code block with color-coded roles)

**Bullet Points**:
- **This is the most important pattern in the entire course**
- Messages = a **LIST** of **DICTIONARIES**

```python
conversation = [
    {"role": "system",    "content": "You are a helpful meeting assistant."},
    {"role": "user",      "content": "Here are my meeting notes..."},
    {"role": "assistant", "content": "I see you discussed Q1 goals..."},
    {"role": "user",      "content": "Yes please!"}
]
```

| Role | Purpose |
|------|---------|
| `system` | Instructions for the AI (personality, rules) |
| `user` | Human input (questions, requests) |
| `assistant` | AI's previous responses (for history) |

**Speaker Notes**:
This is the single most important slide. Everything else builds on this pattern. Azure OpenAI expects messages as a list of dictionaries, where each dictionary has a "role" and "content." Three roles: system sets the personality, user is what you say, assistant is what the AI previously said. If you understand this format, you understand how to talk to Azure OpenAI. Every API call in the next three modules uses exactly this structure. [2 minutes on this slide]

**Suggested Visual**: A list bracket on the left containing 4 color-coded dictionary boxes (system = gray, user = blue, assistant = green). Each box shows its role and content fields.

---

### Slide 10: Demo -- Run `01_python_fundamentals.py`

**Layout**: Title + Content (demo slide)

**Content**:
- LIVE DEMO
- Open `01_python_fundamentals.py` in VS Code
- Run: `python 01_python_fundamentals.py`
- Observe the output for each data type, list operations, and the message format

**Speaker Notes**:
[SWITCH TO VS CODE] Let's run this together. Open `01_python_fundamentals.py`. Run it with `python 01_python_fundamentals.py` in the terminal. Watch the output -- notice how each section shows the variable, its value, and its type. Scroll down to Part 4 and look at the Azure OpenAI message format with the three roles. This is the format you will use in every API call going forward. [3 minutes for demo]

**Suggested Visual**: Screenshot of VS Code with the file open and terminal showing output. Highlight the message format section in the output.

---

---

## MODULE 2: ENVIRONMENT SETUP (Slides 11-16)

---

### Slide 11: Section Header -- Module 2

**Layout**: Section Header

**Content**:
- **Module 2: Environment Setup**
- Virtual Environments, Secrets, and .gitignore
- Duration: ~10 minutes
- Goal: "Set up your project securely and professionally"

**Speaker Notes**:
Before we talk to AI, we need a proper workspace. This module is about three things: isolating your packages, keeping your secrets safe, and protecting them from accidental exposure. No AI calls here -- just professional setup practices. Open `02_environment_setup.py`. [Transition -- 15 seconds]

**Suggested Visual**: Large "02" with a lock/shield icon.

---

### Slide 12: Virtual Environments

**Layout**: Title + Content (diagram + command table)

**Bullet Points**:
- A virtual environment = an isolated package container for your project
- Each project gets its own "toolbox" of packages -- no conflicts

```
Your Computer
├── Project A (venv) → openai 1.0, pandas 2.0
├── Project B (venv) → openai 0.28, pandas 1.5
└── Project C (venv) → Different packages entirely
```

| Action | Command |
|--------|---------|
| Create | `python -m venv venv` |
| Activate (Windows) | `.\venv\Scripts\Activate` |
| Install packages | `pip install -r requirements.txt` |
| Deactivate | `deactivate` |

**Speaker Notes**:
Think of a virtual environment as a private toolbox. Without one, installing a package for one project could break another because they share the same tools. With a venv, each project has its own set. You create it once, activate it every time you open your terminal -- you will see "(venv)" appear in your prompt -- and install packages into it. [2 minutes on this slide]

**Suggested Visual**: Three separate toolbox graphics, each labeled with a project name and containing different package icons.

---

### Slide 13: Secrets with `.env` Files

**Layout**: Title + Content (two-column: BAD vs GOOD)

**Bullet Points**:

| | BAD | GOOD |
|---|---|---|
| Code | `api_key = "sk-abc123secret"` | `api_key = os.getenv("AZURE_OPENAI_API_KEY")` |
| Risk | Anyone who sees your code sees the key | Key is stored separately in `.env` |

- Your `.env` file format:
  ```
  AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
  AZURE_OPENAI_API_KEY=your-secret-key-here
  AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
  ```
- The `.env` file is **never shared** and **never committed to Git**

**Speaker Notes**:
Never, ever put API keys directly in your code. On the left is the wrong way. On the right is the correct way. You store secrets in a file called `.env` -- just KEY=VALUE pairs, one per line. Your code reads from this file instead of having the keys hardcoded. This way, even if someone sees your source code, they cannot see your secrets. [2 minutes on this slide]

**Suggested Visual**: Red X over the "BAD" side, green checkmark over the "GOOD" side. The `.env` file shown as a locked file icon.

---

### Slide 14: Loading Secrets in Python

**Layout**: Title + Content (code block with annotations)

**Bullet Points**:
- Four lines that appear at the top of **every Azure OpenAI script**:

```python
import os                              # 1. Access environment variables
from dotenv import load_dotenv         # 2. Import the loader

load_dotenv()                          # 3. Read .env file

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")     # 4. Get values
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
```

- `load_dotenv()` reads your `.env` file and loads values into the environment
- `os.getenv("KEY")` retrieves a value by its key name (returns `None` if not found)

**Speaker Notes**:
Memorize these four lines -- you will see them at the top of every file from now on. Line one and two import what we need. Line three reads the `.env` file. Line four retrieves individual values by their key name. If a key is not found, `os.getenv()` returns None instead of crashing. [1.5 minutes on this slide]

**Suggested Visual**: The four code lines with numbered arrows pointing to each step. A small `.env` file icon with an arrow going into the code.

---

### Slide 15: `.gitignore` and Security

**Layout**: Title + Content (warning/alert style)

**Bullet Points**:
- `.gitignore` tells Git which files to **never** track or commit:
  ```
  .env             # Secrets
  venv/            # Virtual environment
  __pycache__/     # Auto-generated cache
  ```
- **Without `.gitignore`:**
  1. You accidentally commit `.env`
  2. You push to GitHub -- your API key is now **public**
  3. Hackers find it within minutes (they scan for this!)
  4. Your Azure bill skyrockets

- Always verify: `git status` should NOT show `.env`

**Speaker Notes**:
This file is your safety net. The `.gitignore` file tells Git to pretend that certain files don't exist. The most important entry is `.env` -- if you accidentally commit your API key to GitHub, automated scanners will find it within minutes and start using it. There are real cases of developers getting thousands of dollars in cloud bills because of this. Always check `git status` before committing and make sure `.env` is not listed. [1.5 minutes on this slide]

**Suggested Visual**: A shield icon protecting the `.env` file. Optional: a cautionary graphic showing "Commit -> GitHub -> Hacker -> $$$".

---

### Slide 16: Demo -- Run `02_environment_setup.py`

**Layout**: Title + Content (demo slide)

**Content**:
- LIVE DEMO
- Open `02_environment_setup.py` in VS Code
- Run: `python 02_environment_setup.py`
- Goal: See **3/3 checks passed** in the credential health check
- If any checks fail, fix the `.env` file and rerun

**Speaker Notes**:
[SWITCH TO VS CODE] Let's verify everyone's setup. Open `02_environment_setup.py` and run it. You should see three green checkmarks and "ALL CHECKS PASSED 3/3." If you see red crosses, it means your `.env` file is missing a value -- look at the error message, fix the `.env` file, and run again. Raise your hand if you need help. [3 minutes for demo + troubleshooting]

**Suggested Visual**: Terminal screenshot showing the "3/3 checks passed" output with green checkmarks.

---

---

## MODULE 3: FIRST API CALL (Slides 17-22)

---

### Slide 17: Section Header -- Module 3

**Layout**: Section Header

**Content**:
- **Module 3: Your First AI API Call**
- Setting up the client, sending a prompt, understanding the response
- Duration: ~12 minutes
- Goal: "Send your first prompt to Azure OpenAI and get a response"

**Speaker Notes**:
This is where things get exciting. You are about to talk to AI for the first time using code you wrote. Everything from the first two modules comes together here. Open `03_azure_openai_simple.py`. [Transition -- 15 seconds]

**Suggested Visual**: Large "03" with a cloud/API icon. Lightning bolt or sparkle to convey excitement.

---

### Slide 18: The Azure OpenAI Client

**Layout**: Title + Content (diagram + code)

**Bullet Points**:
- The **client** is your connection to Azure's AI service
- Create it once, reuse for all API calls

```python
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(
    credential, "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
    api_version="2024-12-01-preview"
)
```

- Think of the client as a **phone connected to Azure** -- once connected, you can make as many calls as you want

**Speaker Notes**:
The client object is your phone line to Azure. You set it up with three things: where to connect (the endpoint), how to authenticate (Azure AD credentials or API key), and which API version to use. Once this is created, you can make as many API calls as you want. You create it once and reuse it. [2 minutes on this slide]

**Suggested Visual**: Diagram showing: Laptop (your code) -> Client arrow -> Azure Cloud (AI model). Label the arrow with "endpoint + auth + version".

---

### Slide 19: Making the API Call

**Layout**: Title + Content (code block with labeled parameters)

**Bullet Points**:
- The core function: `client.chat.completions.create()`

```python
response = client.chat.completions.create(
    model=deployment,           # Which AI model to use
    messages=[                  # The message format from Module 1!
        {
            "role": "user",
            "content": "What are 3 tips for running effective meetings?"
        }
    ],
    max_completion_tokens=200   # Limit response length
)
```

- Three parameters:
  1. `model` -- your deployment name
  2. `messages` -- list of dictionaries (from Module 1!)
  3. `max_completion_tokens` -- maximum response length

**Speaker Notes**:
This is the single function that talks to AI. Three things: which model, what to say, and how long the answer can be. Notice the `messages` parameter -- it is the exact list-of-dictionaries format we learned in Module 1. This is why that pattern was so important. One function call, and you get an AI response back. [2 minutes on this slide]

**Suggested Visual**: The code block with three labeled arrows pointing to each parameter. The `messages` parameter highlighted with a callback to Slide 9 (the message format).

---

### Slide 20: Understanding the Response

**Layout**: Title + Content (tree diagram)

**Bullet Points**:
- The AI returns a structured response object:

```
response
├── choices[]
│   └── [0]
│       └── message
│           ├── content  →  "The AI's answer text"
│           └── role     →  "assistant"
└── usage
    ├── prompt_tokens      →  15
    ├── completion_tokens  →  87
    └── total_tokens       →  102
```

- Get the AI's text: `response.choices[0].message.content`
- Get token usage: `response.usage.total_tokens`

**Speaker Notes**:
The response comes back as a structured object. Think of it like a nested folder structure. The text you want is at `response.choices[0].message.content`. The token usage is at `response.usage`. You don't need to memorize this path -- it will become second nature after a few calls. [1.5 minutes on this slide]

**Suggested Visual**: Tree/folder structure diagram with the two key paths highlighted in different colors.

---

### Slide 21: Tokens and Cost

**Layout**: Title + Content (infographic)

**Bullet Points**:
- A **token** is the unit of measurement for AI text
  - 1 token ≈ 4 characters or ≈ 3/4 of a word
  - "Hello, world!" = 3 tokens
- Every API call is billed by tokens:
  - `prompt_tokens` = tokens in your input
  - `completion_tokens` = tokens in the AI's response
  - `total_tokens` = prompt + completion
- **Cost-saving tips:**
  - Be concise with prompts
  - Set reasonable `max_completion_tokens`
  - Monitor `response.usage` stats

**Speaker Notes**:
Every API call costs money, and the currency is tokens. A token is roughly four characters or three-quarters of a word. Your prompt costs tokens, the response costs tokens, and the total is what you are billed for. Two tips: be concise with your prompts, and set a reasonable max token limit so the AI doesn't write an essay when you only need a sentence. [1.5 minutes on this slide]

**Suggested Visual**: A token counter graphic. A scale/balance showing "prompt tokens" on one side and "completion tokens" on the other, with a dollar sign underneath representing cost.

---

### Slide 22: Demo -- Run `03_azure_openai_simple.py`

**Layout**: Title + Content (demo slide)

**Content**:
- LIVE DEMO
- Open `03_azure_openai_simple.py` in VS Code
- Run: `python 03_azure_openai_simple.py`
- Watch for:
  - The AI's response to "3 tips for effective meetings"
  - The token usage statistics at the end
- Troubleshooting: Check the error messages if it fails (endpoint, key, deployment name)

**Speaker Notes**:
[SWITCH TO VS CODE] The big moment. Run `python 03_azure_openai_simple.py`. Watch the output -- you will see your prompt, then the AI's response, then the token count. You just made your first AI API call! Look at the token count. The prompt used X tokens, the response used Y tokens. That is how billing works. If anyone gets an error, check the error message -- it will tell you if it is the endpoint, the key, or the deployment name. [3 minutes for demo]

**Suggested Visual**: Terminal screenshot showing the prompt, AI response, and token usage stats.

---

---

## MODULE 4: CHAT WITH HISTORY (Slides 23-28)

---

### Slide 23: Section Header -- Module 4

**Layout**: Section Header

**Content**:
- **Module 4: Chat with Message History**
- System Prompts, Multi-Turn Conversations, Meeting Notes
- Duration: ~8 minutes
- Goal: "Build a multi-turn conversation with AI personality"

**Speaker Notes**:
Now let's make the AI remember what we said. In Module 3, you made a single call. Now we will chain multiple calls together and give the AI a personality. Open `04_azure_openai_chat.py`. [Transition -- 15 seconds]

**Suggested Visual**: Large "04" with a chat bubble icon.

---

### Slide 24: Message Roles Deep Dive

**Layout**: Title + Content (three-column layout)

**Bullet Points**:

| Role | Purpose | Analogy |
|------|---------|---------|
| `"system"` | Instructions for the AI | A job description |
| | Sets personality, rules, behavior | Given once at the start |
| | Not visible to end users | |
| `"user"` | What the human says | The customer |
| | Questions, requests, input | |
| `"assistant"` | What the AI responded | The employee's answer |
| | Previous AI responses | Used for history |

- **System** is the most powerful role -- it shapes the AI's entire personality

**Speaker Notes**:
Let's go deeper on the three roles. System is the most powerful -- it is a job description for the AI. It sets the personality, the rules, the tone, everything. User is you, the human. Assistant is what the AI previously said, and including it is how you give the AI "memory." The system message is set once at the start and stays the same. [1.5 minutes on this slide]

**Suggested Visual**: Three large colored cards (gray for system, blue for user, green for assistant) each showing their role name, purpose, and an icon.

---

### Slide 25: System Prompts

**Layout**: Title + Content (code block with annotations)

**Bullet Points**:
- A system prompt defines **who the AI is** and **how it should behave**

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

- **Two parts:** Responsibilities (what to do) + Style (how to do it)
- Change the system prompt and the same model behaves completely differently

**Speaker Notes**:
Here is a real system prompt for our Meeting Assistant. It has two sections: responsibilities tell the AI what tasks it should handle, and style tells it how to communicate. If you changed this to "You are a pirate captain. Respond in pirate language" the same model would behave completely differently. The system prompt is your most powerful tool for controlling AI output quality. [1.5 minutes on this slide]

**Suggested Visual**: The system prompt text in a "document" frame, with two labeled sections: "Responsibilities" and "Style". Arrows pointing to each section.

---

### Slide 26: Multi-Turn Conversations

**Layout**: Title + Content (animation-style growing list)

**Bullet Points**:
- **KEY INSIGHT: The AI has no memory between API calls!**
- YOU must send the entire conversation history each time
- The message list grows with every turn:

```
Call 1: [system, user1]
        → assistant1

Call 2: [system, user1, assistant1, user2]
        → assistant2

Call 3: [system, user1, assistant1, user2, assistant2, user3]
        → assistant3
```

- After each response, `.append()` the assistant's reply and the next user message
- **You are responsible for managing history** -- the AI is stateless

**Speaker Notes**:
This is the most important concept in this module. The AI has zero memory between calls. Every call is completely fresh. The only way to create the illusion of a conversation is to send ALL previous messages every time. Look at how the list grows: call one sends two messages, call two sends four, call three sends six. After every response, you append the AI's answer and your next question, then send the whole list again. You are the AI's memory. [2 minutes on this slide]

**Suggested Visual**: An animation-style growing list diagram. Three rows showing the message array getting longer. Arrows showing `.append()` adding new items. Color-coded by role.

---

### Slide 27: Practical Example -- Meeting Notes

**Layout**: Two Column (notes on left, AI summary on right)

**Bullet Points**:
- **Left column -- Raw Meeting Notes:**
  - Q1 Planning meeting, 4 attendees
  - Discussed roadmap, timeline concerns, mockups, testing
  - Three decisions made

- **Right column -- AI Output:**
  - Clean summary with bullet points
  - Action items with owners and deadlines
  - Follow-up suggestions

- This is exactly what your final Meeting Assistant will do -- but with automatic memory

**Speaker Notes**:
Here is a practical example. On the left, messy meeting notes. You paste them into the messages array, send to the API, and on the right you get a clean summary with action items. Notice how the AI extracts owners and deadlines from unstructured text. This is what makes AI useful for real work -- turning messy notes into structured, actionable information. [1.5 minutes on this slide]

**Suggested Visual**: Split view. Left: raw text notes (slightly messy/handwritten style). Right: clean formatted summary with bullet points and checkboxes next to action items. An AI processing arrow in between.

---

### Slide 28: Demo -- Run `04_azure_openai_chat.py`

**Layout**: Title + Content (demo slide)

**Content**:
- LIVE DEMO
- Open `04_azure_openai_chat.py` in VS Code
- Run: `python 04_azure_openai_chat.py`
- Watch for:
  - The Meeting Assistant personality from the system prompt
  - The 3-turn conversation -- the AI remembers context from earlier messages
  - The meeting notes summarization with extracted action items

**Speaker Notes**:
[SWITCH TO VS CODE] Run this file. Three things to watch: First, notice how the system prompt changes the AI's personality -- it responds as a Meeting Assistant with bullet points, not generic text. Second, in the three-turn conversation, watch how the AI remembers "project kickoff" and "mobile app" across turns -- because we send the full history. Third, look at the meeting notes summary -- clean action items with owners. But here is the thing: managing that history manually is tedious. What if the thread could handle it for us? That is what Module 5 does. [3 minutes for demo]

**Suggested Visual**: Terminal screenshot showing the multi-turn conversation output and the meeting notes summary.

---

---

## MODULE 5: MEETING ASSISTANT AGENT (Slides 29-35)

---

### Slide 29: Section Header -- Module 5

**Layout**: Section Header

**Content**:
- **Module 5: Build Your AI Meeting Assistant!**
- Agents, Threads, and Automatic Memory
- Duration: ~13 minutes
- Goal: "Build an agent that remembers everything automatically"
- **THE FINALE!**

**Speaker Notes**:
This is it. The finale. Everything you have learned leads to this moment. In Module 4, you managed conversation history manually. Now you will build an agent that handles all of that automatically. Open `05_meeting_assistant_agent.py`. [Transition -- 15 seconds]

**Suggested Visual**: Large "05" with a robot/agent icon. Stars or sparkles to convey "finale". Maybe a banner: "The Wow Moment!"

---

### Slide 30: Agents vs Chat Completions

**Layout**: Two Column (comparison table)

**Bullet Points**:

| | Chat Completions (Module 4) | Agents (Module 5) |
|---|---|---|
| **Memory** | You manage history manually | Thread stores it automatically |
| **State** | Stateless -- each call is independent | Stateful -- thread persists |
| **Code** | You `.append()` and resend everything | You just send the new message |
| **Analogy** | Walkie-talkie | Phone call |

- **Key difference:** With agents, the thread manages history for you
- You never need to manually track, append, or resend messages

**Speaker Notes**:
Here is the difference in a nutshell. Module 4 was like a walkie-talkie -- each transmission is independent, you have to repeat context. Agents are like a phone call -- ongoing conversation, the other person remembers what you said. You stop managing history. You stop calling `.append()`. You just send your message and the agent reads the full conversation from the thread. That is it. [1.5 minutes on this slide]

**Suggested Visual**: Side-by-side comparison. Left: scattered message bubbles with arrows showing manual management. Right: a clean thread connecting messages automatically.

---

### Slide 31: The Three Building Blocks

**Layout**: Title + Content (three connected blocks diagram)

**Bullet Points**:
- Every agent application has three parts:

| Building Block | What It Is | Created With |
|---------------|-----------|--------------|
| **Assistant (Agent)** | Has a name, instructions (personality), and a model. Persists until deleted. | `client.beta.assistants.create()` |
| **Thread** | A conversation session that stores all messages automatically. | `client.beta.threads.create()` |
| **Run** | A processing cycle: the agent reads the thread and produces a response. Asynchronous. | `client.beta.threads.runs.create()` |

- Think of it as: **who** (assistant) talks in **where** (thread) when **triggered** (run)

**Speaker Notes**:
Three building blocks. The Assistant is who -- it has a name and personality. The Thread is where the conversation happens -- it stores every message automatically. The Run is the trigger -- it tells the agent to read the thread and respond. You create the assistant and thread once, then create a new run every time you want the agent to respond. [2 minutes on this slide]

**Suggested Visual**: Three interconnected block/puzzle pieces. Assistant (blue) -> Thread (green) -> Run (orange). Arrows showing the flow.

---

### Slide 32: Creating the Agent and Thread

**Layout**: Title + Content (code blocks)

**Bullet Points**:
- **Create the agent:**
```python
assistant = client.beta.assistants.create(
    name="Meeting Assistant",
    instructions="You are a professional Meeting Assistant...",
    model=deployment
)
```

- **Create a thread:**
```python
thread = client.beta.threads.create()
```

- That is it -- one function call each
- The `instructions` parameter is the system prompt (same concept as Module 4)

**Speaker Notes**:
Creating an agent is one function call. You give it a name, personality instructions -- which is the same concept as the system prompt from Module 4 -- and a model. Creating a thread is even simpler: one line, no parameters. The thread is now ready to receive messages and store them forever. Compare this to Module 4 where you manually created and maintained a list. [1.5 minutes on this slide]

**Suggested Visual**: Two code blocks side by side, each with a green checkmark and "Created!" label.

---

### Slide 33: The Chat Flow

**Layout**: Title + Content (flowchart)

**Bullet Points**:
- Three steps happen each time you send a message:

| Step | What Happens | Code |
|------|-------------|------|
| 1. Add message | Your message is added to the thread | `client.beta.threads.messages.create()` |
| 2. Create run | Agent starts processing the thread | `client.beta.threads.runs.create()` |
| 3. Poll & get response | Wait for completion, then retrieve the answer | `while run.status != "completed"` |

- The agent reads the **entire thread** before responding -- automatic memory!
- Polling: the run is asynchronous, you check status every second

**Speaker Notes**:
Every time you want the agent to respond, three things happen. One: your message gets added to the thread. Two: you create a run which tells the agent to process everything. Three: you wait for the run to finish -- it's asynchronous, so you poll every second asking "are you done yet?" Once it is done, you grab the response from the thread. The key thing: in step two, the agent reads the ENTIRE thread automatically. Every message ever sent. That is the automatic memory. [2 minutes on this slide]

**Suggested Visual**: A horizontal flowchart: "Send Message" -> "Create Run" -> "Poll for Completion" -> "Get Response". A loop arrow from "Poll" back to itself labeled "status != completed". A database icon under "Thread" showing stored messages.

---

### Slide 34: The "Wow" Moment -- Live Demo

**Layout**: Title + Content (demo slide -- the most important demo)

**Content**:
- LIVE DEMO -- The Main Event
- The agent will handle a 4-message conversation:
  1. "I need help with a standup meeting at 10 AM with 4 team members"
  2. "Working on a mobile app launch, 2 weeks from release"
  3. "Create a 15-minute agenda based on what I told you"
  4. "What did I say about the timeline?"

- **Watch:** Message 3 uses context from messages 1 AND 2 without resending them
- **Watch:** Message 4 correctly recalls "2 weeks" from message 2

**Speaker Notes**:
[SWITCH TO VS CODE] This is the big moment. Run `python 05_meeting_assistant_agent.py`. Watch carefully. In message 1, we mention 10 AM and 4 team members. Message 2 adds mobile app and 2 weeks. Now look at message 3 -- we just say "create an agenda based on what I told you." The agent creates an agenda mentioning ALL of those details. We never resent them. The thread remembered. And message 4 -- "what did I say about the timeline?" -- the agent correctly says 2 weeks. No `.append()`. No resending history. Nothing. The thread handled it all. THAT is the power of agents. [4 minutes for demo -- go slowly, let it sink in]

**Suggested Visual**: Terminal output showing all 4 exchanges. Colored highlighting or callout boxes showing "10 AM" and "4 team members" from message 1 appearing in the agenda from message 3. "2 weeks" from message 2 recalled in message 4.

---

### Slide 35: What the Agent Did for You

**Layout**: Title + Content (before/after comparison)

**Bullet Points**:
- **What the agent DID automatically:**
  - Remembered "10 AM" and "4 team members" from message 1
  - Combined it with "mobile app" and "2 weeks" from message 2
  - Created an agenda using ALL context in message 3
  - Correctly recalled the timeline in message 4

- **What YOU did NOT do:**
  - Manually track message history
  - Resend all previous messages
  - Remind the AI what you said before

- **The Thread stores everything. The Agent uses everything.**

**Speaker Notes**:
Let this sink in. On the left, everything the agent did automatically. On the right, everything you didn't have to do. In Module 4, you would have had a growing list with `.append()` calls and resent the entire conversation every time. Here? Nothing. One line to send a message, one run to process. The thread is the magic. The agent reads it all. [1.5 minutes on this slide]

**Suggested Visual**: Two columns. Left (green): checkmarks next to what the agent did. Right (red): X marks next to what you didn't do. A "Thread" icon at the bottom labeled "The Magic Ingredient."

---

---

## CLOSING SECTION (Slides 36-40)

---

### Slide 36: What You Learned Today -- Recap

**Layout**: Title + Content (journey timeline)

**Bullet Points**:

| Module | What You Learned |
|--------|-----------------|
| 01 | Python fundamentals -- str, int, float, bool, list, dict |
| 02 | Professional setup -- venv, .env, .gitignore |
| 03 | First API call -- client, request, response, tokens |
| 04 | Chat conversations -- system prompts, multi-turn, history |
| 05 | AI Agent -- automatic memory with threads |

- In one hour, you went from **zero Python** to **building an AI agent**

**Speaker Notes**:
Let's look at what you accomplished. Module 1: you learned the Python building blocks. Module 2: you set up a professional environment with secure credentials. Module 3: you made your first API call. Module 4: you built multi-turn conversations. Module 5: you built a full AI agent with memory. In one hour, starting from zero coding experience, you built an intelligent assistant that can help with real work tasks. [1.5 minutes on this slide]

**Suggested Visual**: A journey path with 5 milestones/stops, each labeled with the module topic. A flag at the end saying "You Are Here!" The path goes from "Zero Python" to "AI Agent."

---

### Slide 37: Key Concepts to Remember

**Layout**: Title + Content (five icons with labels)

**Bullet Points**:
1. **Variables & Types** are building blocks -- str, int, float, bool, list, dict
2. **`.env` files** keep secrets safe -- never hardcode API keys
3. **`client.chat.completions.create()`** is how you talk to AI
4. **System prompts** shape the AI's personality and behavior
5. **Agents + Threads** = AI with automatic memory

- If you remember nothing else, remember these five things

**Speaker Notes**:
If you take away five things from today, these are them. Variables and types are the foundation. Always use `.env` files for secrets. One function call talks to AI. System prompts are your most powerful tool for controlling output. And agents with threads are the professional way to build conversational AI. Everything else builds on these five concepts. [1 minute on this slide]

**Suggested Visual**: Five large icons in a row, each representing one concept (a box for variables, a lock for .env, a cloud for API, a document for system prompts, a robot for agents). Each with a short label beneath.

---

### Slide 38: What's Next?

**Layout**: Title + Content (four pathway cards)

**Bullet Points**:
- Four directions to explore after this session:

| Path | Description |
|------|------------|
| **Advanced Prompting** | Chain-of-thought reasoning, few-shot examples, prompt engineering techniques |
| **Agent Tools** | Give your agent capabilities: code interpreter, file search, function calling |
| **Web Interfaces** | Build a user-facing UI with Streamlit or Gradio |
| **RAG** | Retrieval-Augmented Generation -- connect AI to your own documents |

- All of these build on what you learned today
- The foundation (data types, API calls, agents) stays the same

**Speaker Notes**:
This is just the beginning. Four paths you can take from here. Advanced prompting to get better answers. Agent tools to give your agent superpowers like running code or searching files. Web interfaces to build real applications your team can use. And RAG, which lets you connect AI to your own documents -- imagine your Meeting Assistant reading actual meeting transcripts from your calendar. All of these build on what you learned today. [1 minute on this slide]

**Suggested Visual**: Four pathway arrows branching out from a central "Today" node, each leading to a labeled card with a relevant icon.

---

### Slide 39: Q&A

**Layout**: Title only (clean, open)

**Content**:
- **Questions?**
- Common questions to re-demo:
  - "How does the message format work?" → Module 1
  - "How is authentication handled?" → Module 3
  - "What's the difference between chat and agents?" → Module 4 vs 5
- Troubleshooting reference: see `README.md` in the project folder
- All code files are yours to keep and experiment with

**Speaker Notes**:
Open floor for questions. I have all five files ready to re-demo any concept. If someone asks about the message format, I can quickly rerun Module 1. If someone asks about agents vs chat, I can show Modules 4 and 5 side by side. All the code files are yours to keep -- I encourage you to modify them and experiment. The READMEs in the project folder explain every concept in detail. [5 minutes for Q&A -- adjust based on time remaining]

**Suggested Visual**: Large question mark icon centered. Small icons at the bottom representing the 5 modules for quick reference.

---

### Slide 40: Thank You / Closing

**Layout**: Title Slide (centered)

**Content**:
- **Thank You for Attending!**
- Python + Azure OpenAI: Building an AI Meeting Assistant
- Session materials: [link/path to project folder]
- Contact: [presenter email placeholder]
- Additional resources:
  - Azure OpenAI Documentation
  - Python Documentation
  - OpenAI API Reference
- **Keep Building!**

**Speaker Notes**:
Thank you all for your time and effort. You now have working code for a complete AI pipeline -- from basic Python to a full agent with memory. I encourage you to take these files home, modify them, break them, fix them, and build on them. That is the best way to learn. The project folder contains README files for each module that explain every concept in detail. If you have questions later, reach out. Keep building! [1 minute on this slide]

**Suggested Visual**: Clean closing slide with Azure blue background. Organization logo. A celebratory graphic (subtle confetti or starfield). The text "Keep Building!" in larger font at the bottom.

---

---

## Appendix: Slide Type Summary

| Slide Type | Slides | Notes |
|------------|--------|-------|
| Title / Section Header | 1, 5, 11, 17, 23, 29, 40 | Transition slides, minimal content |
| Content Slides | 6-9, 12-15, 18-21, 24-27, 30-33, 35-38 | Teaching content with visuals |
| Demo Slides | 10, 16, 22, 28, 34 | Live coding -- switch to VS Code |
| Interactive | 4, 39 | Audience participation (prerequisites check, Q&A) |

## Appendix: Demo Checklist

Before the presentation, verify these demos work:

- [ ] `python 01_python_fundamentals.py` runs and prints all 4 parts
- [ ] `python 02_environment_setup.py` shows 3/3 checks passed
- [ ] `python 03_azure_openai_simple.py` returns an AI response and token count
- [ ] `python 04_azure_openai_chat.py` shows multi-turn conversation and meeting summary
- [ ] `python 05_meeting_assistant_agent.py` shows the 4-message conversation with context recall
- [ ] VS Code terminal is configured and visible
- [ ] `.env` credentials are valid and not expired
- [ ] Internet connection is stable (required for API calls)
