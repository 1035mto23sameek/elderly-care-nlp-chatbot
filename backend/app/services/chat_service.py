from app.services.language_service import (
    detect_language,
    translate_to_english
)

from app.services.preprocessing_service import clean_text
from app.services.intent_service import predict_intent

def generate_response(message: str):

    detected_language = detect_language(message)

    translated_text = translate_to_english(
        message,
        detected_language
    )

    cleaned_text = clean_text(translated_text)

    intent_result = predict_intent(cleaned_text)

    predicted_intent = intent_result["intent"]

    if predicted_intent == "emotional_support":

        response = (
            "I understand how you feel. "
            "Would you like calming music or breathing exercises?"
        )

    elif predicted_intent == "medication_reminder":

        response = (
            "Please remember to take your medicines on time."
        )

    elif predicted_intent == "doctor_booking":

        response = (
            "I can help you with doctor appointment support."
        )

    elif predicted_intent == "transport_booking":

        response = (
            "Transport booking assistance is available."
        )

    elif predicted_intent == "diet_suggestion":

        response = (
            "I can suggest healthy nutrition plans for you."
        )

    elif predicted_intent == "exercise_suggestion":

        response = (
            "Gentle exercises and yoga may help you stay active."
        )

    else:

        response = "I am here to support you."

    return {
        "detected_language": detected_language,
        "translated_text": translated_text,
        "cleaned_text": cleaned_text,
        "intent": predicted_intent,
        "response": response
        
    }