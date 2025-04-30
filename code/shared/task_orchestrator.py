# /code/shared/task_orchestrator.py

class TaskOrchestrator:
    def __init__(self):
        self.agent_registry = {}
        self.task_queue = []

    def register_agent(self, agent):
        self.agent_registry[agent.name] = agent
        print(f"Registered agent: {agent.name} [{agent.role}]")

    def add_task(self, task):
        self.task_queue.append(task)

    def run_next_task(self):
        if not self.task_queue:
            print("No tasks in queue.")
            return

        task = self.task_queue.pop(0)
        agent_name = task.get("assigned_agent")
        
        if agent_name in self.agent_registry:
            agent = self.agent_registry[agent_name]
            print(f"Orchestrator assigning task to {agent_name}")
            agent.act(task)
        else:
            print(f"No agent registered with name: {agent_name}")
