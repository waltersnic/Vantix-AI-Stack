# /code/echosoul/lore_npc_agent.py

from code.shared.agent_base import AgentBase

class LoreNPCAgent(AgentBase):
    def __init__(self, name="LoreNPC", persona="mysterious guard", tools=None, memory=None):
        super().__init__(name, role="npc", tools=tools, memory=memory)
        self.persona = persona
        self.emotion_state = "neutral"

    def act(self, task):
        print(f"[{self.name}] Reacting to: {task['task']}")

        if task["task"] == "speak_to_player":
            player_input = task["context"].get("player_input", "")
            response = self._generate_response(player_input)
            print(f"[{self.name}] says: {response}")
            self.memory.remember_short_term(f"Player said: {player_input}")
            self.memory.remember_short_term(f"I replied: {response}")

        elif task["task"] == "emotion_trigger":
            mood = task["context"].get("mood", "neutral")
            self.emotion_state = mood
            print(f"[{self.name}] now feels: {mood}")

    def _generate_response(self, input_text):
        if self.emotion_state == "angry":
            return f"*growls* What do you want, stranger?"
        elif self.emotion_state == "happy":
            return f"Ah! A fine day to you. {self.persona.capitalize()}s don’t get much joy, but today feels different."
        else:
            return f"You speak, and I listen. What brings you here?"
