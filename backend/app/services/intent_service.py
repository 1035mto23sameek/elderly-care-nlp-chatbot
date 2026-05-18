from transformers import pipeline


classifier = pipeline(
    "text-classification",
    model="app/models/intent_classifier"
)


LABEL_MAPPING = {
    "LABEL_0": "diet_suggestion",
    "LABEL_1": "doctor_booking",
    "LABEL_2": "emotional_support",
    "LABEL_3": "exercise_suggestion",
    "LABEL_4": "medication_reminder",
    "LABEL_5": "transport_booking"
}


def predict_intent(text: str):

    prediction = classifier(text)

    predicted_label = prediction[0]["label"]

    confidence = prediction[0]["score"]

    intent = LABEL_MAPPING.get(
        predicted_label,
        "unknown"
    )

    return {
        "intent": intent,
        "confidence": confidence
    }