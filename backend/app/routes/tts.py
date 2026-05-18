from fastapi import APIRouter

from fastapi.responses import FileResponse

from app.services.tts_service import generate_speech


router = APIRouter()


@router.get("/text-to-speech")
def text_to_speech(text: str):

    audio_path = generate_speech(text)

    return FileResponse(
        audio_path,
        media_type="audio/mpeg",
        filename="response.mp3"
    )