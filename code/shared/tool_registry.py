# /code/shared/tool_registry.py

class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register_tool(self, name, func):
        self.tools[name] = func
        print(f"Tool registered: {name}")

    def use_tool(self, name, *args, **kwargs):
        tool = self.tools.get(name)
        if tool:
            return tool(*args, **kwargs)
        else:
            raise Exception(f"Tool '{name}' not found in registry.")
