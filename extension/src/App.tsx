import "./style.css";

export function App() {
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
          readOnly
        />
      </section>

      <button className="primaryButton" type="button">
        Generate replies
      </button>
    </main>
  );
}
