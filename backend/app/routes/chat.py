from fastapi import APIRouter
from app.services.chat_service import generate_response

router = APIRouter()


@router.get("/chat")
def chat(message: str):

    result = generate_response(message)

    return {
        "user_message": message,
        "detected_language": result["detected_language"],
        "translated_text": result["translated_text"],
        "cleaned_text": result["cleaned_text"],
        "predicted_intent": result["intent"],
        "predicted_emotion": result["emotion"],
        "bot_response": result["response"]
    }