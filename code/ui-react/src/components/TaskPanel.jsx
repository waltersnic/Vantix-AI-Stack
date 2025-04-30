import React, { useState } from 'react';

function TaskPanel() {
  const [agent, setAgent] = useState('');
  const [task, setTask] = useState('');
  const [context, setContext] = useState('');
  const [confirmation, setConfirmation] = useState('');

  const sendTask = async () => {
    const payload = {
      agent,
      task,
      context: context ? JSON.parse(context) : {}
    };

    try {
      const res = await fetch('http://localhost:8000/api/send_task', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      setConfirmation(data.message);
    } catch (err) {
      console.error('Task send error:', err);
      setConfirmation('Failed to send task.');
    }
  };

  return (
    <div className="border p-4 rounded shadow">
      <h2 className="font-semibold text-xl mb-2">Send Task to Agent</h2>
      <input
        className="border p-2 w-full mb-2"
        placeholder="Agent name (e.g. DropBot)"
        value={agent}
        onChange={e => setAgent(e.target.value)}
      />
      <input
        className="border p-2 w-full mb-2"
        placeholder="Task name (e.g. launch_product)"
        value={task}
        onChange={e => setTask(e.target.value)}
      />
      <textarea
        className="border p-2 w-full mb-2"
        placeholder='Context (JSON), e.g. {"title": "AI Dice Pack", "price": 9.99}'
        value={context}
        onChange={e => setContext(e.target.value)}
      />
      <button
        className="bg-blue-600 text-white px-4 py-2 rounded"
        onClick={sendTask}
      >
        Send Task
      </button>
      {confirmation && <p className="mt-3 text-green-600">{confirmation}</p>}
    </div>
  );
}

export default TaskPanel;
