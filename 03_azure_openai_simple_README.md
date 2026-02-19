# Module 3: Your First Azure OpenAI API Call

## Companion Reference for `03_azure_openai_simple.py`

### Overview

This is where the real excitement begins. In this module you will send your first prompt to Azure OpenAI and receive an AI-generated response. You will learn how to set up the client connection, structure an API call, interpret the response object, and understand token-based billing.

By the end of this module you will have a working script that talks to Azure OpenAI and returns intelligent responses.

**Duration:** ~12 minutes

---

### Prerequisites

- Completed Module 2 (`02_environment_setup.py`) with all 3/3 credential checks passed
- Virtual environment activated (`(venv)` visible in your terminal prompt)
- Packages installed (`pip install -r requirements.txt`)
- `.env` file configured with your Azure OpenAI credentials

---

### Concepts Covered

#### 1. What is an API?

An **API** (Application Programming Interface) is a way for your code to talk to an external service. When you call the Azure OpenAI API, your code sends a request over the internet to Microsoft's Azure servers, which run the AI model and send a response back.

Think of it like ordering at a restaurant: you (the code) give your order (the prompt) to the waiter (the API), who takes it to the kitchen (Azure's AI model) and brings back your meal (the response).

---

#### 2. The Azure OpenAI Client

The `AzureOpenAI()` object is your connection to Azure's AI service. You create it once and reuse it for all your API calls.

This file uses **Azure AD token-based authentication**, which is the more secure, enterprise-preferred method:

```python
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# Set up Azure AD authentication
credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(
    credential, "https://cognitiveservices.azure.com/.default"
)

# Create the client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
    api_version="2024-12-01-preview"
)
```

**Parameters explained:**

| Parameter | What It Does |
|-----------|-------------|
| `azure_endpoint` | The URL of your Azure OpenAI resource (from `.env`) |
| `azure_ad_token_provider` | Handles authentication using your Azure AD credentials |
| `api_version` | Which version of the Azure OpenAI API to use |

**Note:** Later modules (04 and 05) use a simpler API key-based authentication method:

```python
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-10-21"
)
```

Both methods work. Your organization may require one or the other.

---

#### 3. Making an API Call

The core function is `client.chat.completions.create()`. It takes three main parameters:

```python
response = client.chat.completions.create(
    model=deployment,                    # Your deployment name (e.g., "gpt-4o")
    messages=[                           # List of messages (the format from Module 1!)
        {
            "role": "user",
            "content": "What are 3 tips for running effective meetings? Keep it brief."
        }
    ],
    max_completion_tokens=200            # Limit response length
)
```

| Parameter | Type | What It Does |
|-----------|------|-------------|
| `model` | string | The name of your deployed model in Azure |
| `messages` | list of dicts | The conversation in the `[{"role": "...", "content": "..."}]` format you learned in Module 1 |
| `max_completion_tokens` | integer | Maximum number of tokens the AI can use in its response |

---

#### 4. Understanding the Response Object

The API returns a structured response object. Here is how to access the important parts:

```python
# The AI's text response
ai_response = response.choices[0].message.content

# The role (always "assistant")
role = response.choices[0].message.role

# Token usage statistics
prompt_tokens = response.usage.prompt_tokens           # Tokens in your prompt
completion_tokens = response.usage.completion_tokens   # Tokens in the response
total_tokens = response.usage.total_tokens             # Grand total
```

**Response structure visualized:**

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

---

#### 5. Tokens and Cost

A **token** is the unit Azure OpenAI uses to measure text. Roughly:
- 1 token ≈ 4 characters of English text
- 1 token ≈ 3/4 of a word
- The word "hamburger" = 3 tokens
- The phrase "Hello, world!" = 3 tokens

**Why tokens matter:**
- Every API call costs money based on tokens used
- `prompt_tokens` = how many tokens your input consumed
- `completion_tokens` = how many tokens the AI's response consumed
- `total_tokens = prompt_tokens + completion_tokens`

**Cost-saving tips:**
- Be concise with your prompts
- Set a reasonable `max_completion_tokens` value
- Monitor your `response.usage` stats

---

#### 6. Error Handling

The file wraps the API call in a `try/except` block to catch and explain common errors:

```python
try:
    response = client.chat.completions.create(...)
except Exception as e:
    print(f"ERROR: {type(e).__name__}")
    print(f"   {str(e)}")
```

**Common errors and fixes:**

| Error | Cause | Fix |
|-------|-------|-----|
| `AuthenticationError` | Invalid API key or Azure AD credentials | Check your `.env` file credentials |
| `NotFoundError` | Invalid endpoint URL | Verify the endpoint URL matches your Azure portal |
| `DeploymentNotFound` | Deployment name doesn't match | Check that `AZURE_OPENAI_DEPLOYMENT_NAME` in `.env` matches the name in your Azure portal |
| `ModuleNotFoundError` | Packages not installed | Run `pip install -r requirements.txt` with venv activated |

---

### Code Walkthrough

The file is organized into 4 steps:

| Step | What It Does |
|------|-------------|
| Step 1 | Loads environment variables from `.env` and verifies credentials exist |
| Step 2 | Creates the Azure OpenAI client using Azure AD token-based authentication |
| Step 3 | Sends a meeting-related prompt to the API and receives a response |
| Step 4 | Extracts the AI's text response and displays token usage statistics |

Run the file:

```bash
python 03_azure_openai_simple.py
```

You should see the AI's response to "What are 3 tips for running effective meetings?" followed by token usage counts.

---

### Key Takeaways

1. `AzureOpenAI()` -- creates the client connection with endpoint, authentication, and API version
2. `client.chat.completions.create()` -- sends a request to the AI model
3. `messages = [{"role": "...", "content": "..."}]` -- the input format (list of dictionaries from Module 1)
4. `response.choices[0].message.content` -- extracts the AI's text response
5. `response.usage` -- shows token counts (directly affects cost)
6. Each API call costs tokens -- be concise and set reasonable limits

---

### Common Mistakes and Troubleshooting

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Running without activating venv | `ModuleNotFoundError: No module named 'openai'` | Activate your virtual environment first |
| Missing or wrong endpoint URL | `NotFoundError` or connection error | Check `AZURE_OPENAI_ENDPOINT` in `.env` -- should look like `https://your-resource.openai.azure.com/` |
| Deployment name mismatch | `DeploymentNotFound` | The name in `.env` must exactly match the deployment name in your Azure portal |
| Skipping Module 2 | Credentials return `None` | Run `02_environment_setup.py` first to verify your `.env` is correct |
| Setting `max_completion_tokens` too low | Response gets cut off mid-sentence | Increase the value (e.g., from 50 to 200) |

---

### Try It Yourself

Change the prompt and run again to see different responses:

```python
prompt = "What should be included in a meeting agenda?"

response = client.chat.completions.create(
    model=deployment,
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=200
)
print(response.choices[0].message.content)
```

Experiment ideas:
- Ask the AI to write a meeting invitation email
- Try different `max_completion_tokens` values and observe how the response length changes
- Compare the token usage across different prompt lengths

---

### What's Next

In **Module 4 (04_azure_openai_chat.py)** you will build on this single API call by adding system prompts that control the AI's personality and multi-turn conversations that maintain message history across multiple exchanges.
