from langdetect import detect
from deep_translator import GoogleTranslator


def detect_language(text: str):

    try:
        language = detect(text)
        return language

    except Exception:
        return "unknown"


def translate_to_english(text: str, source_language: str):

    try:
        if source_language == "en":
            return text

        translated = GoogleTranslator(
            source='auto',
            target='en'
        ).translate(text)

        return translated

    except Exception:
        return text