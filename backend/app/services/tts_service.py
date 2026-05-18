import uuid

from gtts import gTTS


def generate_speech(text: str):

    filename = f"{uuid.uuid4()}.mp3"

    output_path = f"app/audio_responses/{filename}"

    tts = gTTS(
        text=text,
        lang="en"
    )

    tts.save(output_path)

    return output_path