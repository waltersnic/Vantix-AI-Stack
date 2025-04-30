import React, { useEffect, useState } from 'react';

function AgentCard() {
  const [agents, setAgents] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/agents')
      .then(res => res.json())
      .then(data => setAgents(data))
      .catch(err => console.error('Error fetching agents:', err));
  }, []);

  return (
    <div className="border p-4 rounded shadow">
      <h2 className="font-semibold text-xl mb-2">Registered Agents</h2>
      {agents.length === 0 ? (
        <p className="text-gray-500">No agents found.</p>
      ) : (
        <ul className="space-y-2">
          {agents.map(agent => (
            <li key={agent.name} className="p-2 bg-gray-100 rounded">
              <strong>{agent.name}</strong> – {agent.role}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default AgentCard;
