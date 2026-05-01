"""
03_python_essentials_short.py — Python Essentials (Condensed)
Variables, Types, Lists, Dictionaries.
"""

# --- Variables & Data Types ---
prompt = "Summarize my meeting notes"       # str
max_tokens = 500                            # int
temperature = 0.7                           # float (0=focused, 1=creative)
is_streaming = False                        # bool

print("--- Data Types ---")
print(f"str:   {prompt} → {type(prompt)}")
print(f"int:   {max_tokens} → {type(max_tokens)}")
print(f"float: {temperature} → {type(temperature)}")
print(f"bool:  {is_streaming} → {type(is_streaming)}")

# --- Lists (ordered, uses []) ---
messages = []
messages.append("Hello!")
messages.append("How can I help?")
messages.append("Let me summarize that.")

print("\n--- Lists ---")
print(f"messages: {messages}")
print(f"First: {messages[0]}, Last: {messages[-1]}, Count: {len(messages)}")

# --- Dictionaries (key-value, uses {}) ---
user_message = {
    "role": "user",
    "content": "Please summarize my meeting notes"
}

print("\n--- Dictionaries ---")
print(f"user_message: {user_message}")
print(f"role: {user_message['role']}, content: {user_message['content']}")

# --- THE KEY PATTERN: List of Dicts (LLM chat message format) ---
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Here are my notes: discussed Q1 goals."},
    {"role": "assistant", "content": "I see you discussed Q1 goals. Want action items?"},
    {"role": "user", "content": "Yes please!"}
]

print("\n--- LLM Chat Message Format (List of Dicts) ---")
for msg in conversation:
    emoji = {"system": "⚙️", "user": "👤", "assistant": "🤖"}[msg["role"]]
    print(f"  {emoji} {msg['role'].upper()}: {msg['content']}")

print("\n✅ Next: python 04_project_setup_short.py")
