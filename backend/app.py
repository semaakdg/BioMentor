from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "AIzaSyAZVjKD3lvlqlEwxusCZ08OH0d68viPIEw"

class PlanRequest(BaseModel):
    goal: str

class ChatRequest(BaseModel):
    question: str

def call_gemini_api(prompt: str):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": API_KEY}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        response = requests.post(url, headers=headers, params=params, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
    except Exception as e:
        return f"Hata: {str(e)}"

@app.post("/plan")
def generate_plan(data: PlanRequest):
    prompt = f"""
    Kullanıcı '{data.goal}' hedefi seçti.

    Ona 7 günlük detaylı bir plan oluştur. Yanıtı şu formatta döndür:

    Kısa Öneriler:
    - Günlük yapılacak 3 ana tavsiye

    Detaylar:
    - 1. Gün: Açıklama
    - 2. Gün: Açıklama
    - 3. Gün: Açıklama
    - 4. Gün: Açıklama
    - 5. Gün: Açıklama
    - 6. Gün: Açıklama
    - 7. Gün: Açıklama

    Uyarı:
    - Bu öneriler tıbbi tavsiye yerine geçmez.
    """
    answer = call_gemini_api(prompt)
    return {"answer": answer}

@app.post("/chat")
def chat_with_ai(data: ChatRequest):
    prompt = f"""
    Kullanıcının sorusu: {data.question}

    Ona ilaçsız ve doğal yöntemlere dayalı, bilimsel kaynaklarla desteklenmiş bir yanıt ver.
    Yanıtı şu formatta döndür:

    Kısa Öneriler:
    - Öneri 1
    - Öneri 2
    - Öneri 3

    Detaylar:
    - Öneri 1 açıklaması
    - Öneri 2 açıklaması
    - Öneri 3 açıklaması

    Uyarı:
    - Bu öneriler tıbbi tavsiye yerine geçmez.
    """
    answer = call_gemini_api(prompt)
    return {"answer": answer}
