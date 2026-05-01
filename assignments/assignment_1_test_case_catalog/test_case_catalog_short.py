"""
lab_easy_contact_book_short.py - Team Contact Book Lab (Condensed)
Pure Python — no API calls. Practice dicts, lists, loops, functions.
"""

print("🧪 LAB: Team Contact Book\n")

# TASK 1: Create team members as dictionaries
member1 = {"name": "Sarah Chen", "role": "Project Manager", "email": "sarah@company.com", "is_available": True}

# TODO: Create 3 more members
# member2 = {"name": "...", "role": "Developer", "email": "...", "is_available": True}
# member3 = {"name": "...", "role": "Designer", "email": "...", "is_available": False}
# member4 = {"name": "...", "role": "Developer", "email": "...", "is_available": True}


# TASK 2: Store all members in a list
# team = [member1, member2, member3, member4]


# TASK 3: Display the roster
def display_roster(team):
    print(f"📇 TEAM ROSTER ({len(team)} members)")
    # TODO: Loop through team and print each member
    # for i, member in enumerate(team):
    #     status = "✅" if member["is_available"] else "❌"
    #     print(f"  {i+1}. {member['name']} — {member['role']} | {member['email']} {status}")
    pass


# TASK 4: Search by role
def search_by_role(team, search_term):
    results = []
    # TODO: Find members whose role contains search_term
    # for member in team:
    #     if search_term.lower() in member["role"].lower():
    #         results.append(member)
    return results


# TASK 5: Count members per role
def role_summary(team):
    summary = {}
    # TODO: Count each role
    # for member in team:
    #     role = member["role"]
    #     if role in summary:
    #         summary[role] += 1
    #     else:
    #         summary[role] = 1
    return summary


# TASK 6: Uncomment to test
# display_roster(team)
#
# print("\n🔍 Searching for 'dev'...")
# for d in search_by_role(team, "dev"):
#     print(f"  Found: {d['name']} ({d['role']})")
#
# print("\n📊 Role Summary:")
# for role, count in role_summary(team).items():
#     print(f"  {role}: {count}")
