---

## **3. `neuroclash-game-design.md`**
```markdown
# NeuroClash Game Design Document

NeuroClash is a multiplayer strategy game where factions of AI agents battle for territory, resources, and dominance using real-time tactics.

---

## Game Core Loop

1. Map loads (procedural or preset)
2. Agents deploy and begin exploring/resource collecting
3. Agents evolve strategies over time through self-play
4. Human players can observe, control, or compete

---

## Agent Roles

- **Scout**: Explores map and reveals terrain
- **Builder**: Constructs defenses and resource structures
- **Fighter**: Attacks enemies or defends key zones
- **Strategist**: Coordinates team agents based on objectives

---

## AI Systems

- Built using Unity + ML-Agents Toolkit
- Trained using PPO + curriculum learning
- Integrated with shared Vantix agent architecture

---

## Unique Mechanics

- **Possession Mode**: Player can take control of any agent for limited time
- **Self-Healing AI**: Agents adapt to teammate losses and shift tactics
- **Dynamic Terrain**: Some maps generated via LLM input prompts

---

## Visual & Audio

- Stylized sci-fi aesthetic
- Dynamic lighting cues based on agent emotion states
- Audio triggered by agent state changes or strategy shifts
