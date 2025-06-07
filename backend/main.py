from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Union
from pathlib import Path
from tempfile import NamedTemporaryFile
from docx import Document
from pdfminer.high_level import extract_text
from dotenv import load_dotenv
import os

# ✅ Load .env from the same directory as main.py
env_path = os.path.join(os.path.dirname(__file__), ".env")
print("🔍 Loading .env from:", env_path)

# Try loading it
load_dotenv(dotenv_path=env_path)

# DEBUG: Read contents of .env to confirm
try:
    with open(env_path, "r") as f:
        print("📄 .env contents:\n", f.read())
except Exception as e:
    print("⚠️ Could not read .env file:", e)

# ✅ Fetch API key
api_key = os.getenv("OPENAI_API_KEY")
print("🔑 OpenAI Key Loaded:", api_key)

# ✅ Create OpenAI client
from openai import OpenAI
client = OpenAI(api_key=api_key)

# ✅ FastAPI app instance
app = FastAPI()

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Request model
class JDRequest(BaseModel):
    jd_text: str
    resume_text: str

# ✅ File upload endpoint
@app.post("/extract-text/")
async def extract_text_from_resume(file: UploadFile = File(...)):
    suffix = Path(file.filename).suffix.lower()
    contents = await file.read()

    if suffix == ".pdf":
        with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(contents)
            tmp_path = tmp.name
        text = extract_text(tmp_path)
        os.remove(tmp_path)
    elif suffix == ".docx":
        with NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            tmp.write(contents)
            tmp_path = tmp.name
        doc = Document(tmp_path)
        text = "\n".join([p.text for p in doc.paragraphs])
        os.remove(tmp_path)
    else:
        text = contents.decode("utf-8")

    return {"text": text}

# ✅ GPT-powered resume analysis
@app.post("/analyze/")
async def analyze(jd_data: JDRequest):
    jd = jd_data.jd_text
    resume = jd_data.resume_text

    prompt = f"""
You are an ATS and resume analysis expert.

Compare the resume below against the job description.

Return:
- An **ATS match score out of 100**
- A list of **matched skills or keywords**
- A list of **missing or weak areas**
- A few **GPT suggestions** to improve the resume

Job Description:
{jd}

Resume:
{resume}
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"result": response.choices[0].message.content}
