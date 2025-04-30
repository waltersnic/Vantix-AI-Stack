# Vantix Agent Architecture

The Vantix AI Stack is powered by modular, conjoined AI agents, each with specialized roles. These agents communicate across projects to deliver scalable, emergent behaviors.

---

## Core Agent Types

### 1. **Planner Agent**
- Responsible for task decomposition and scheduling
- Uses LLM for complex instruction parsing and scenario planning
- Example: AetherChain DropBot planner sequences copywriting → branding → launch

### 2. **Analyzer Agent**
- Observes environment state and reports key data
- Used in NeuroClash to detect threats and opportunities
- Used in EchoSoul for emotional detection and dialogue consistency

### 3. **Executor Agent**
- Carries out direct actions or API requests
- In AetherChain: posts to Gumroad, triggers automated tweets
- In NeuroClash: moves units, places structures

### 4. **Communicator Agent**
- Facilitates messaging between agents
- Used for negotiation, knowledge sharing, or memory synchronization

---

## Memory and Learning

- **Short-term Memory**: Stored per agent session
- **Long-term Memory**: Vector-based, shared across agents
- **Training Models**: RL (PPO, SAC), LLM fine-tunes, or self-play loops

---

## Shared Services

- **Task Orchestrator**: Decides which agent acts and when
- **Tool Registry**: Agents have access to shared tools (web scraping, file I/O, diffusion model triggering, etc.)
- **Simulation Adapter**: Connects agents to Unity or real-world APIs

---

## Agent Messaging Protocol

Agent messages are standardized:
```json
{
  "sender": "Agent-A",
  "recipient": "Agent-B",
  "intent": "collaborate",
  "task": "summarize_environment",
  "context": {...},
  "timestamp": "..."
}
