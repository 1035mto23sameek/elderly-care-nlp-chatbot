import json


with open(
    "app/knowledge_base/elderly_care.json",
    "r"
) as file:

    knowledge_base = json.load(file)


def retrieve_knowledge(text: str):

    text = text.lower()

    for item in knowledge_base:

        if item["topic"] in text:

            return item["content"]

    return None