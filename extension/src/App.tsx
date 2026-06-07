import { useEffect, useState } from "react";
import { generateReplies } from "./api";
import type { GenerateResponse, Tone } from "./types";
import "./style.css";

type SelectedTextResponse = {
  selectedText?: string;
};

export function App() {
  const [selectedText, setSelectedText] = useState("");
  const [tone, setTone] = useState<Tone>("professional");
  const [result, setResult] = useState<GenerateResponse | null>(null);
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    loadSelectedText();
  }, []);

  async function loadSelectedText() {
    const [tab] = await chrome.tabs.query({
      active: true,
      currentWindow: true,
    });

    if (!tab.id) {
      return;
    }

    chrome.tabs.sendMessage(
      tab.id,
      { type: "GET_SELECTED_TEXT" },
      (response: SelectedTextResponse) => {
        setSelectedText(response?.selectedText || "");
      },
    );
  }

  async function handleGenerate() {
    setError("");
    setResult(null);
    setIsLoading(true);

    try {
      const response = await generateReplies({
        selectedText,
        tone,
      });

      setResult(response);
    } catch {
      setError("Failed to generate replies.");
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <main className="app">
      <header className="header">
        <h1>ResReply</h1>
        <p>Generate high-signal replies from selected webpage text.</p>
      </header>

      <section className="card">
        <label htmlFor="selectedText">Selected text</label>
        <textarea
          id="selectedText"
          placeholder="Selected webpage text will appear here."
          rows={6}
          value={selectedText}
          readOnly
        />
      </section>
      <section className="card">
        <label htmlFor="tone">Tone</label>
        <select
          id="tone"
          value={tone}
          onChange={(event) => setTone(event.target.value as Tone)}
        >
          <option value="professional">Professional</option>
          <option value="technical">Technical</option>
          <option value="recruiter-safe">Recruiter-safe</option>
          <option value="supportive">Supportive</option>
          <option value="witty">Witty</option>
        </select>
      </section>
      <button
        className="primaryButton"
        type="button"
        disabled={!selectedText || isLoading}
        onClick={handleGenerate}
      >
        {isLoading ? "Generating..." : "Generate replies"}
      </button>

      {error && <p role="alert">{error}</p>}

      {result && (
        <section className="card">
          <h2>Reply score: {result.replyScore}/10</h2>
          <p>{result.strategy}</p>

          {result.suggestions.map((suggestion) => (
            <article key={suggestion.label}>
              <h3>{suggestion.label}</h3>
              <p>{suggestion.text}</p>
            </article>
          ))}
        </section>
      )}
    </main>
  );
}