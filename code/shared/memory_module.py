# /code/shared/memory_module.py

class AgentMemory:
    def __init__(self):
        self.short_term = []
        self.long_term = {}

    def remember_short_term(self, item):
        self.short_term.append(item)
        if len(self.short_term) > 10:
            self.short_term.pop(0)

    def store_long_term(self, key, value):
        self.long_term[key] = value

    def retrieve_long_term(self, key):
        return self.long_term.get(key, None)

    def summarize_recent(self):
        return "\n".join(self.short_term[-5:])
