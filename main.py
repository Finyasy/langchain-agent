from fastapi import FastAPI, Request

from chatbot_agent import conversation

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Teams Chatbot API. Use /api/messages to interact."}


@app.post("/api/messages")
async def messages(request: Request):
    data = await request.json()
    user_input = data.get("text", "Hello")

    response = conversation.predict(input=user_input)

    return {"type": "message", "text": response}