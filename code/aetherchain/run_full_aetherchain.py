# /code/aetherchain/run_full_aetherchain.py

from code.aetherchain.trendscout_agent import TrendScoutAgent
from code.aetherchain.dropbot_agent import DropBotAgent
from code.shared.gumroad_api import GumroadAPI
from code.shared.social_poster import post_to_social
from code.shared.tool_registry import ToolRegistry
from code.shared.memory_module import AgentMemory
from code.shared.task_orchestrator import TaskOrchestrator

# Shared tools and memory
tool_registry = ToolRegistry()
tool_registry.register_tool("gumroad_api", GumroadAPI())
tool_registry.register_tool("social_poster", post_to_social)
shared_memory = AgentMemory()

# Agents
scout = TrendScoutAgent(tools=tool_registry.tools, memory=shared_memory)
dropbot = DropBotAgent(tools=tool_registry.tools, memory=shared_memory)

# Orchestrator
orchestrator = TaskOrchestrator()
orchestrator.register_agent(scout)
orchestrator.register_agent(dropbot)

# 1. Scout scans trends
orchestrator.add_task({
    "assigned_agent": "TrendScout",
    "task": "scan_trends",
    "context": {}
})

# 2. DropBot picks top trend and launches it
top_trend = {
    "title": "AI Dungeon Cards",
    "description": "Generate quests with GPT!",
    "price": 9.99
}

orchestrator.add_task({
    "assigned_agent": "DropBot",
    "task": "launch_product",
    "context": { "product_data": top_trend }
})

orchestrator.add_task({
    "assigned_agent": "DropBot",
    "task": "announce_drop",
    "context": { "message": f"Now live: {top_trend['title']} – {top_trend['description']}" }
})

# Run tasks
orchestrator.run_next_task()
orchestrator.run_next_task()
orchestrator.run_next_task()
