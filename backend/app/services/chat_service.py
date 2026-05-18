from app.services.language_service import (
    detect_language,
    translate_to_english
)

from app.services.preprocessing_service import clean_text

from app.services.intent_service import predict_intent

from app.services.emotion_service import detect_emotion


def generate_response(message: str):

    # LANGUAGE DETECTION
    detected_language = detect_language(message)

    # TRANSLATION
    translated_text = translate_to_english(
        message,
        detected_language
    )

    # TEXT CLEANING
    cleaned_text = clean_text(translated_text)

    # INTENT PREDICTION
    intent_result = predict_intent(cleaned_text)

    predicted_intent = intent_result["intent"]

    # EMOTION PREDICTION
    emotion_result = detect_emotion(cleaned_text)

    predicted_emotion = emotion_result["emotion"]

    # RESPONSE GENERATION

    if predicted_intent == "emotional_support":

        if predicted_emotion == "sadness":

            response = (
                "I understand you may be feeling sad. "
                "Would you like calming music or breathing exercises?"
            )

        elif predicted_emotion == "fear":

            response = (
                "It is okay to feel worried sometimes. "
                "I am here with you."
            )

        elif predicted_emotion == "joy":

            response = (
                "I am glad you are feeling positive today."
            )

        elif predicted_emotion == "anger":

            response = (
                "Let us try some relaxation activities together."
            )

        else:

            response = (
                "I am here to support your emotional wellbeing."
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

        response = (
            "I am here to support you."
        )

    return {
        "detected_language": detected_language,
        "translated_text": translated_text,
        "cleaned_text": cleaned_text,
        "intent": predicted_intent,
        "emotion": predicted_emotion,
        "response": response
    }