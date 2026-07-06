from fastapi import FastAPI
from faster_whisper import WhisperModel

app = FastAPI()

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