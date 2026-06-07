import { useEffect, useState } from "react";
import "./style.css";

type SelectedTextResponse = {
  selectedText?: string;
};

export function App() {
  const [selectedText, setSelectedText] = useState("");

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

      <button className="primaryButton" type="button">
        Generate replies
      </button>
    </main>
  );
}