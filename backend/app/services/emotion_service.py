from transformers import pipeline


emotion_classifier = pipeline(
    task="text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)


def detect_emotion(text: str):

    predictions = emotion_classifier(text)

    predictions = predictions[0]

    best_prediction = max(
        predictions,
        key=lambda x: x["score"]
    )

    emotion = best_prediction["label"]

    confidence = best_prediction["score"]

    return {
        "emotion": emotion,
        "confidence": confidence
    }