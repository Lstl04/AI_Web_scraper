import React, { useState } from "react";
import axios from "axios";

function App() {
  const [url, setUrl] = useState("");
  const [instructions, setInstructions] = useState("");
  const [content, setContent] = useState("");
  const [loading, setLoading] = useState(false);
  const [model, setModel] = useState("ollama"); 

  const handleScrape = async () => {
    if (!url || !instructions) return alert("Fill in all fields");

    console.log("Sending request:", { url, instructions, model });

    setLoading(true);
    try {
      const response = await axios.post("http://127.0.0.1:5000/scrape", {
        url,
        instructions,
        model, 
      });
      console.log("Server Response:", response.data);
      setContent(response.data.content);
    } catch (error) {
      console.error("Error:", error);
      alert("Scraping failed");
    }
    setLoading(false);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h2>AI Web Scraper</h2>
      
      {/* Model Selector */}
      <select value={model} onChange={(e) => setModel(e.target.value)} style={{ padding: "10px", marginBottom: "10px" }}>
        <option value="ollama">Use Ollama (Local)</option>
        <option value="openai">Use OpenAI API</option>
      </select>

      <br />
      <input
        type="text"
        placeholder="Enter website URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        style={{ padding: "10px", width: "60%" }}
      />
      <br />
      <textarea
        placeholder="Enter formatting instructions"
        value={instructions}
        onChange={(e) => setInstructions(e.target.value)}
        style={{ padding: "10px", width: "60%", marginTop: "10px", height: "80px" }}
      />
      <br />
      <button onClick={handleScrape} style={{ marginTop: "10px", padding: "10px" }}>
        {loading ? "Scraping..." : "Scrape"}
      </button>

      <div style={{ marginTop: "20px", textAlign: "left", maxWidth: "800px", margin: "auto" }}>
        <h3>Formatted Content:</h3>
        <p>{content || "No content yet"}</p>
      </div>
    </div>
  );
}

export default App;
