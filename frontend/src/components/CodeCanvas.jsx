import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { prism } from 'react-syntax-highlighter/dist/esm/styles/prism';

export default function CodeCanvas({ code }) {
  if (!code) return null;
  return (
    <div className="bg-white p-4 rounded shadow">
      <SyntaxHighlighter language="latex" style={prism} showLineNumbers>
        {code}
      </SyntaxHighlighter>
    </div>
  );
}