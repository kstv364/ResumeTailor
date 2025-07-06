import React from 'react';

export default function ResumeUrlInput({ value, onChange }) {
  return (
    <div>
      <label className="block font-medium mb-1">Resume URL:</label>
      <input
        type="text"
        value={value}
        onChange={e => onChange(e.target.value)}
        placeholder="https://.../resume.pdf"
        className="w-full p-2 border rounded"
      />
    </div>
  );
}