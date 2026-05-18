from app.services.intent_service import predict_intent


samples = [
    "I feel lonely",
    "Book a doctor appointment",
    "Suggest yoga exercises",
    "Remind me medicine"
]


for text in samples:

    result = predict_intent(text)

    print("\\nTEXT:", text)

    print("PREDICTED:", result)