from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI(
    title="Elderly Care NLP Chatbot",
    version="1.0.0"
)

app.include_router(chat_router)

@app.get("/")
def root():
    return {
        "message": "Elderly Care NLP Chatbot API Running"
    }