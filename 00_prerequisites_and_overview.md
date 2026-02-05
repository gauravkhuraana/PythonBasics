# 🎯 Python + Azure OpenAI: Hands-On Session

## Session Overview

| | |
|---|---|
| **Duration** | 1 Hour |
| **Level** | Beginner (No coding experience required) |
| **Goal** | Build an AI Meeting Assistant that remembers your conversation |
| **Format** | Hands-on coding with guided exercises |

---

## 📋 Prerequisites (Complete BEFORE the Session)

### 1. Software Installation

| Software | Version | Download Link |
|----------|---------|---------------|
| **Python** | 3.10 or higher | [python.org/downloads](https://www.python.org/downloads/) |
| **VS Code** | Latest | [code.visualstudio.com](https://code.visualstudio.com/) |
| **Python Extension** | Latest | Install from VS Code Extensions (Ctrl+Shift+X) |

#### ✅ Verify Python Installation
Open a terminal and run:
```powershell
python --version
```
You should see: `Python 3.10.x` or higher

---

### 2. Azure OpenAI Access

You will receive the following credentials from your instructor:
- ✅ Azure OpenAI Endpoint URL
- ✅ Azure OpenAI API Key
- ✅ Deployment Name (e.g., gpt-4o)

> **Note:** Credentials will be provided at the start of the session. No action needed beforehand.

---

### 3. Download Session Materials

Before the session, download/clone the training folder to your computer:
```
PythonBasics/
├── README.md
├── .env.example
├── .gitignore
├── requirements.txt
├── 01_python_fundamentals.py
├── 02_environment_setup.py
├── 03_azure_openai_simple.py
├── 04_azure_openai_chat.py
└── 05_meeting_assistant_agent.py
```

---

## 🎓 What You Will Learn

### Part 1: Python Fundamentals (~12 min)
- **Variables & Data Types**: `str`, `int`, `float`, `bool`
- **Collections**: Lists `[]` and Dictionaries `{}`
- **Why it matters**: These are building blocks for AI API calls

### Part 2: Environment Setup (~10 min)
- **Virtual Environments (venv)**: Isolate project packages
- **Secrets Management (.env)**: Store API keys safely
- **Git Ignore (.gitignore)**: Protect secrets from commits
- **Why it matters**: Professional setup that keeps credentials secure

### Part 3: Your First AI API Call (~12 min)
- **Azure OpenAI Client**: Connect to Azure
- **Simple Request**: Send a prompt, get a response
- **Understanding Tokens**: How AI usage is measured
- **Why it matters**: The foundation of all AI applications

### Part 4: Chat with Message History (~8 min)
- **System Prompts**: Set AI behavior/personality
- **Multi-turn Conversations**: Maintain chat history
- **Practical Example**: Summarize meeting notes
- **Why it matters**: Real AI apps need conversation context

### Part 5: Build Your Meeting Assistant Agent (~13 min)
- **Agents vs Chat**: Why agents are more powerful
- **Threads**: Automatic conversation memory
- **Your Meeting Assistant**: Helps with agendas, action items, follow-ups
- **Why it matters**: Experience the "wow factor" of AI agents!

---

## 🏆 By the End of This Session, You Will...

✅ Understand Python basics needed for AI development  
✅ Know how to securely manage API credentials  
✅ Make your first Azure OpenAI API call  
✅ Build a multi-turn chatbot with memory  
✅ Create an AI Meeting Assistant agent  
✅ Have working code you can extend for your own projects  

---

## 📁 Session Files Overview

| File | What You'll Build | Key Concepts |
|------|-------------------|--------------|
| `01_python_fundamentals.py` | Learn Python basics | Variables, lists, dictionaries |
| `02_environment_setup.py` | Configure your environment | venv, .env, gitignore |
| `03_azure_openai_simple.py` | First AI API call | Client setup, prompts, responses |
| `04_azure_openai_chat.py` | Chatbot with history | System prompts, multi-turn |
| `05_meeting_assistant_agent.py` | 🎉 **Meeting Assistant!** | Agents, threads, memory |

---

## ⏱️ Session Timeline

| Time | Activity | File |
|------|----------|------|
| 0:00 - 0:05 | Setup verification | - |
| 0:05 - 0:17 | Python Fundamentals | `01_python_fundamentals.py` |
| 0:17 - 0:27 | Environment Setup | `02_environment_setup.py` |
| 0:27 - 0:39 | First Azure OpenAI Call | `03_azure_openai_simple.py` |
| 0:39 - 0:47 | Chat with Messages | `04_azure_openai_chat.py` |
| 0:47 - 1:00 | Build Meeting Assistant | `05_meeting_assistant_agent.py` |

---

## ❓ Frequently Asked Questions

**Q: Do I need prior coding experience?**  
A: No! This session is designed for complete beginners.

**Q: What if I fall behind during the session?**  
A: All files have detailed comments. You can catch up at your own pace.

**Q: Can I keep the code after the session?**  
A: Yes! The code is yours to extend and use.

**Q: Will the Azure OpenAI credentials keep working?**  
A: Check with your instructor about credential validity after the session.

**Q: What if something doesn't work?**  
A: Each file includes troubleshooting tips. The README has common fixes.

---

## 🚀 Quick Start Checklist

Before the session begins, verify:

- [ ] Python 3.10+ installed (`python --version`)
- [ ] VS Code installed and working
- [ ] Python extension installed in VS Code
- [ ] Session materials downloaded
- [ ] Terminal opens in VS Code (Ctrl+`)

---

## 📞 Need Help?

If you encounter issues during setup:
1. Check the troubleshooting section in `README.md`
2. Ask your instructor or session facilitator
3. Google the exact error message (most Python errors are well-documented!)

---

**See you at the session! 🎉**
