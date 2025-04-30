# /code/shared/run_command_center.py

from code.shared.command_center_interface import CommandCenter
from code.shared.gumroad_api import GumroadAPI
from code.shared.social_poster import post_to_social
from code.shared.tool_registry import ToolRegistry
from code.shared.memory_module import AgentMemory

from code.aetherchain.dropbot_agent import DropBotAgent
from code.aetherchain.trendscout_agent import TrendScoutAgent
from code.echosoul.lore_npc_agent import LoreNPCAgent

# Shared memory and tools
shared_memory = AgentMemory()
tools = ToolRegistry()
tools.register_tool("gumroad_api", GumroadAPI())
tools.register_tool("social_poster", post_to_social)

# Initialize agents
dropbot = DropBotAgent(tools=tools.tools, memory=shared_memory)
scout = TrendScoutAgent(tools=tools.tools, memory=shared_memory)
npc = LoreNPCAgent(name="Sir Vaelin", persona="wounded knight", memory=shared_memory)

# Command Center
cc = CommandCenter()
cc.register_agent(dropbot)
cc.register_agent(scout)
cc.register_agent(npc)

# Send tasks
cc.send_task("TrendScout", "scan_trends")
cc.send_task("DropBot", "launch_product", {
    "product_data": {
        "title": "Knight Lore Dice Set",
        "description": "RPG dice with built-in AI lore cards",
        "price": 6.66
    }
})
cc.send_task("Sir Vaelin", "speak_to_player", {
    "player_input": "What happened to your arm?"
})
cc.send_task("Sir Vaelin", "emotion_trigger", {
    "mood": "sad"
})

# Show output
cc.display_status()
cc.show_logs()
