from app.services.emotion_service import detect_emotion


samples = [
    "I feel lonely today",
    "I am very happy today",
    "I am scared about my health",
    "I feel anxious and stressed",
    "I miss my family"
]


for text in samples:

    result = detect_emotion(text)

    print("\\nTEXT:", text)

    print("EMOTION:", result)