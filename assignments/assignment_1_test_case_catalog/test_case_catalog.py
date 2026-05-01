"""
================================================================
🧪 LAB ASSIGNMENT 1 — EASY LEVEL
   Build a Team Contact Book (Python Only)
================================================================

⏱️  Estimated time: 15-20 minutes
🎯  Difficulty: ⭐ Easy (No API calls — pure Python!)

SCENARIO:
   You're organizing a project team. Build a contact book that
   stores team members and their roles, and can display, search,
   and summarize the team.

SKILLS TESTED (from File 01):
   ✅ Variables and data types (str, int, bool)
   ✅ Lists — ordered collections
   ✅ Dictionaries — key-value pairs
   ✅ Loops and f-strings
   ✅ Functions

================================================================
📋 INSTRUCTIONS — Complete the TODOs below!
================================================================

Run when done:  python lab_easy_contact_book.py

EXPECTED OUTPUT (example):
   📇 TEAM ROSTER (4 members)
   ──────────────────────────
   1. Sarah Chen — Project Manager | sarah@company.com
   2. John Park — Developer       | john@company.com
   ...
   🔍 Search results for "dev": John Park (Developer)
   📊 Role Summary: 1 Project Manager, 2 Developers, 1 Designer

================================================================
"""

print("=" * 60)
print("🧪 LAB: Team Contact Book")
print("=" * 60)


# ============================================================
# TASK 1: Create team members as dictionaries (3 points)
# ============================================================
# Each member should have: name (str), role (str), 
#                          email (str), is_available (bool)
#
# TODO: Create at least 4 team member dictionaries
# HINT: Use the same pattern as Azure OpenAI messages!
#       member = {"key": "value", "key": "value"}
# ============================================================

# Example (first one is done for you):
member1 = {
    "name": "Sarah Chen",
    "role": "Project Manager",
    "email": "sarah@company.com",
    "is_available": True
}

# TODO: Create member2 (a Developer)
# member2 = ...

# TODO: Create member3 (a Designer)
# member3 = ...

# TODO: Create member4 (another Developer)
# member4 = ...


# ============================================================
# TASK 2: Store all members in a list (2 points)
# ============================================================
# TODO: Create a list called 'team' containing all 4 members
# HINT: This is the same pattern as a conversation message list!
#       team = [member1, member2, ...]
# ============================================================

# team = ...


# ============================================================
# TASK 3: Display the team roster (3 points)
# ============================================================
# TODO: Write a function that prints each team member nicely
# 
# Expected output for each member:
#   1. Sarah Chen — Project Manager | sarah@company.com ✅
#   (✅ if available, ❌ if not)
#
# HINT: Use enumerate() and f-strings
#       for i, member in enumerate(team):
#           print(f"   {i+1}. {member['name']} ...")
# ============================================================

def display_roster(team):
    """Display all team members in a formatted list."""
    print(f"\n📇 TEAM ROSTER ({len(team)} members)")
    print("─" * 40)
    
    # TODO: Loop through team and print each member
    # Use ✅ for available members, ❌ for unavailable
    pass


# ============================================================
# TASK 4: Search by role (3 points)
# ============================================================
# TODO: Write a function that finds members by role keyword
#
# Example: search_by_role(team, "dev") → finds all Developers
#
# HINT: Use .lower() to make search case-insensitive
#       if search_term.lower() in member["role"].lower():
# ============================================================

def search_by_role(team, search_term):
    """Find team members whose role contains the search term."""
    results = []
    
    # TODO: Loop through team, check if search_term is in role
    # Append matching members to results list
    
    return results


# ============================================================
# TASK 5: Generate a role summary (4 points)
# ============================================================
# TODO: Write a function that counts how many people are in
#       each role and returns a dictionary
#
# Example output: {"Project Manager": 1, "Developer": 2, "Designer": 1}
#
# HINT: Create an empty dict, loop through team
#       if role in summary:
#           summary[role] += 1
#       else:
#           summary[role] = 1
# ============================================================

def role_summary(team):
    """Count team members per role. Returns a dict."""
    summary = {}
    
    # TODO: Count each role
    
    return summary


# ============================================================
# TASK 6: Put it all together! (2 points)
# ============================================================
# TODO: Uncomment and run the code below once you've completed
#       all the tasks above.
# ============================================================

# # Display full roster
# display_roster(team)
# 
# # Search for developers
# print("\n🔍 Searching for 'dev'...")
# devs = search_by_role(team, "dev")
# for d in devs:
#     print(f"   Found: {d['name']} ({d['role']})")
# 
# # Show role summary
# print("\n📊 Role Summary:")
# for role, count in role_summary(team).items():
#     print(f"   {role}: {count}")
# 
# # Bonus: Count available members
# available = [m for m in team if m["is_available"]]
# print(f"\n✅ Available: {len(available)}/{len(team)} members")


print("\n" + "=" * 60)
print("💡 HINTS & CONNECTION TO AZURE OPENAI")
print("=" * 60)
print("""
   Notice the patterns you used here:
   
   📖 Dictionaries → Same as Azure OpenAI message format
      {"name": "Sarah"}  ↔  {"role": "user", "content": "..."}
   
   📋 List of Dicts → Same as conversation history
      [member1, member2]  ↔  [msg1, msg2, msg3]
   
   🔁 Looping + f-strings → Used to process AI responses
   
   🔍 Search function → Similar to filtering AI outputs
   
   These are the EXACT same building blocks used in
   Files 03, 04, and 05 to talk to Azure OpenAI!
""")
