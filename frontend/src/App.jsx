import { useState } from 'react';
import './App.css';

function App() {
  const [resumeUrl, setResumeUrl] = useState('');
  const [jobDescription, setJobDescription] = useState('');
  const [latexCode, setLatexCode] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [copySuccess, setCopySuccess] = useState('');

  const handleGenerate = async () => {
    setError('');
    setLatexCode('');
    setLoading(true);
    try {
      const uploadRes = await fetch('/upload/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ file_url: resumeUrl }),
      });
      if (!uploadRes.ok) throw new Error('Failed to upload resume URL');
      const uploadData = await uploadRes.json();
      const resume_id = uploadData.resume_id;

      const tailorRes = await fetch('/tailor/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ resume_id, job_description: jobDescription }),
      });
      if (!tailorRes.ok) throw new Error('Failed to tailor resume');
      const tailorData = await tailorRes.json();
      setLatexCode(tailorData.latex_resume);
    } catch (err) {
      setError(err.message || 'Unknown error');
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(latexCode);
    setCopySuccess('Copied!');
    setTimeout(() => setCopySuccess(''), 2000);
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
        <div className="code-block">
          {copySuccess && <div className="copy-success">{copySuccess}</div>}
          <button onClick={handleCopy} className="copy-button">
            Copy
          </button>
          <code>{latexCode}</code>
        </div>
      </div>
    </div>
  );
}

export default App;
