# Capstone Option — Defect Triage Assistant 🐞

> Interactive defect triage on your **local LLM**, with cross-bug memory.

This is the ⭐⭐⭐ capstone build of [Assignment 3's](../assignment_3_qa_agent/) `triage` skill — same brain, but a real loop you'd actually use during a release week.

## What you get

- Paste a raw bug description → get a consistent markdown triage decision:
  - **Severity** (Critical / High / Medium / Low) + 1-line justification
  - **Owner area** (auth, payments, ui-cart, mobile-ios, …)
  - **Duplicate likelihood** with reference to earlier `BUG-N` IDs
  - **2-3 clarifying questions** (only if needed)
  - **Suggested next step** (assign / merge / request-info / hotfix / schedule)
- Memory across the whole session, so the agent can spot duplicates between bugs you paste 5 minutes apart.
- Type `list` to see all bugs seen so far. Type `chat <message>` for non-bug questions. Type `quit` to exit.

## Files

- [`defect_triage_assistant.py`](defect_triage_assistant.py) — full version with interactive loop and class-based agent

## Run it

```powershell
# LM Studio must be running with a model loaded (Video 5)
python defect_triage_assistant.py
```

Then paste something like:

```
On Android 14, when the user has 3+ saved cards and taps "Pay",
the spinner runs forever and the app eventually freezes.
```

…and watch it return a structured triage decision.

## Make it your own

Stretch ideas worth one bullet on your résumé:

- **Persist** `agent.bugs_seen` to a JSON file so closing the app doesn't lose memory.
- **Summarize the triage day** at exit: severity counts + most common owner areas.
- **Auto-tag**: parse the markdown the model returned and write a CSV of `bug_id,severity,owner,dup_of`.
- **Embeddings + semantic dup detection** using `sentence-transformers` (later course material) — rank prior bugs by similarity before sending to the model.
