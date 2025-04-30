# /code/backend-fastapi/agent_router.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Temporary in-memory registry
AGENTS = {}

class TaskRequest(BaseModel):
    agent: str
    task: str
    context: dict = {}

@router.post("/register")
def register_agent(name: str, role: str):
    AGENTS[name] = {"name": name, "role": role, "status": "online"}
    return {"message": f"{name} registered as {role}"}

@router.get("/agents")
def get_agents():
    return list(AGENTS.values())

@router.post("/send_task")
def send_task(task: TaskRequest):
    if task.agent not in AGENTS:
        raise HTTPException(status_code=404, detail="Agent not found")
    # Future: trigger real agent here
    return {"message": f"Task '{task.task}' sent to {task.agent}", "context": task.context}
