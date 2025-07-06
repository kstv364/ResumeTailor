import { useState } from 'react';
import './App.css';

function App() {
  const [resumeUrl, setResumeUrl] = useState('');
  const [jobDescription, setJobDescription] = useState('');
  const [llmOutput, setLlmOutput] = useState('');
  const [latexCode, setLatexCode] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleGenerate = async () => {
    setError('');
    setLlmOutput('');
    setLatexCode('');
    setLoading(true);
    try {
      // 1. Upload resume URL to backend
      const uploadRes = await fetch('http://localhost:8000/upload/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ file_url: resumeUrl }),
      });
      if (!uploadRes.ok) throw new Error('Failed to upload resume URL');
      const uploadData = await uploadRes.json();
      const resume_id = uploadData.resume_id;

      // 2. Send resume_id and JD to /tailor/
      const tailorRes = await fetch('http://localhost:8000/tailor/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ resume_id, job_description: jobDescription }),
      });
      if (!tailorRes.ok) throw new Error('Failed to tailor resume');
      const tailorData = await tailorRes.json();
      setLlmOutput(tailorData.llm_response);
      setLatexCode(tailorData.latex_resume);
    } catch (err) {
      setError(err.message || 'Unknown error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>ResumeTailor</h1>
      <div className="input-panel">
        <input
          type="text"
          placeholder="Enter public resume URL"
          value={resumeUrl}
          onChange={e => setResumeUrl(e.target.value)}
          className="input"
        />
        <textarea
          placeholder="Paste job description (JD) here"
          value={jobDescription}
          onChange={e => setJobDescription(e.target.value)}
          className="textarea"
          rows={6}
        />
        <button onClick={handleGenerate} className="generate-btn" disabled={loading}>
          {loading ? 'Generating...' : 'Generate LaTeX'}
        </button>
        {error && <div style={{ color: 'red' }}>{error}</div>}
      </div>
      <div className="output-panel">
        <h2>LLM Output (Raw LaTeX)</h2>
        <pre className="code-block">
          <code>{llmOutput}</code>
        </pre>
        <h2>Cleaned LaTeX (Copy-Paste Ready)</h2>
        <pre className="code-block">
          <code>{latexCode}</code>
        </pre>
        <h2>Rendered TeX</h2>
        <div className="rendered-tex">
          {/* For real rendering, use a library like KaTeX or MathJax. Here, just display as plain text. */}
          <pre>{latexCode}</pre>
        </div>
      </div>
    </div>
  );
}

export default App;
