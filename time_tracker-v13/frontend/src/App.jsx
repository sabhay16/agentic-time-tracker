import React, { useState, useEffect } from "react";
import axios from "axios";

export default function App() {
  const [entries, setEntries] = useState([]);
  const [suggested, setSuggested] = useState(null);

  const fetchEntries = async () => {
    const res = await axios.get("/api/entries");
    setEntries(res.data);
  };

  const suggestEntry = async () => {
    const res = await axios.post("/api/suggest", { context: "Monday, worked on client X" });
    setSuggested(res.data);
  };

  useEffect(() => {
    fetchEntries();
  }, []);

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-4">Agentic Time Tracker</h1>
      <button
        onClick={suggestEntry}
        className="bg-blue-500 text-white px-4 py-2 rounded mb-4"
      >
        Suggest Entry with AI
      </button>
      {suggested && (
        <div className="bg-white shadow p-4 rounded mb-4">
          <h2 className="font-bold">Suggested Entry</h2>
          <pre>{JSON.stringify(suggested, null, 2)}</pre>
        </div>
      )}
      <div className="bg-white shadow rounded p-4">
        <h2 className="font-semibold mb-2">Logged Entries</h2>
        <ul>
          {entries.map((entry, idx) => (
            <li key={idx} className="border-b py-1">
              {entry.Consultant} - {entry.Client} - {entry.Date} - {entry.Hours} hrs
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}