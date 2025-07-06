import React, { useEffect, useRef } from 'react';

export default function LatexRenderPanel({ code }) {
  const container = useRef(null);

  useEffect(() => {
    if (code && window.latex) {
      const generator = new window.latexjs.HtmlGenerator({ hyphenate: false });
      const latex = window.latexjs.parse(code, { generator: generator }).htmlDocument();
      container.current.innerHTML = latex;
    }
  }, [code]);

  return (
    <div className="bg-white p-4 rounded shadow overflow-auto">
      <div ref={container}></div>
    </div>
  );
}