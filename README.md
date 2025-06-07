Resume and Job Description Analyzer
This is an AI-powered resume analyzer web app that compares a resume (uploaded as PDF/DOCX or pasted text) with a job description (JD) and generates:

✅ ATS Match Score

📌 Matched and Missing Keywords

💡 GPT-style Smart Suggestions for resume improvement

📁 Project Structure

ai_resume_analyzer_project/
├── backend/
│   ├── main.py                 # FastAPI backend entry point
│   ├── utils.py                # Resume/JD processing logic
│   ├── requirements.txt        # Python dependencies
│   └── .env                    # (not included) contains OPENAI_API_KEY
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js              # Main React component
│   │   ├── index.js            # Entry point for React
│   │   └── index.css           # Custom styling
│   ├── package.json            # React app dependencies
│   └── README.md


⚙️ Tech Stack
Backend (FastAPI)
Language: Python

Libraries:
fastapi
python-docx
pdfplumber
openai
python-multipart
dotenv

Frontend (React)
React.js
CSS


🚀 How to Run
🔧 1. Backend Setup

cd resume_and_JD_analyzer_project/backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt


Create a .env file like this:
OPENAI_API_KEY=your_openai_key_here

Start the backend server:
uvicorn main:app --reload --port 8000


🎨 2. Frontend Setup 

cd resume_and_JD_analyzer_project/frontend
npm install
npm start

Runs the app at http://localhost:3000


alignment

📌 Sample Output:-

ATS Match Score: 85/100

Matched Skills:
- Java, Python, AWS, Agile, SQL, Docker, Kubernetes, CI/CD

Missing Areas:
- Optimization mathematics
- Ambiguous problem solving
- Communication of technical challenges

Suggestions:
1. Add examples of problem-solving under uncertainty.
2. Include keywords from job description in context.
3. Showcase cross-team collaboration results.
...

