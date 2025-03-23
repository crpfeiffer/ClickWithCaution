import React, { useState } from 'react';
import axios from 'axios';

const AnalyzeText = () => {
    const [text, setText] = useState('');
    const [result, setResult] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/analyze', { text });
            setResult(response.data.result);
        } catch (error) {
            console.error('Error analyzing text:', error);
            setResult('An error occurred while analyzing the text.');
        }
    };

    return (
        <div>
            <h1>Scam Text Analyzer</h1>
            <form onSubmit={handleSubmit}>
                <textarea
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    placeholder="Enter text to analyze"
                    rows={5}
                    cols={50}
                />
                <br />
                <button type="submit">Analyze</button>
            </form>
            {result && (
                <div>
                    <h2>Analysis Result:</h2>
                    <p>{result}</p>
                </div>
            )}
        </div>
    );
};

export default AnalyzeText;