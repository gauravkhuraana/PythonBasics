"""
================================================================
03_python_essentials.py — Video 3
PYTHON ESSENTIALS FOR AI IN 15 MINUTES
================================================================

🎯 GOAL:
   Cover just enough Python to talk to an AI: variables,
   types, lists, dicts, loops, and the message-list pattern
   you'll re-use in every later video.

This file covers:
  ✅ Variables and data types (str, int, float, bool)
  ✅ Lists  — ordered collections  [ ]
  ✅ Dicts  — key-value pairs      { }
  ✅ How these map to LLM message lists

Run this file:  python 03_python_essentials.py
================================================================
"""

print("=" * 60)
print("PART 1: VARIABLES AND DATA TYPES")
print("=" * 60)

# ============================================================
# STRINGS (str) - Text data
# ============================================================
# In AI, strings are used for: prompts, responses, instructions

prompt = "Summarize my test run results"
assistant_name = "QA Assistant"

print(f"\n📝 STRINGS (str) - Text data")
print(f"   prompt = \"{prompt}\"")
print(f"   Type: {type(prompt)}")

# String operations you'll use often:
combined = assistant_name + " says: " + prompt
print(f"   Combined: {combined}")


# ============================================================
# INTEGERS (int) - Whole numbers
# ============================================================
# In AI, integers are used for: max_tokens, counting, limits

max_tokens = 500  # Maximum length of AI response
message_count = 3

print(f"\n🔢 INTEGERS (int) - Whole numbers")
print(f"   max_tokens = {max_tokens}")
print(f"   Type: {type(max_tokens)}")


# ============================================================
# FLOATS (float) - Decimal numbers
# ============================================================
# In AI, floats are used for: temperature (creativity setting)

temperature = 0.7  # 0 = focused/deterministic, 1 = creative/random

print(f"\n🌡️  FLOATS (float) - Decimal numbers")
print(f"   temperature = {temperature}")
print(f"   Type: {type(temperature)}")
print(f"   Tip: Lower = more focused, Higher = more creative")


# ============================================================
# BOOLEANS (bool) - True/False
# ============================================================
# In AI, booleans are used for: flags, settings, conditions

is_streaming = False  # Whether to stream responses
debug_mode = True

print(f"\n✅ BOOLEANS (bool) - True/False")
print(f"   is_streaming = {is_streaming}")
print(f"   Type: {type(is_streaming)}")


print("\n" + "=" * 60)
print("PART 2: LISTS - Ordered Collections")
print("=" * 60)

# ============================================================
# LISTS - Using square brackets []
# ============================================================
# In AI, lists store: conversation history, multiple messages

# Empty list
messages = []

# Add items with .append()
messages.append("Hello!")
messages.append("How can I help with your test run?")
messages.append("Let me summarize that for you.")

print(f"\n📋 LISTS - Ordered collections using [ ]")
print(f"   messages = {messages}")
print(f"   Number of messages: {len(messages)}")

# Access items by index (starts at 0!)
print(f"\n   Accessing list items:")
print(f"   messages[0] = \"{messages[0]}\" (first item)")
print(f"   messages[1] = \"{messages[1]}\" (second item)")
print(f"   messages[-1] = \"{messages[-1]}\" (last item)")

# Loop through a list
print(f"\n   Looping through list:")
for i, msg in enumerate(messages):
    print(f"   {i}: {msg}")


print("\n" + "=" * 60)
print("PART 3: DICTIONARIES - Key-Value Pairs")
print("=" * 60)

# ============================================================
# DICTIONARIES - Using curly braces {}
# ============================================================
# In AI, dictionaries structure: messages with role + content

# A single message as a dictionary
user_message = {
    "role": "user",
    "content": "Please summarize my test run results"
}

print(f"\n📖 DICTIONARIES - Key-value pairs using {{ }}")
print(f"   user_message = {user_message}")

# Access values by key
print(f"\n   Accessing dictionary values:")
print(f"   user_message['role'] = \"{user_message['role']}\"")
print(f"   user_message['content'] = \"{user_message['content']}\"")


print("\n" + "=" * 60)
print("PART 4: COMBINING LISTS + DICTS (Azure OpenAI Format!)")
print("=" * 60)

# ============================================================
# THIS IS THE KEY PATTERN FOR AZURE OPENAI!
# Messages = LIST of DICTIONARIES
# ============================================================

conversation = [
    {"role": "system", "content": "You are a helpful QA assistant."},
    {"role": "user", "content": "Here are my test results: 28 passed, 5 failed."},
    {"role": "assistant", "content": "Got it — want a triage summary of the 5 failures?"},
    {"role": "user", "content": "Yes please!"}
]

print(f"\n🌟 LLM CHAT MESSAGE FORMAT (works for both local & cloud):")
print(f"   A LIST of DICTIONARIES with 'role' and 'content'\n")

for msg in conversation:
    role = msg["role"].upper()
    content = msg["content"]
    
    # Add emoji based on role
    if msg["role"] == "system":
        emoji = "⚙️ "
    elif msg["role"] == "user":
        emoji = "👤"
    else:
        emoji = "🤖"
    
    print(f"   {emoji} {role}: {content}")


print("\n" + "=" * 60)
print("🎯 KEY TAKEAWAYS")
print("=" * 60)
print("""
   1. str (strings)  → Prompts and responses
   2. int (integers) → Token limits, counts
   3. float          → Temperature (creativity)
   4. bool           → True/False settings
   5. list           → Ordered collection using [ ]
   6. dict           → Key-value pairs using { }
   
   🌟 MOST IMPORTANT for talking to any LLM:
   Messages are a LIST of DICTIONARIES:
   [
       {"role": "system", "content": "..."},
       {"role": "user", "content": "..."},
       {"role": "assistant", "content": "..."}
   ]
""")


print("=" * 60)
print("✅ COMPLETE! Next: python 04_project_setup.py")
print("=" * 60)


# ============================================================
# 🧪 TRY IT YOURSELF!
# ============================================================
# Uncomment and modify the code below to practice:

# # Create your own QA-related message
# my_message = {
#     "role": "user",
#     "content": "YOUR MESSAGE HERE"
# }
# print(f"\nMy message: {my_message}")

# # Add it to a conversation list
# my_conversation = [
#     {"role": "system", "content": "You are a QA assistant."},
#     my_message
# ]
# print(f"My conversation: {my_conversation}")
