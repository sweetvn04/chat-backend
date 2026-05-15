from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware # solve cors issue

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status" : "server is running!"}

@app.post("/chat")
def chat(request: ChatRequest):
    return {"reply": "I recieved " + request.message}


