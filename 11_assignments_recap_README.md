# Video 11 — Assignments: Key Concepts & Tips

---

## What this video covers

A focused walkthrough of the **core concept** behind each assignment — what it's *really* testing, the one pattern you must get right, and the tips that separate a good solution from a great one.

Think of this as your study guide before you submit, or your debrief after you're done.

---

## Assignment 1 — Test Case Catalog ⭐

**Files:** [assignments/assignment_1_test_case_catalog/](assignments/assignment_1_test_case_catalog/)

### What it's really testing

Pure Python data modelling. Before you can call an LLM or build anything smart, you need to be fluent with Python's two most important structures: **dictionaries** and **lists**.

### The one pattern to nail

Model every test case as a **single flat dictionary**:

```python
tc = {
    "id":        "TC-001",
    "title":     "Login with valid credentials",
    "module":    "login",
    "priority":  "High",
    "status":    "pass",
    "automated": True,
}
```

Then collect all of them in a **list** called `catalog`. Every operation in the assignment — display, filter, summarise — is just a loop over that list.

```python
catalog = [tc1, tc2, tc3, tc4, tc5]

for tc in catalog:
    print(tc["id"], tc["title"], tc["status"])
```

This dict-in-a-list pattern is *identical* to what you'll use for LLM message histories later:
```python
messages = [
    {"role": "system",    "content": "You are a QA assistant."},
    {"role": "user",      "content": "Write a test plan."},
    {"role": "assistant", "content": "..."},
]
```
Same shape. Learning it here pays off in every later assignment.

### Tips

- **Build the data first, logic second.** Create all 5 test case dicts and put them in the list before writing any functions.
- **Use f-strings for display.** `f"[{tc['id']}] {tc['title']} | {tc['module']}"` is cleaner than concatenation.
- **Filter with a list comprehension:**
  ```python
  login_cases = [tc for tc in catalog if tc["module"] == "login"]
  ```
- **Count statuses with `.count()`:**
  ```python
  statuses = [tc["status"] for tc in catalog]
  pass_count = statuses.count("pass")
  ```

---

## Assignment 2 — Bug Report Generator ⭐⭐

**Files:** [assignments/assignment_2_bug_report_generator/](assignments/assignment_2_bug_report_generator/)

### What it's really testing

Your first real LLM integration: load config securely, build a client, craft a system prompt, make a call, and extract the response. Every future AI project starts with these exact steps.

### The one pattern to nail

The **four-line LLM call**:

```python
response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user",   "content": user_input},
    ],
)
result = response.choices[0].message.content
```

Everything else (`.env` loading, client setup, printing) wraps these four lines.

### Key concepts

| Concept | Why it matters |
|---------|---------------|
| `python-dotenv` + `.env` | Never hard-code API keys or URLs in source code |
| `OpenAI(base_url=..., api_key=...)` | Same client constructor works for LM Studio, OpenAI, Azure, OpenRouter — only the params change |
| System prompt | Sets the *persona and output format* — write it in plain English first, then paste into code |
| `response.choices[0].message.content` | The exact path to the model's reply — memorise this |

### Tips

- **Write the system prompt in plain English first.** Describe the output you want as if briefing a colleague. Then wrap it in a Python string. Prompt quality matters 10× more than code structure for this assignment.
- **Always print `response.usage`** while developing:
  ```python
  print(response.usage)
  # CompletionUsage(prompt_tokens=142, completion_tokens=310, total_tokens=452)
  ```
  It tells you if your prompt is ballooning and helps you tune `max_tokens`.
- **Keep `temperature` low (0.2–0.4)** for structured outputs like bug reports — you want consistency, not creativity.
- **Test with a one-liner bug description first** ("login crashes on iPhone"), get it working end-to-end, *then* add the multi-field input.

---

## Assignment 3 — QA Agent ⭐⭐⭐

**Files:** [assignments/assignment_3_qa_agent/](assignments/assignment_3_qa_agent/)

### What it's really testing

Building a **class-based agent** that can switch between multiple skills, routes the user's intent to the right prompt, and maintains a running conversation history — the architecture used by real AI agents.

### The one pattern to nail

Keep state **inside the class**, not in global variables:

```python
class QAAgent:
    def __init__(self, client, model):
        self.client = client
        self.model  = model
        self.history = [{"role": "system", "content": BASE_SYSTEM_PROMPT}]

    def chat(self, user_message, skill_prompt=None):
        # Inject skill context if routing determined a skill
        messages = self.history.copy()
        if skill_prompt:
            messages.insert(1, {"role": "system", "content": skill_prompt})
        messages.append({"role": "user", "content": user_message})
        response = self.client.chat.completions.create(
            model=self.model, messages=messages
        )
        reply = response.choices[0].message.content
        self.history.append({"role": "user",      "content": user_message})
        self.history.append({"role": "assistant", "content": reply})
        return reply
```

