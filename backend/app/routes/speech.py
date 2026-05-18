import os

from fastapi import APIRouter, UploadFile, File

from app.services.speech_service import transcribe_audio


router = APIRouter()


UPLOAD_DIR = "app/audio_uploads"


@router.post("/speech-to-text")
async def speech_to_text(
    audio: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        audio.filename
    )

    with open(file_path, "wb") as buffer:

        buffer.write(
            await audio.read()
        )

    transcription = transcribe_audio(
        file_path
    )

    return {
        "filename": audio.filename,
        "transcription": transcription
    }