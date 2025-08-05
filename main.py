from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import PlainTextResponse
from typing import Optional
import os
from datetime import datetime

app = FastAPI()


verify_token = os.environ.get("VERIFY_TOKEN")

@app.get("/", response_class=PlainTextResponse)
async def verify_webhook(request: Request):
    # Extract query parameters with dotted names
    mode = request.query_params.get("hub.mode")
    challenge = request.query_params.get("hub.challenge")
    token = request.query_params.get("hub.verify_token")

    if mode == "subscribe" and token == verify_token:
        print("WEBHOOK VERIFIED")
        return PlainTextResponse(content=challenge, status_code=200)
    else:
        raise HTTPException(status_code=403)

@app.post("/")
async def receive_webhook(request: Request):
    timestamp = datetime.now().isoformat(sep=" ", timespec="seconds")
    print(f"\n\nWebhook received {timestamp}\n")
    body = await request.json()
    print(body)
    return {}