### Skill routing

Route by keyword detection — keep it simple:

```python
def detect_skill(user_input: str) -> str:
    text = user_input.lower()
    if any(w in text for w in ["test plan", "test cases", "scenarios"]):
        return "test_plan"
    if any(w in text for w in ["bug", "crash", "issue", "defect"]):
        return "triage"
    if any(w in text for w in ["passed", "failed", "skipped", "results"]):
        return "summary"
    if any(w in text for w in ["risk", "release", "ready", "quality"]):
        return "risk"
    return "general"
```

### Key concepts

| Concept | Why it matters |
|---------|---------------|
| Python class | Bundles state (`history`, `client`) and behaviour (`chat`, `detect_skill`) together |
| `self.history` list | The conversation's memory — must live on the instance, not a module-level variable |
| Skill routing | Keyword detection is simple and reliable enough for a demo; in production you'd ask the LLM itself to classify |
| Multiple system prompts | Each skill has its own persona; inject as a second system message on the fly |

### Tips

- **Build one skill end-to-end first** (e.g., `triage`): routing → correct system prompt → response. Only then add the other three skills. Adding all four at once makes debugging painful.
- **Print the detected skill label** during development so you can see what's being triggered:
  ```python
  skill = detect_skill(user_input)
  print(f"  🔧 [{skill}]")
  ```
- **Don't reset history between skill switches.** The whole point is that the agent remembers what it discussed earlier when assessing risk or writing a plan.
- **Keep each skill's system prompt short and specific.** One sentence of persona + 3 bullet points of output format is enough. Longer prompts don't reliably produce better results.

---

## Capstone — Defect Triage Assistant ⭐⭐⭐

**Files:** [assignments/capstone_options/](assignments/capstone_options/)

### What it's really testing

Everything from Assignments 1–3 plus **cross-bug memory**: the assistant remembers bugs it has already seen in this session and can spot patterns, suggest duplicate candidates, and flag clusters of related failures.

### The one pattern to nail

Decide up front **where cross-bug context lives**. Two options:

**Option A — Keep it in the shared history list**
Every bug discussion lands in the same `history` list, so the model automatically sees all previous bugs. Simple but the context window fills up after ~20 bugs.

**Option B — Separate bug log dict**
```python
self.bug_log = {}   # {"BUG-001": {title, severity, area, summary}, ...}
```
When a new bug comes in, inject a brief summary of related past bugs as a system message before asking the model to triage. Scales to hundreds of bugs.

For the course capstone, Option A is fine. Option B is the real-world approach.

### Key concepts

| Concept | Why it matters |
|---------|---------------|
| Persistent session state | Data that survives across multiple turns of the same run |
| Context injection | Feeding earlier results back into the prompt to enable cross-bug analysis |
| Interactive loop | `while True:` + clean `quit`/`exit` handling |
| Combined skills | Triage + pattern detection in one agent vs. separate agents |

### Tips

- **Start with the triage loop first** (single bug, good output). Cross-bug memory is an extension you bolt on after the core works.
- **Use a short bug ID** ("BUG-001", "BUG-002") so you can reference past bugs in prompts cleanly.
- **Cap context injection.** If using Option B, only inject the last 5 bugs as context — the model doesn't need the full backlog to spot recent patterns.
- **Test with realistic data.** Use actual bug titles from your day job (scrubbed of sensitive info). The model response quality is noticeably better when the input sounds real.

---

## 📌 Concept cheatsheet (all assignments)

| Concept | First appears | Used in |
|---------|:------------:|---------|
| Dict as data model | A1 | A1, A2, A3, Capstone |
| List of dicts | A1 | A1, A2 (messages), A3 (history) |
| `python-dotenv` / `.env` | A2 | A2, A3, Capstone |
| `OpenAI` client setup | A2 | A2, A3, Capstone |
| System prompt crafting | A2 | A2, A3, Capstone |
| `response.choices[0].message.content` | A2 | A2, A3, Capstone |
| Python class + `self` | A3 | A3, Capstone |
| `history` list (multi-turn) | A3 | A3, Capstone |
| Skill routing / intent detection | A3 | A3, Capstone |
| Cross-session state | Capstone | Capstone |

---

Next: [Wrap-Up & Your Next Steps](next_steps_README.md) — capstone brief and where to go from here.
