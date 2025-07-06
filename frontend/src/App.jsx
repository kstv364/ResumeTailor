import React , { useState } from 'react';
import ResumeUrlInput from './components/ResumeUrlInput';
import JobDescriptionInput from './components/JobDescriptionInput';
import CodeCanvas from './components/CodeCanvas';
import LatexRenderPanel from './components/LatexRenderPanel';

export default function App() {
  const [resumeUrl, setResumeUrl] = useState('');
  const [jobDesc, setJobDesc] = useState('');
  const [latexCode, setLatexCode] = useState('');

  const handleUpload = async () => {
    await fetch('http://localhost:8000/upload/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: 'resume-123', file_url: resumeUrl })
    });
  };

  const handleTailor = async () => {
    const res = await fetch('http://localhost:8000/tailor/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ resume_id: 'resume-123', job_description: jobDesc })
    });
    const data = await res.json();
    setLatexCode(data.latex_resume);
  };

  return (
    <div className="p-4 space-y-4 max-w-4xl mx-auto">
      <ResumeUrlInput value={resumeUrl} onChange={setResumeUrl} />
      <button onClick={handleUpload} className="px-4 py-2 bg-green-600 text-white rounded">Upload Resume</button>
      <JobDescriptionInput value={jobDesc} onChange={setJobDesc} />
      <button onClick={handleTailor} className="px-4 py-2 bg-blue-600 text-white rounded">Tailor Resume</button>
      <CodeCanvas code={latexCode} />
      <LatexRenderPanel code={latexCode} />
    </div>
  );
}