from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok", "msg": "Server attivo 🚀"}

# Simula pipeline audio → AI → risposta
@app.post("/audio")
async def audio_endpoint(file: UploadFile = File(...)):

    # Legge il file ricevuto (audio dall'ESP32)
    data = await file.read()
    size = len(data)

    print(f"Ricevuto audio: {size} bytes")

    # 👉 QUI normalmente faresti:
    # - Whisper (audio → testo)
    # - ChatGPT (testo → risposta)
    # - TTS (testo → audio)

    # Per test semplificato ritorniamo solo una risposta finta
    fake_response = {
        "received_bytes": size,
        "message": "Audio ricevuto correttamente 🎧",
        "reply": "Ciao! Il tuo ESP32 sta comunicando con il server 👍"
    }

    return JSONResponse(fake_response)