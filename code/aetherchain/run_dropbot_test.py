# /code/aetherchain/run_dropbot_test.py

from code.shared.gumroad_api import GumroadAPI
from code.shared.social_poster import post_to_social
from code.shared.tool_registry import ToolRegistry
from code.shared.memory_module import AgentMemory
from code.shared.task_orchestrator import TaskOrchestrator
from code.shared.message_protocol import create_message
from code.aetherchain.dropbot_agent import DropBotAgent

# Initialize tools
gumroad_tool = GumroadAPI()
tool_registry = ToolRegistry()
tool_registry.register_tool("gumroad_api", gumroad_tool)
tool_registry.register_tool("social_poster", post_to_social)

# Create DropBot with tools and memory
memory = AgentMemory()
dropbot = DropBotAgent(tools=tool_registry.tools, memory=memory)

# Initialize orchestrator
orchestrator = TaskOrchestrator()
orchestrator.register_agent(dropbot)

# Fake product launch task
launch_task = {
    "assigned_agent": "DropBot",
    "task": "launch_product",
    "context": {
        "product_data": {
            "title": "AI-Enhanced Lemonade Stand Kit",
            "description": "Everything your kid needs to start a smart, branded business.",
            "price": 12.99
        }
    }
}

# Fake announcement task
announce_task = {
    "assigned_agent": "DropBot",
    "task": "announce_drop",
    "context": {
        "message": "Now live: AI-Enhanced Lemonade Stand Kit is up for grabs! Get yours now!"
    }
}

# Queue tasks
orchestrator.add_task(launch_task)
orchestrator.add_task(announce_task)

# Run DropBot
orchestrator.run_next_task()
orchestrator.run_next_task()
