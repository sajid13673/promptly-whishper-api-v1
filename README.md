# Promptly Whisper API

A lightweight **speech-to-text API** built with **FastAPI** and **Faster-Whisper**.

This service is responsible for converting recorded audio into text and is used by the Promptly frontend to provide voice input functionality in the AI chat interface.

## ✨ Features

* 🎙️ Audio-to-text transcription
* ⚡ FastAPI REST API
* 🤖 Powered by Faster-Whisper
* 🌍 English language transcription
* 📤 Accepts uploaded audio files
* 🔌 Simple API integration with web and mobile clients
* 🧩 Designed as a standalone service for Promptly

## 🛠️ Tech Stack

* **Python 3.12+**
* **FastAPI**
* **Uvicorn**
* **Faster-Whisper**
* **Pydantic**

## 📁 Project Structure

```text
whisper-api/
├── app.py
├── test.py
├── requirements.txt
├── .gitignore
└── .venv/
```

> The project structure may change as the API evolves.

## ⚡ Getting Started

### Prerequisites

Make sure you have the following installed:

* [Python](https://www.python.org/) 3.12+
* pip
* Git

### Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git

cd whisper-api
```

### Create a Virtual Environment

#### Windows

```powershell
python -m venv .venv
```

Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🤖 Faster-Whisper Model

The API uses the **Faster-Whisper** implementation of OpenAI's Whisper speech recognition model.

The model is loaded when the application starts.

For example:

```python
from faster_whisper import WhisperModel

model = WhisperModel("base")
```

The model may be downloaded automatically the first time the application runs.

### Model Size

The project currently uses the:

```text
base
```

model.

Faster-Whisper provides different model sizes with different trade-offs between transcription accuracy, processing speed, and resource requirements.

## 🚀 Running the API

Start the FastAPI application using Uvicorn:

```bash
uvicorn app:app --reload --port 8001
```

The API will be available at:

```text
http://localhost:8001
```

Interactive API documentation is available at:

```text
http://localhost:8001/docs
```

ReDoc documentation:

```text
http://localhost:8001/redoc
```

## 🎙️ Transcription API

### `POST /transcribe`

Transcribes an uploaded audio file and returns the recognized text.

### Request

The endpoint expects a multipart form-data request containing an audio file.

Example using `curl`:

```bash
curl -X POST "http://localhost:8001/transcribe" \
  -H "Accept: application/json" \
  -F "file=@audio.webm"
```

### Example Response

```json
{
  "text": "Hello, how are you today?"
}
```

## 🌍 Supported Language

The current Promptly voice-input implementation supports **English**.

If the application receives an unsupported language, the client should display:

```text
Only English language is currently supported.
```

The API can be extended to support additional languages in the future.

## 🔗 Promptly Integration

The Whisper API is one of the services used by the Promptly application.

```text
┌──────────────────────┐
│   Promptly Frontend  │
│       Next.js        │
└──────────┬───────────┘
           │
           │ Audio File
           ▼
┌──────────────────────┐
│    Whisper API       │
│      FastAPI         │
│   Faster-Whisper     │
└──────────┬───────────┘
           │
           │ Transcribed Text
           ▼
┌──────────────────────┐
│   Promptly Frontend  │
│    Chat Input        │
└──────────────────────┘
```

The frontend records the user's voice, sends the recorded audio to this API, receives the transcription, and places the resulting text into the chat input.

## 🔧 Frontend Configuration

The Promptly frontend can be configured to communicate with the transcription API using an environment variable:

```env
NEXT_PUBLIC_TRANSCRIBER_API_URL=http://localhost:8001
```

The frontend can then send the recorded audio to:

```text
POST {TRANSCRIBER_API_URL}/transcribe
```

## 🧪 Testing

Start the API:

```bash
uvicorn app:app --reload --port 8001
```

Then open:

```text
http://localhost:8001/docs
```

Use the Swagger UI to test the `/transcribe` endpoint by uploading an audio file.

You can also test the API from the command line:

```bash
curl -X POST "http://localhost:8001/transcribe" \
  -F "file=@audio.webm"
```

## 🌐 CORS

When the API is accessed from a browser-based frontend, the appropriate frontend origin must be allowed through FastAPI CORS configuration.

For local development, the Promptly frontend typically runs on:

```text
http://localhost:3000
```

Example:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

For production, replace the development origin with the actual frontend domain rather than allowing every origin.

## 🔐 Environment & Security

Do not commit sensitive configuration or credentials to the repository.

The following should generally be excluded from Git:

```text
.venv/
__pycache__/
.env
*.pyc
```

The downloaded Whisper model files should also not be committed to the repository.

## 📌 Project Status

This project is currently being developed as the speech-to-text service for **Promptly v1**.

The current implementation focuses on:

* Audio upload
* English speech-to-text transcription
* Integration with the Promptly chat interface

Additional languages, authentication, file validation, and production optimizations may be added in future versions.

## 🔗 Related Repository

### Promptly Frontend

The Next.js frontend that consumes this transcription API:

[Promptly Frontend – Next.js](https://github.com/sajid13673/promptly-frontend-nextjs-v1)

### Promptly Backend

The Laravel API responsible for the main Promptly application:

```text
<add-backend-repository-url>
```

## 📄 License

This project is for personal/learning purposes.
