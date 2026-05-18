from app.services.knowledge_service import retrieve_knowledge


samples = [
    "I have stress",
    "Suggest exercise",
    "I cannot sleep properly",
    "Tell me about nutrition"
]


for text in samples:

    result = retrieve_knowledge(text)

    print("\\nTEXT:", text)

    print("KNOWLEDGE:", result)