from fastapi import FastAPI
from app.routes.chat import router as chat_router
from app.routes.speech import router as speech_router

app = FastAPI(
    title="Elderly Care NLP Chatbot",
    version="1.0.0"
)

app.include_router(chat_router)

app.include_router(speech_router)

@app.get("/")
def root():
    return {
        "message": "Elderly Care NLP Chatbot API Running"
    }