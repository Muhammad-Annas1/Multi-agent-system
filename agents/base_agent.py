from models import UserContext
from typing import Any, Dict

class BaseAgent:
    name: str

    def __init__(self, name: str):
        self.name = name

    async def handle(self, ctx: UserContext) -> Dict[str, Any]:
        raise NotImplementedError("Implement in subclass")
