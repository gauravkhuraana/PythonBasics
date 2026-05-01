"""
test_case_catalog_short.py — Assignment 1 (Condensed)
Pure Python — no API calls. Practice dicts, lists, loops, functions.
"""

print("🧪 ASSIGNMENT 1: Test Case Catalog\n")

# TASK 1: Model a test case
tc1 = {"id": "TC-001", "title": "Login with valid creds",
       "module": "login", "priority": "High",
       "status": "pass", "automated": True}

# TODO: Create tc2..tc5 covering different modules / statuses


# TASK 2: Build the catalog list
# catalog = [tc1, tc2, tc3, tc4, tc5]


# TASK 3: Display
def display_catalog(catalog):
    print(f"📋 CATALOG ({len(catalog)} cases)")
    # TODO: loop + print  with icons {"pass":"✅","fail":"❌","skip":"⏭"}


# TASK 4: Filter by module
def cases_in_module(catalog, module_name):
    return [tc for tc in catalog if tc["module"].lower() == module_name.lower()]


# TASK 5: Status summary + pass rate
def status_summary(catalog):
    summary = {}
    # TODO: summary[tc["status"]] = summary.get(tc["status"], 0) + 1
    return summary


def pass_rate(catalog):
    # TODO: passes / (passes + fails) * 100
    return 0.0


# TASK 6: Uncomment once everything above is filled in
# display_catalog(catalog)
# print(f"\n🔍 login cases: {len(cases_in_module(catalog, 'login'))}")
# print(f"📊 {status_summary(catalog)}")
# print(f"📈 Pass rate: {pass_rate(catalog):.1f}%")
