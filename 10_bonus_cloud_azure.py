"""
================================================================
03_azure_openai_simple.py
AZURE OPENAI: Your First API Call
================================================================

🎯 LAB GOAL REMINDER:
Building toward your AI Meeting Assistant!
Now let's make your first real AI API call.

This file covers:
  ✅ Setting up the Azure OpenAI client
  ✅ Making a simple API request
  ✅ Understanding the response
  ✅ Common errors and troubleshooting

Prerequisites:
  - Completed 02_environment_setup.py (credentials loaded)
  - Virtual environment activated
  - packages installed (pip install -r requirements.txt)

Run this file: python 03_azure_openai_simple.py
================================================================
"""

import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# ============================================================
# STEP 1: Load environment variables
# ============================================================
load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

print("=" * 60)
print("AZURE OPENAI: Your First API Call")
print("=" * 60)

# Quick check before proceeding
if not all([endpoint, deployment]):
    print("\n❌ ERROR: Missing credentials!")
    print("   Please run 02_environment_setup.py first")
    print("   and make sure your .env file is configured.")
    exit(1)

print("\n✅ Credentials loaded successfully!")


# ============================================================
# STEP 2: Create the Azure OpenAI client
# ============================================================
print("\n" + "-" * 40)
print("STEP 2: Creating Azure OpenAI Client")
print("-" * 40)

print("""
📝 CODE EXPLANATION:

   # Using Azure AD token-based auth (no API key needed!)
   credential = DefaultAzureCredential()
   token_provider = get_bearer_token_provider(
       credential, "https://cognitiveservices.azure.com/.default"
   )
   client = AzureOpenAI(
       azure_endpoint=endpoint,
       azure_ad_token_provider=token_provider,
       api_version="2024-12-01-preview"
   )
""")

# Use Azure AD authentication (key-based auth is disabled by org policy)
credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(
    credential, "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
    api_version="2024-12-01-preview"
)

print("✅ Client created!")


# ============================================================
# STEP 3: Make a simple API call
# ============================================================
print("\n" + "-" * 40)
print("STEP 3: Making Your First API Call")
print("-" * 40)

print("""
📝 CODE EXPLANATION:

   response = client.chat.completions.create(
       model=deployment,           # Your deployment name (e.g., "gpt-4o")
       messages=[                  # List of messages (remember File 01!)
           {
               "role": "user",     # Who is speaking
               "content": "..."    # What they're saying
           }
       ],
       max_tokens=150              # Limit response length
   )
""")

# Our first prompt - meeting-related to preview the final goal!
prompt = "What are 3 tips for running effective meetings? Keep it brief."

print(f"\n🗣️  Your prompt: \"{prompt}\"")
print("\n⏳ Sending request to Azure OpenAI...")

try:
    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_completion_tokens=200
    )
    
    # ============================================================
    # STEP 4: Understanding the response
    # ============================================================
    print("\n" + "-" * 40)
    print("STEP 4: Understanding the Response")
    print("-" * 40)
    
    print("""
📝 RESPONSE STRUCTURE:

   response.choices[0].message.content  → The AI's answer (text)
   response.choices[0].message.role     → "assistant"
   response.usage.prompt_tokens         → Tokens in your prompt
   response.usage.completion_tokens     → Tokens in the response
   response.usage.total_tokens          → Total tokens used
    """)
    
    # Extract the AI's response
    ai_response = response.choices[0].message.content
    
    print("\n🤖 AI RESPONSE:")
    print("-" * 40)
    print(ai_response)
    print("-" * 40)
    
    # Show token usage
    print(f"\n📊 TOKEN USAGE:")
    print(f"   Prompt tokens:     {response.usage.prompt_tokens}")
    print(f"   Completion tokens: {response.usage.completion_tokens}")
    print(f"   Total tokens:      {response.usage.total_tokens}")
    
    print("\n🎉 SUCCESS! You just made your first Azure OpenAI API call!")

except Exception as e:
    print(f"\n❌ ERROR: {type(e).__name__}")
    print(f"   {str(e)}")
    print("\n🔧 TROUBLESHOOTING:")
    print("   - AuthenticationError: Check your API key in .env")
    print("   - NotFoundError: Check your endpoint URL in .env")
    print("   - DeploymentNotFound: Check deployment name matches Azure portal")


print("\n" + "=" * 60)
print("🎯 KEY TAKEAWAYS")
print("=" * 60)
print("""
   1. AzureOpenAI() - Create client with endpoint, key, version
   2. client.chat.completions.create() - Make API call
   3. messages = [{"role": "...", "content": "..."}] - Input format
   4. response.choices[0].message.content - Get AI response
   5. response.usage - See token counts (affects cost!)
   
   🔑 REMEMBER: Each API call costs tokens!
      - Be concise with prompts
      - Set reasonable max_tokens
      - Monitor your usage
""")


print("\n" + "=" * 60)
print("✅ COMPLETE! Next: python 04_azure_openai_chat.py")
print("=" * 60)


# ============================================================
# 🧪 TRY IT YOURSELF!
# ============================================================
# Change the prompt below and run again!

# prompt = "What should be included in a meeting agenda?"
# 
# response = client.chat.completions.create(
#     model=deployment,
#     messages=[{"role": "user", "content": prompt}],
#     max_tokens=200
# )
# print(response.choices[0].message.content)
