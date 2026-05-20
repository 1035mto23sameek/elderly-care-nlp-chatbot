from app.services.language_service import (
    detect_language,
    translate_to_english
)

from app.services.preprocessing_service import clean_text

from app.services.intent_service import predict_intent

from app.services.emotion_service import detect_emotion

from app.services.memory_service import (
    save_message,
    get_last_messages
)

from app.services.knowledge_service import retrieve_knowledge

def generate_response(
    message: str,
    session_id: str
):

    # LANGUAGE DETECTION
    detected_language = detect_language(message)

    # TRANSLATION
    translated_text = translate_to_english(
        message,
        detected_language
    )

    # TEXT CLEANING
    cleaned_text = clean_text(translated_text)

    conversation_context = get_last_messages(session_id)

    # INTENT PREDICTION
    intent_result = predict_intent(cleaned_text)

    predicted_intent = intent_result["intent"]

    # EMOTION PREDICTION
    emotion_result = detect_emotion(cleaned_text)

    predicted_emotion = emotion_result["emotion"]

    save_message(
    session_id,
    "user",
    cleaned_text
    )

    knowledge_response = retrieve_knowledge(
        cleaned_text
    )

    # RESPONSE GENERATION

    if predicted_intent == "emotional_support":

        if predicted_emotion == "sadness":

            if len(conversation_context) > 0:

                response = (
                    "I understand you still seem emotionally low. "
                    "Would you like calming music or breathing exercises?"
                )

            else:

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
            "Please remember to take your medicines regularly and follow your doctor's recommendations carefully."
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
            "Healthy balanced meals with proper hydration and nutrition are important for maintaining elderly wellbeing."
        )

    elif predicted_intent == "exercise_suggestion":

        response = (
            "Regular walking, chair yoga, and light stretching exercises may help improve mobility and overall wellbeing."
        )

    else:

        response = (
            "I am here to support you."
        )


    save_message(
        session_id,
        "assistant",
        response
    )

    if knowledge_response:

        response += " " + knowledge_response

    return {
        "detected_language": detected_language,
        "translated_text": translated_text,
        "cleaned_text": cleaned_text,
        "intent": predicted_intent,
        "emotion": predicted_emotion,
        "context": conversation_context,
        "knowledge": knowledge_response,
        "response": response
    }