# Minimal Poe Server Bot (Modal + FastAPI)

This repo contains a minimal test bot for [Poe server bots](https://creator.poe.com/docs/server-bots) deployed on Modal.

## What this bot does

- Implements Poe server bot protocol using `fastapi-poe`
- Exposes the required endpoints via `fp.make_app(...)`
- Replies with a simple echo message: `Echo: <your message>`

## Files

- `bot.py` - Bot logic and FastAPI app creation
- `modal_app.py` - Modal ASGI deployment entrypoint
- `requirements.txt` - Python dependencies

## 1) Local test

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# optional: set your Poe access key for local testing
export POE_ACCESS_KEY="your_poe_access_key"

uvicorn bot:app --host 0.0.0.0 --port 8000
```

## 2) Deploy to Modal

Install Modal CLI and log in:

```bash
pip install modal
modal token new
```

Create a Modal secret (must be named `poe-secrets` to match `modal_app.py`):

```bash
modal secret create poe-secrets POE_ACCESS_KEY="your_poe_access_key"
```

Deploy:

```bash
modal deploy modal_app.py
```

Modal prints a public URL for your app. Use that URL in Poe when creating your server bot.

## 3) Connect bot on Poe

1. Go to [Poe bot creator](https://poe.com/create_bot?server=1)
2. Choose **Server bot**
3. Paste your deployed Modal URL
4. Save and test in Poe chat