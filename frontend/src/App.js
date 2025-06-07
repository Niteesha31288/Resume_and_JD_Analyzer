import React, { useState } from 'react';
import './index.css';

function App() {
  const [resume, setResume] = useState(null);
  const [jd, setJd] = useState('');
  const [result, setResult] = useState('');

  const handleAnalyze = async () => {
    const formData = new FormData();
    formData.append('file', resume);

    const resumeText = await fetch('http://127.0.0.1:8000/extract-text/', {
      method: 'POST',
      body: formData,
    }).then(res => res.text());

    const analysis = await fetch('http://127.0.0.1:8000/analyze/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ resume_text: resumeText, jd_text: jd }),
    }).then(res => res.json());

    const formatted = analysis.result
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>') // bold
      .replace(/\n/g, '<br />'); // new lines

    setResult(formatted);
  };

  return (
    <div className="container">
      <h1>Resume and JD Analysis</h1>
      <form>
        <input
          type="file"
          accept=".pdf,.docx"
          onChange={(e) => setResume(e.target.files[0])}
        />
        <textarea
          placeholder="Paste Job Description..."
          value={jd}
          onChange={(e) => setJd(e.target.value)}
        />
        <button type="button" onClick={handleAnalyze}>
          Analyze
        </button>
      </form>
      {result && (
        <div
          className="result-box"
          dangerouslySetInnerHTML={{ __html: result }}
        />
      )}
    </div>
  );
}

export default App;




