# /code/echosoul/run_npc_test.py

from code.echosoul.lore_npc_agent import LoreNPCAgent
from code.shared.memory_module import AgentMemory
from code.shared.task_orchestrator import TaskOrchestrator

# Shared memory
memory = AgentMemory()

# Create NPC
npc = LoreNPCAgent(name="Eron the Guard", persona="gruff sentinel", memory=memory)

# Orchestrator
orchestrator = TaskOrchestrator()
orchestrator.register_agent(npc)

# Simulate emotion shift
orchestrator.add_task({
    "assigned_agent": "Eron the Guard",
    "task": "emotion_trigger",
    "context": { "mood": "angry" }
})

# Simulate dialogue
orchestrator.add_task({
    "assigned_agent": "Eron the Guard",
    "task": "speak_to_player",
    "context": { "player_input": "Why are you guarding this door?" }
})

# Run interaction
orchestrator.run_next_task()
orchestrator.run_next_task()

# Display memory summary
print("\n[Memory Summary]")
print(npc.memory.summarize_recent())
