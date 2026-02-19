# Module 2: Environment Setup -- Virtual Environments, Secrets, and .gitignore

## Companion Reference for `02_environment_setup.py`

### Overview

This module teaches professional Python project setup practices. There are no AI API calls here -- instead you will learn how to isolate your project's dependencies, store secrets securely, and protect sensitive information from being accidentally published. These are industry-standard practices used in every professional Python project.

By the end of this module your environment will be fully configured and verified, ready for making Azure OpenAI API calls in the next module.

**Duration:** ~10 minutes

---

### Prerequisites

- Completed Module 1 (`01_python_fundamentals.py`)
- Python 3.10+ installed
- VS Code with the Python extension
- Session materials downloaded (the project folder)

---

### Concepts Covered

#### 1. Virtual Environments (`venv`)

A **virtual environment** is an isolated container of Python packages for a single project. Think of it as a private toolbox -- each project gets its own toolbox so the tools (packages) never conflict with each other.

**Why use virtual environments?**

```
   Your Computer
   ├── Project A (venv) → openai 1.0, pandas 2.0
   ├── Project B (venv) → openai 0.28, pandas 1.5
   └── Project C (venv) → Different packages entirely
```

Without virtual environments, installing a package for Project B could break Project A if they need different versions of the same package.

**Benefits:**
- Each project has its own packages (no conflicts)
- Easy to share: just share `requirements.txt`
- Clean uninstall: delete the `venv/` folder
- Matches production environments

**Commands to remember:**

| Action | Command (Windows) | Command (Mac/Linux) |
|--------|-------------------|---------------------|
| Create venv (once per project) | `python -m venv venv` | `python -m venv venv` |
| Activate venv (every terminal session) | `.\venv\Scripts\Activate` | `source venv/bin/activate` |
| Install packages | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Deactivate when done | `deactivate` | `deactivate` |

**How to tell it's active:** You will see `(venv)` at the beginning of your terminal prompt.

---

#### 2. The `.env` File -- Secure Credential Storage

A `.env` file is a plain-text configuration file that stores secrets as `KEY=VALUE` pairs, one per line. It lives in your project root folder and is never shared or committed to version control.

**Why use `.env` files?**

```python
# BAD -- secret is visible in your code for anyone to see!
api_key = "sk-abc123secretkey456"

# GOOD -- secret is loaded from .env file
api_key = os.getenv("AZURE_OPENAI_API_KEY")
```

If you hardcode secrets in your source code and push to GitHub, hackers can find and exploit them within minutes.

**Your `.env` file format:**

```
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-secret-key-here
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
```

**Important rules:**
- The file is named exactly `.env` (no extension, just `.env`)
- No spaces around the `=` sign
- No quotes around values
- One `KEY=VALUE` pair per line
- Copy the provided `.env.example` file to `.env` and fill in your actual values

---

#### 3. Loading Secrets with `python-dotenv`

The `python-dotenv` package reads your `.env` file and makes the values available in your Python code. This four-line pattern appears at the top of every file from Module 3 onward:

```python
import os
from dotenv import load_dotenv

# Read the .env file and load values into environment
load_dotenv()

# Retrieve individual values
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
```

**How it works step by step:**

1. `import os` -- provides `os.getenv()` to read environment variables
2. `from dotenv import load_dotenv` -- imports the loader from the `python-dotenv` package
3. `load_dotenv()` -- reads your `.env` file and loads each `KEY=VALUE` pair into the environment
4. `os.getenv("KEY")` -- retrieves a specific value by its key name. Returns `None` if the key is not found

---

#### 4. The `.gitignore` File -- Protecting Secrets from Git

Git is a version control system that tracks changes to your code. The `.gitignore` file tells Git which files and folders to **ignore** -- meaning they will never be tracked or committed.

**Critical entries for your `.gitignore`:**

```
# Secrets -- NEVER commit!
.env

# Virtual environment -- each developer creates their own
venv/

# Python cache -- auto-generated files
__pycache__/
*.pyc
```

**What happens without `.gitignore`?**

1. You accidentally commit `.env` to Git
2. You push to GitHub -- your API key is now **public**
3. Hackers run automated scanners that find exposed keys within minutes
4. Your Azure bill skyrockets as attackers use your credits

**Always verify before committing:** Run `git status` and make sure `.env` is NOT listed in the output.

---

#### 5. Credential Health Check

The file includes a validation section that checks whether all three required credentials loaded correctly. This is a simple pattern you can reuse in any project:

```python
if endpoint:
    print("AZURE_OPENAI_ENDPOINT: Loaded")
else:
    print("AZURE_OPENAI_ENDPOINT: Not found!")
```

The health check:
- Verifies each of the 3 required variables (`AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_DEPLOYMENT_NAME`)
- Shows masked values for security (e.g., `abcd...wxyz` instead of the full key)
- Reports a pass/fail summary (`3/3 checks passed` or tells you what to fix)

---

### Code Walkthrough

The file is organized into 5 parts:

| Part | What It Covers |
|------|----------------|
| Part 1 | What a virtual environment is and the commands to create/activate one |
| Part 2 | Why `.env` files are necessary and the `KEY=VALUE` format |
| Part 3 | The 4-line Python pattern to load and read secrets (`import os`, `from dotenv`, `load_dotenv()`, `os.getenv()`) |
| Part 4 | Why `.gitignore` matters -- the security horror story |
| Part 5 | Credential health check -- verifies all 3 credentials are loaded |

Run the file to verify your setup:

```bash
python 02_environment_setup.py
```

You should see `3/3 checks passed` at the end. If not, follow the instructions in the output to fix your `.env` file.

---

### Key Takeaways

1. `venv` = Isolated package environment per project
2. `.env` = Store secrets as `KEY=VALUE` pairs
3. `load_dotenv()` = Load `.env` values into your Python code
4. `os.getenv("KEY")` = Retrieve secret values safely
5. `.gitignore` = Prevent `.env` and `venv/` from being committed to Git
6. **Golden rule:** Never hardcode secrets in your code!

---

### Common Mistakes and Troubleshooting

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Naming the file `.env.txt` instead of `.env` | Secrets won't load (`None` for all values) | Rename to exactly `.env` (no extension). In Windows, make sure file extensions are visible in File Explorer settings |
| Forgetting to activate the venv | `ModuleNotFoundError: No module named 'dotenv'` | Run `.\venv\Scripts\Activate` (Windows) or `source venv/bin/activate` (Mac/Linux) |
| Adding quotes around values in `.env` | The quotes become part of the value | Write `KEY=value` not `KEY="value"` |
| Committing `.env` before creating `.gitignore` | Secrets are exposed in Git history | Create `.gitignore` first, then create `.env`. If already committed, remove with `git rm --cached .env` |
| Not running `pip install -r requirements.txt` | Missing packages | Activate venv first, then run the install command |

---

### Try It Yourself

Add a custom environment variable to practice the workflow:

1. Open your `.env` file
2. Add a new line: `MY_NAME=YourNameHere`
3. Uncomment the code at the bottom of `02_environment_setup.py`:

```python
my_name = os.getenv("MY_NAME")
print(f"Hello, {my_name}! Your custom variable works!")
```

4. Run the file again and confirm your custom variable appears

---

### What's Next

In **Module 3 (03_azure_openai_simple.py)** you will use these loaded credentials to create an Azure OpenAI client and make your very first API call to an AI model. You will send a prompt and receive an AI-generated response.
