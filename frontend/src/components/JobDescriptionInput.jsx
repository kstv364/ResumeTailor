import React, { useState } from 'react';
import 'react-quill/dist/quill.snow.css';
import ReactQuill from 'react-quill';

export default function JobDescriptionInput({ value, onChange }) {
  return (
    <div>
      <label className="block font-medium mb-1">Job Description:</label>
      <ReactQuill
        theme="snow"
        value={value}
        onChange={onChange}
        modules={{ toolbar: [['bold', 'italic'], ['link'], [{ list: 'bullet' }]] }}
        formats={[ 'bold', 'italic', 'link', 'list', 'bullet' ]}
      />
    </div>
  );
}
