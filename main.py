from fastapi import FastAPI, Request, HTTPException
from typing import Optional
import os
from datetime import datetime

app = FastAPI()

verify_token = os.environ.get("VERIFY_TOKEN")


@app.get("/")
async def verify_webhook(
    mode: Optional[str] = None,
    challenge: Optional[str] = None,
    verify_token: Optional[str] = None,
):
    if mode == "subscribe" and verify_token == verify_token:
        print("WEBHOOK VERIFIED")
        return challenge
    else:
        raise HTTPException(status_code=403)


@app.post("/")
async def receive_webhook(request: Request):
    timestamp = datetime.now().isoformat(sep=" ", timespec="seconds")
    print(f"\n\nWebhook received {timestamp}\n")
    body = await request.json()
    print(body)
    return {}
