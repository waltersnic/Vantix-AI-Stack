# /code/shared/agent_base.py

class AgentBase:
    def __init__(self, name, role, tools=None, memory=None):
        self.name = name
        self.role = role
        self.tools = tools or {}
        self.memory = memory or []
        self.context = {}

    def receive_message(self, msg):
        """Handle incoming message."""
        self.memory.append(msg)
        print(f"[{self.name}] received: {msg}")

    def send_message(self, recipient, intent, task, context=None):
        """Send structured message to another agent."""
        return {
            "sender": self.name,
            "recipient": recipient,
            "intent": intent,
            "task": task,
            "context": context or {},
        }

    def act(self, task):
        """Override with custom logic in subclass."""
        raise NotImplementedError("Each agent must define its act() method.")
