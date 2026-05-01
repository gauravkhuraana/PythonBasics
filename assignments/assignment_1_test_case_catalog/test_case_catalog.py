"""
================================================================
🧪 ASSIGNMENT 1 — EASY LEVEL
   Build a Test Case Catalog (Pure Python — no API calls)
================================================================

⏱️  Estimated time: 15-20 minutes
🎯  Difficulty: ⭐ Easy

SCENARIO:
   You're an SDET on a team that's been keeping test cases in
   a giant spreadsheet. Build a small Python catalog that stores
   test cases, lists them by module, searches them, and gives a
   pass/fail summary.

SKILLS TESTED (from Video 3):
   ✅ Variables and data types (str, int, bool)
   ✅ Lists and dictionaries
   ✅ Loops and f-strings
   ✅ Functions

================================================================
📋 INSTRUCTIONS — Complete the TODOs below!
================================================================

Run when done:  python test_case_catalog.py

EXPECTED OUTPUT (example):
   📋 TEST CASE CATALOG (5 cases)
   ──────────────────────────────
   1. [TC-001] Login with valid creds        | login    | High   | ✅ pass
   2. [TC-002] Login with invalid creds      | login    | High   | ❌ fail
   3. [TC-003] Reset password email          | login    | Medium | ⏭ skip
   4. [TC-101] Add item to cart              | cart     | High   | ✅ pass
   5. [TC-102] Remove last item from cart    | cart     | Medium | ❌ fail

   🔍 Cases in module 'login': 3
   📊 Status summary: pass=2, fail=2, skip=1
   📈 Pass rate: 40.0%
================================================================
"""

print("=" * 60)
print("🧪 ASSIGNMENT 1: Test Case Catalog")
print("=" * 60)


# ============================================================
# TASK 1: Model a single test case as a dictionary (3 points)
# ============================================================
# A test case has these fields:
#   id            (str)   — e.g., "TC-001"
#   title         (str)   — short description of what's tested
#   module        (str)   — e.g., "login", "cart", "checkout"
#   priority      (str)   — "High" / "Medium" / "Low"
#   status        (str)   — "pass" / "fail" / "skip"
#   automated     (bool)  — True if it's covered by automation
#
# TODO: Create AT LEAST 5 test case dictionaries.
# HINT: Same dict pattern you'll use later for LLM messages —
#       {"key": "value", ...}
# ============================================================

# Example (first one is done for you):
tc1 = {
    "id":        "TC-001",
    "title":     "Login with valid creds",
    "module":    "login",
    "priority":  "High",
    "status":    "pass",
    "automated": True,
}

# TODO: Create tc2 (login, fails)
# tc2 = ...

# TODO: Create tc3 (login, skipped)
# tc3 = ...

# TODO: Create tc4 (cart, passes)
# tc4 = ...

# TODO: Create tc5 (cart, fails)
# tc5 = ...


# ============================================================
# TASK 2: Store all test cases in a list (2 points)
# ============================================================
# TODO: Create a list called 'catalog' containing all your
#       test case dicts.
# ============================================================

# catalog = [tc1, tc2, tc3, tc4, tc5]


# ============================================================
# TASK 3: Display the catalog (3 points)
# ============================================================
# Expected line per case:
#   1. [TC-001] Login with valid creds        | login    | High   | ✅ pass
# Use:  ✅ for pass, ❌ for fail, ⏭ for skip.
#
# HINT: f-strings + .ljust() for column alignment, e.g.
#   f"{tc['title']:<35}"  (left-pad title to 35 chars)
# ============================================================

def display_catalog(catalog):
    """Print every test case as a numbered, aligned row."""
    print(f"\n📋 TEST CASE CATALOG ({len(catalog)} cases)")
    print("─" * 70)

    # TODO: Loop through and print each case.
    # for i, tc in enumerate(catalog, start=1):
    #     icon = {"pass": "✅", "fail": "❌", "skip": "⏭"}[tc["status"]]
    #     print(f"  {i}. [{tc['id']}] {tc['title']:<35} | "
    #           f"{tc['module']:<8} | {tc['priority']:<6} | {icon} {tc['status']}")
    pass


# ============================================================
# TASK 4: Filter by module (3 points)
# ============================================================
# Return all test cases whose 'module' matches `module_name`
# (case-insensitive).
# ============================================================

def cases_in_module(catalog, module_name):
    """Return a list of test cases whose module equals module_name."""
    results = []
    # TODO: append matching cases to results
    return results


# ============================================================
# TASK 5: Status summary + pass rate (4 points)
# ============================================================
# Build a dict like {"pass": 2, "fail": 2, "skip": 1}.
# Then compute the pass rate as a float percent (passes /
# total runnable, where runnable = pass + fail; skips don't
# count toward the denominator).
#
# HINT:
#   summary[status] = summary.get(status, 0) + 1
# ============================================================

def status_summary(catalog):
    """Return a dict of status → count, e.g., {'pass': 2, 'fail': 2}."""
    summary = {}
    # TODO: count each status
    return summary


def pass_rate(catalog):
    """Return the pass percentage (passes / (passes + fails))."""
    # TODO: compute and return a float (e.g. 40.0)
    return 0.0


# ============================================================
# TASK 6: Put it all together (2 points)
# ============================================================
# Uncomment the block below once Tasks 1–5 are done.
# ============================================================

# display_catalog(catalog)
#
# print(f"\n🔍 Cases in module 'login': {len(cases_in_module(catalog, 'login'))}")
#
# summary = status_summary(catalog)
# pretty = ", ".join(f"{k}={v}" for k, v in summary.items())
# print(f"📊 Status summary: {pretty}")
# print(f"📈 Pass rate: {pass_rate(catalog):.1f}%")
#
# # Bonus: how many are automated?
# automated = [tc for tc in catalog if tc["automated"]]
# print(f"🤖 Automated: {len(automated)}/{len(catalog)} cases")


# ============================================================
# 💡 WHY THIS MATTERS FOR LATER VIDEOS
# ============================================================
# The shape you used here:
#
#   catalog = [
#       {"id": "...", "title": "...", "status": "..."},
#       {"id": "...", "title": "...", "status": "..."},
#       ...
#   ]
#
# is the EXACT same shape as an LLM message list:
#
#   messages = [
#       {"role": "system",    "content": "..."},
#       {"role": "user",      "content": "..."},
#       {"role": "assistant", "content": "..."},
#   ]
#
# In Assignment 2 you'll send a list-of-dicts like this to a
# real AI model and get a polished bug report back.
# ============================================================
