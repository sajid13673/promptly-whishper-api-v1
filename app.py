from fastapi import FastAPI, UploadFile, File
from faster_whisper import WhisperModel
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Loading Whisper model...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Whisper model loaded!")


@app.get("/")
def root():
    return {
        "message": "Whisper API is running!"
    }

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    suffix = os.path.splitext(file.filename)[1] or ".webm"

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_audio:
        temp_audio.write(await file.read())
        temp_path = temp_audio.name

    try:
        segments, info = model.transcribe(temp_path)

        text = " ".join(segment.text for segment in segments).strip()

        return {
            "language": info.language,
            "text": text
        }

    finally:
        os.remove(temp_path)