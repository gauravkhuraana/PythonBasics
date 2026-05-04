# Video 5 — Run AI on Your Laptop with LM Studio

---

## What you'll get from this video

- A **local LLM** running on your own machine — no cloud, no API key, no usage cost.
- LM Studio's built-in **OpenAI-compatible server** running at `http://localhost:1234`.
- A model loaded that we'll connect to from Python in Video 6.

---

## Why local first?

| Local LLM | Cloud LLM |
|-----------|-----------|
| Free after download | Pay per token |
| Works offline | Needs internet |
| Your data stays on your machine | Sent to a provider |
| Slower & smaller models | Faster & state-of-the-art |
| Perfect for **learning** | Better for production |

We start local because the *Python code is identical* — only the URL and key change. Video 10 covers the cloud variant.

---

## 1. Install LM Studio

Download from **<https://lmstudio.ai/>**. It's a free desktop app for Windows, macOS, and Linux.

System hints:

- **At least 8 GB RAM**, ideally 16 GB.
- An SSD with ~5 GB free for one small model.
- A discrete GPU is great but **not required** — we'll use CPU-friendly models.

---

## 2. Download a starter model

Inside LM Studio:

1. Click the **Search / Discover** icon (magnifying glass).
2. Search for one of these beginner-friendly models (any will work):
   - `Llama 3.2 3B Instruct` (~2 GB)
   - `Phi-3 mini Instruct` (~2 GB)
   - `Qwen2.5 3B Instruct` (~2 GB)
3. Pick a **Q4** or **Q5** quantization (smaller, faster, fine for learning).
4. Click **Download**.

> 💡 "Quantization" = compressing the model weights. Q4 is ~4 bits per weight, Q8 is ~8 bits. Lower = smaller & faster but slightly lower quality. For this course, Q4 is plenty.

---

## 3. Test in the chat UI

1. Click the **Chat** icon (speech bubble).
2. At the top, **load** the model you just downloaded.
3. Type "Hello, what can you do?" and hit Enter.

If you get a coherent response — the model works. ✅

---

## 4. Start the local server

This is the part Video 6 needs.

1. Click the **Developer** / **Local Server** icon (`</>` in the sidebar).
2. At the top, **load** the same model.
3. Click **Start Server**.

You should see something like:

```
Server running on http://localhost:1234
GET  /v1/models
POST /v1/chat/completions
```

That's an **OpenAI-compatible API**. The `openai` Python SDK can talk to it without any code changes — we just point it at `localhost`.

### Sanity check (optional, in the terminal)

```powershell
curl http://localhost:1234/v1/models
```

Should return JSON listing the loaded model.

---

## 5. Note your model name

In the LM Studio Server tab, look at the model identifier — something like:

```
lmstudio-community/Llama-3.2-3B-Instruct-GGUF
```

Or simply `llama-3.2-3b-instruct`. **Copy it** — we'll put it in `.env` in Video 6.

---

## 🛟 Troubleshooting

| Problem | Fix |
|---------|-----|
| Model loads but is very slow | Try a smaller (3B or under) Q4 model |
| "Out of memory" errors | Lower context length in server settings to 2048 |
| Port 1234 already in use | Change to 1235 in server settings; update `.env` accordingly |
| Server tab is empty | Make sure you loaded a model **before** clicking Start |

---

## ✅ Keep LM Studio running

Don't close it — Video 6 will connect to this exact server.

Next: [Video 6](06_first_local_ai_call_README.md) — your first Python → Local LLM program.
