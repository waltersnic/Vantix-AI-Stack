# /code/shared/command_center_interface.py

class CommandCenter:
    def __init__(self):
        self.agents = {}
        self.logs = []

    def register_agent(self, agent):
        self.agents[agent.name] = agent
        self.logs.append(f"[REGISTERED] {agent.name} as {agent.role}")

    def send_task(self, agent_name, task_name, context=None):
        agent = self.agents.get(agent_name)
        if not agent:
            self.logs.append(f"[ERROR] Agent {agent_name} not found.")
            return

        task = {
            "assigned_agent": agent_name,
            "task": task_name,
            "context": context or {}
        }

        self.logs.append(f"[TASK] Sent '{task_name}' to {agent_name}")
        agent.act(task)

    def display_status(self):
        print("\n--- COMMAND CENTER STATUS ---")
        for name, agent in self.agents.items():
            print(f"{name} ({agent.role}) – Emotion: {getattr(agent, 'emotion_state', 'N/A')}")

    def show_logs(self):
        print("\n--- COMMAND LOG ---")
        for log in self.logs:
            print(log)
