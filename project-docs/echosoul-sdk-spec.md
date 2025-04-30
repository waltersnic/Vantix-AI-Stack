# EchoSoul SDK – Intelligent NPC System

EchoSoul is a drop-in SDK for Unity (and eventually Godot/Unreal) that transforms static NPCs into emotionally driven, memory-based characters.

---

## Core Features

- LLM-powered dialogue generation
- Personality profiles embedded per NPC
- Long-term memory using vector DBs (ChromaDB or FAISS)
- Emotion engine: NPCs evolve based on past player actions

---

## Architecture

- `NPCBrain.cs` – Manages AI calls, memory, and personality
- `DialogueManager.cs` – Handles UI and player inputs
- `EmotionModule.cs` – Tracks mood, stress, excitement, etc.
- `MemoryStore.cs` – Saves past conversations, facts, and lore references

---

## Plugin API

```csharp
// Unity Example
npcBrain.LoadPersonality("irritable_guard");
npcBrain.Say("Who goes there?");
npcBrain.ReactToPlayer("bribery");
