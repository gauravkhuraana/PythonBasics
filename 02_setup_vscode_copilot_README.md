# Video 2 — Setting Up Your AI Workshop

> **Duration:** 8–10 minutes · **Type:** Install walkthrough

---

## 🎯 What you'll get from this video

By the end you'll have:

- ✅ Python 3.11+ installed and verified
- ✅ VS Code installed with the Python extension
- ✅ Your first `hello.py` running from both the terminal and the VS Code Run button
- ✅ GitHub Copilot installed and signed in (we'll *use* it deeply in Video 9)

---

## 1. Install Python

Download from **<https://www.python.org/downloads/>** → install the latest 3.11+ release.

**Windows users — important:** ✅ tick the box **"Add python.exe to PATH"** on the first install screen. Easy to miss; painful to fix later.

### Verify

```powershell
python --version
```

Expected: `Python 3.11.x` or higher. If you see "command not found", PATH isn't set — re-run the installer.

---

## 2. Install VS Code

Download from **<https://code.visualstudio.com/>**. Default options are fine.

### Install the essentials (Extensions panel: `Ctrl+Shift+X`)

1. **Python** — Microsoft (gives you IntelliSense, Run, Debug)
2. **GitHub Copilot** — sign in with your GitHub account
3. **GitHub Copilot Chat**

> 💡 If you don't have Copilot, you can still complete the entire course. Video 9 is the only Copilot-specific lesson and it will still teach you the patterns.

---

## 3. Your first program

Create a new file `hello.py`:

```python
print("Hello, AI!")
name = "Future AI builder"
print(f"Welcome, {name}.")
```

### Run it 3 ways

**A. From a terminal in VS Code** (open with `` Ctrl+` ``):

```powershell
python hello.py
```

**B. Click the ▶️ "Run Python File" button** (top-right of the editor).

**C. Right-click the editor → Run Python → Run Python File in Terminal.**

All three should print:

```
Hello, AI!
Welcome, Future AI builder.
```

---

## 4. Sign into GitHub Copilot

1. Click the Copilot icon in the bottom-right status bar.
2. Sign in with GitHub.
3. Authorize VS Code in your browser.

Quick sanity check: open `hello.py`, type a comment like `# print numbers from 1 to 5` on a new line, press **Enter**, and Copilot should suggest a `for` loop in grey ghost text. **Tab** to accept.

---

## 🛟 Troubleshooting

| Problem | Fix |
|---------|-----|
| `python` not recognised on Windows | Re-run installer → tick "Add to PATH" |
| Mac says "command not found" | Try `python3` instead of `python` |
| VS Code Run button doesn't appear | Open a `.py` file; install the Python extension |
| Copilot suggestions don't show | Bottom-right status bar → click Copilot icon → check sign-in |

---

## ✅ Done?

You're ready for [Video 3](03_python_essentials_README.md), where we'll learn just enough Python to talk to an AI.
