from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from openai import OpenAI
import tempfile
import os

app = FastAPI()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key="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") 
 
@app.get("/")
def home():
    return {"status": "ok", "msg": "Server attivo2 🚀"}

@app.post("/audio")
async def audio_endpoint(file: UploadFile = File(...)):

    # salva file temporaneo
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    # 🎤 Speech-to-Text
    with open(tmp_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=audio_file
        )

    user_text = transcript.text

    print("Testo utente:", user_text)

    # 💬 ChatGPT
    chat = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Rispondi in modo breve."},
            {"role": "user", "content": user_text}
        ]
    )

    reply = chat.choices[0].message.content

    print("Risposta:", reply)

    return JSONResponse({
        "input_text": user_text,
        "reply": reply
    })
    
