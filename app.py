from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import requests
import uvicorn
import json

app = FastAPI(title="Gemma Streaming Chat 🔥")

class ChatRequest(BaseModel):
    message: str
    history: list = []

def generate_stream(user_message: str, history: list):
    payload = {
        "model": "gemma2:2b",
        "messages": history + [{"role": "user", "content": user_message}],
        "stream": True
    }
    with requests.post("http://localhost:11434/api/chat", json=payload, stream=True) as r:
        for line in r.iter_lines():
            if line:
                data = json.loads(line)
                yield data["message"]["content"]

@app.post("/chat")
def chat_stream(request: ChatRequest):
    return StreamingResponse(generate_stream(request.message, request.history), media_type="text/plain")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)