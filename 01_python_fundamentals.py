"""
================================================================
01_python_fundamentals.py
PYTHON BASICS: Variables, Types, and Collections
================================================================

🎯 LAB GOAL REMINDER:
By the end of this session, you'll build an AI Meeting Assistant!
First, let's learn the Python building blocks you'll need.

This file covers:
  ✅ Variables and data types (str, int, float, bool)
  ✅ Lists - ordered collections
  ✅ Dictionaries - key-value pairs
  ✅ How these map to Azure OpenAI concepts

Run this file: python 01_python_fundamentals.py
================================================================
"""

print("=" * 60)
print("PART 1: VARIABLES AND DATA TYPES")
print("=" * 60)

# ============================================================
# STRINGS (str) - Text data
# ============================================================
# In AI, strings are used for: prompts, responses, instructions

prompt = "Summarize my meeting notes"
assistant_name = "Meeting Assistant"

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
messages.append("How can I help with your meeting?")
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
    "content": "Please summarize my meeting notes"
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
    {"role": "system", "content": "You are a helpful meeting assistant."},
    {"role": "user", "content": "Here are my meeting notes: discussed Q1 goals."},
    {"role": "assistant", "content": "I see you discussed Q1 goals. Would you like me to extract action items?"},
    {"role": "user", "content": "Yes please!"}
]

print(f"\n🌟 AZURE OPENAI MESSAGE FORMAT:")
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
   
   🌟 MOST IMPORTANT for Azure OpenAI:
   Messages are a LIST of DICTIONARIES:
   [
       {"role": "system", "content": "..."},
       {"role": "user", "content": "..."},
       {"role": "assistant", "content": "..."}
   ]
""")


print("=" * 60)
print("✅ COMPLETE! Next: python 02_environment_setup.py")
print("=" * 60)


# ============================================================
# 🧪 TRY IT YOURSELF!
# ============================================================
# Uncomment and modify the code below to practice:

# # Create your own meeting-related message
# my_message = {
#     "role": "user",
#     "content": "YOUR MESSAGE HERE"
# }
# print(f"\nMy message: {my_message}")

# # Add it to a conversation list
# my_conversation = [
#     {"role": "system", "content": "You are a meeting assistant."},
#     my_message
# ]
# print(f"My conversation: {my_conversation}")
