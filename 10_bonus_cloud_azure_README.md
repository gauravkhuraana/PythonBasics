# Video 10 — Bonus: Connect to Cloud AI (Azure OpenAI)

> **Duration:** 10–12 minutes · **Type:** Optional / cloud follow-up

---

## 🎯 What you'll see

- The exact same prompt from Video 6, sent to **Azure OpenAI** instead of LM Studio.
- The 2-line code change that swaps local for cloud.
- When local makes more sense vs when cloud does.

**Files for this video:**
- [10_bonus_cloud_azure.py](10_bonus_cloud_azure.py) — full annotated version
- [10_bonus_cloud_azure_short.py](10_bonus_cloud_azure_short.py) — minimal demo

---

## The 2-line change

```diff
- from openai import OpenAI
+ from openai import AzureOpenAI
+ from azure.identity import DefaultAzureCredential, get_bearer_token_provider

- client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
+ credential = DefaultAzureCredential()
+ token_provider = get_bearer_token_provider(credential,
+     "https://cognitiveservices.azure.com/.default")
+ client = AzureOpenAI(
+     azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
+     azure_ad_token_provider=token_provider,
+     api_version="2024-12-01-preview",
+ )
```

Everything below `client = …` (the `messages` list, the `chat.completions.create` call, parsing `response.choices[0].message.content`) is **identical**.

That's the point: build against the OpenAI SDK and you can swap providers later.

---

## Local vs Cloud — when to pick which

| Need | Pick |
|------|------|
| Learning, hacking, weekend projects | **Local** (LM Studio) |
| Sensitive data must not leave the machine | **Local** |
| State-of-the-art quality (GPT-4 class) | **Cloud** |
| Production app with paying users | **Cloud** |
| Hard SLAs, scaling, observability | **Cloud** |
| You don't have a GPU | **Cloud** for big models, **Local** for small |

---

## Prerequisites for this video

- An **Azure OpenAI resource** with a deployment (e.g. `gpt-4o`, `gpt-4o-mini`).
- `az login` completed in your terminal (we use Azure AD auth — no API key in code).
- `.env` filled in:
  ```
  AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
  AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
  ```

> 💡 No Azure account? You can also use **plain OpenAI** by switching to `OpenAI(api_key=...)` with your OpenAI API key. The SDK is the same.

---

## Cost note (Azure OpenAI)

Cloud APIs charge per **token**. Always check `response.usage` in the early days of a project so the bill never surprises you.

---

Next: [Video 11](11_next_steps_README.md) — wrap-up + your capstone.
