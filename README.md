# 🎯 Python + Azure OpenAI: Hands-On Session

## Lab Goal: Build an AI Meeting Assistant

**By the end of this 1-hour session, you will build an AI Meeting Assistant that:**
- ✅ Remembers your entire conversation
- ✅ Helps create meeting agendas
- ✅ Extracts action items from meeting notes
- ✅ Provides follow-up suggestions

You'll learn Python basics, environment setup, and Azure OpenAI—all leading to this goal!

---

## 📁 Session Files (Complete in Order)

| # | File | Duration | What You'll Learn |
|---|------|----------|-------------------|
| 1 | `01_python_fundamentals.py` | ~12 min | Variables, types, lists, dictionaries |
| 2 | `02_environment_setup.py` | ~10 min | Virtual environments, secrets, .gitignore |
| 3 | `03_azure_openai_simple.py` | ~12 min | Your first AI API call |
| 4 | `04_azure_openai_chat.py` | ~8 min | Chat with message history |
| 5 | `05_meeting_assistant_agent.py` | ~13 min | 🎉 Build your Meeting Assistant! |

---

## 🚀 Setup Instructions

### Step 1: Open Terminal in VS Code
- Press `` Ctrl+` `` (backtick) to open the terminal
- Or go to **View → Terminal**

### Step 2: Create Virtual Environment
```powershell
# Navigate to this folder (if not already there)
cd e:\Automation\PythonBasics

# Create virtual environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\Activate

# You should see (venv) at the start of your terminal prompt
```

### Step 3: Install Required Packages
```powershell
pip install -r requirements.txt
```

### Step 4: Configure Your Credentials
1. Copy `.env.example` to `.env`
2. Fill in the Azure OpenAI credentials provided by your instructor:
   - `AZURE_OPENAI_ENDPOINT` - Your Azure OpenAI resource URL
   - `AZURE_OPENAI_API_KEY` - Your API key
   - `AZURE_OPENAI_DEPLOYMENT_NAME` - Model deployment name (e.g., gpt-4o)

### Step 5: Run Each File in Order
```powershell
python 01_python_fundamentals.py
python 02_environment_setup.py
python 03_azure_openai_simple.py
python 04_azure_openai_chat.py
python 05_meeting_assistant_agent.py
```

---

## 🔧 Troubleshooting

### "python is not recognized"
- Make sure Python is installed and added to PATH
- Try `python3` instead of `python`

### "ModuleNotFoundError: No module named 'openai'"
- Make sure your virtual environment is activated: `.\venv\Scripts\Activate`
- Run `pip install -r requirements.txt` again

### "AuthenticationError" or "API key invalid"
- Check your `.env` file has the correct API key
- Make sure there are no extra spaces or quotes

### "Resource not found" or "Endpoint not found"
- Verify your `AZURE_OPENAI_ENDPOINT` URL is correct
- It should look like: `https://your-resource-name.openai.azure.com/`

### "DeploymentNotFound"
- Check that `AZURE_OPENAI_DEPLOYMENT_NAME` matches your Azure portal exactly

---

## 📚 What's Next?

After this session, you can explore:
- **Advanced prompting**: Chain-of-thought, few-shot learning
- **Agent tools**: Code interpreter, file search
- **Building applications**: Streamlit, Gradio for UI
- **RAG (Retrieval-Augmented Generation)**: Connect AI to your documents

---

## 💡 Tips for Success

1. **Run each file** before moving to the next—they build on each other
2. **Read the comments**—they explain what each line does
3. **Experiment!** Change prompts and see what happens
4. **Ask questions**—there are no silly questions when learning

Good luck and enjoy building your first AI application! 🚀
