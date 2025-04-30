# /code/backend-fastapi/memory_api.py

from fastapi import APIRouter, HTTPException

router = APIRouter()

# Temporary fake memory store
AGENT_MEMORY = {
    "DropBot": ["Launched: AI Dice Pack", "Posted: Drop live"],
    "TrendScout": ["Found: AI Dungeon Cards", "Found: Overlay Kit"],
    "Sir Vaelin": ["Player said: What happened?", "I replied: You speak, and I listen."]
}

@router.get("/memory/{agent_name}")
def get_memory(agent_name: str):
    memory = AGENT_MEMORY.get(agent_name)
    if not memory:
        raise HTTPException(status_code=404, detail="No memory found for that agent")
    return {"agent": agent_name, "recent_memory": memory}
