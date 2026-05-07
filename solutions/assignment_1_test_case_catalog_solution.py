"""
SOLUTION — Assignment 1: Test Case Catalog
Pure Python (no API). Reference implementation.
"""

# TASK 1: Five test cases
tc1 = {"id": "TC-001", "title": "Login with valid creds",
       "module": "login", "priority": "High",
       "status": "pass", "automated": True}

tc2 = {"id": "TC-002", "title": "Login with invalid creds",
       "module": "login", "priority": "High",
       "status": "fail", "automated": True}

tc3 = {"id": "TC-003", "title": "Reset password email",
       "module": "login", "priority": "Medium",
       "status": "skip", "automated": False}

tc4 = {"id": "TC-101", "title": "Add item to cart",
       "module": "cart", "priority": "High",
       "status": "pass", "automated": True}

tc5 = {"id": "TC-102", "title": "Remove last item from cart",
       "module": "cart", "priority": "Medium",
       "status": "fail", "automated": False}

# TASK 2: Catalog
catalog = [tc1, tc2, tc3, tc4, tc5]

ICONS = {"pass": "✅", "fail": "❌", "skip": "⏭"}


# TASK 3: Display
def display_catalog(catalog):
    print(f"\n📋 TEST CASE CATALOG ({len(catalog)} cases)")
    print("─" * 70)
    for i, tc in enumerate(catalog, start=1):
        icon = ICONS.get(tc["status"], "❓")
        print(f"  {i}. [{tc['id']}] {tc['title']:<35} | "
              f"{tc['module']:<8} | {tc['priority']:<6} | {icon} {tc['status']}")


# TASK 4: Filter by module
def cases_in_module(catalog, module_name):
    return [tc for tc in catalog
            if tc["module"].lower() == module_name.lower()]


# TASK 5: Status summary + pass rate
def status_summary(catalog):
    summary = {}
    for tc in catalog:
        summary[tc["status"]] = summary.get(tc["status"], 0) + 1
    return summary


def pass_rate(catalog):
    summary = status_summary(catalog)
    passes = summary.get("pass", 0)
    fails = summary.get("fail", 0)
    runnable = passes + fails
    if runnable == 0:
        return 0.0
    return passes / runnable * 100


# TASK 6: Drive it
if __name__ == "__main__":
    print("=" * 60)
    print("🧪 ASSIGNMENT 1 — SOLUTION")
    print("=" * 60)

    display_catalog(catalog)

    print(f"\n🔍 Cases in module 'login': "
          f"{len(cases_in_module(catalog, 'login'))}")

    pretty = ", ".join(f"{k}={v}" for k, v in status_summary(catalog).items())
    print(f"📊 Status summary: {pretty}")
    print(f"📈 Pass rate: {pass_rate(catalog):.1f}%")

    automated = [tc for tc in catalog if tc["automated"]]
    print(f"🤖 Automated: {len(automated)}/{len(catalog)} cases")
