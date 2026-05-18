from fastapi import APIRouter

from app.services.chat_service import generate_response

router = APIRouter()


@router.get("/chat")
def chat(message: str, session_id: str = "default_user"):

    result = generate_response(
        message,
        session_id
    )

    return {
        "session_id": session_id,
        "user_message": message,
        "detected_language": result["detected_language"],
        "translated_text": result["translated_text"],
        "cleaned_text": result["cleaned_text"],
        "predicted_intent": result["intent"],
        "predicted_emotion": result["emotion"],
        "conversation_context": result["context"],
        "bot_response": result["response"]
    }