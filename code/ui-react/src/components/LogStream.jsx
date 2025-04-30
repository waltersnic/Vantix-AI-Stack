import React, { useEffect, useState } from 'react';

function LogStream() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    const socket = new WebSocket('ws://localhost:8000/logs/stream');

    socket.onmessage = (event) => {
      setLogs(prev => [event.data, ...prev.slice(0, 19)]);
    };

    socket.onerror = (err) => {
      console.error('WebSocket error:', err);
    };

    return () => socket.close();
  }, []);

  return (
    <div className="border p-4 mt-4 rounded shadow h-64 overflow-auto bg-black text-green-400 font-mono text-sm">
      <h2 className="text-white font-bold mb-2">Live System Logs</h2>
      <ul>
        {logs.map((log, idx) => (
          <li key={idx}>{log}</li>
        ))}
      </ul>
    </div>
  );
}

export default LogStream;
