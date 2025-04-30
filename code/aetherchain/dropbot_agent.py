# /code/aetherchain/dropbot_agent.py

from code.shared.agent_base import AgentBase
from code.shared.message_protocol import create_message

class DropBotAgent(AgentBase):
    def __init__(self, name="DropBot", tools=None, memory=None):
        super().__init__(name, role="product_launcher", tools=tools, memory=memory)

    def act(self, task):
        print(f"[{self.name}] Executing task: {task['task']}")

        if task["task"] == "launch_product":
            product = task["context"].get("product_data")
            if not product:
                print("No product data provided.")
                return

            gumroad = self.tools.get("gumroad_api")
            if not gumroad:
                print("Gumroad API tool not available.")
                return

            response = gumroad.publish(product)
            print(f"[{self.name}] Product launched: {response}")
            self.memory.remember_short_term(f"Launched: {product.get('title')}")

        elif task["task"] == "announce_drop":
            post_tool = self.tools.get("social_poster")
            message = task["context"].get("message")
            if post_tool and message:
                post_tool(message)
                self.memory.remember_short_term(f"Posted: {message}")
