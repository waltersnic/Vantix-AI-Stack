import React from 'react';
import AgentCard from './components/AgentCard';
import TaskPanel from './components/TaskPanel';
import LogStream from './components/LogStream';

function App() {
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Vantix Command Center</h1>
      <div className="grid grid-cols-2 gap-4">
        <AgentCard />
        <TaskPanel />
      </div>
      <LogStream />
    </div>
  );
}

export default App;
