from .base_agent import BaseAgent
from models import UserContext
from tools.technical_tools import RestartServiceTool, CollectLogsTool
from guardrails import OutputGuardrail
from typing import Dict, Any

class TechnicalAgent(BaseAgent):
    def __init__(self, guardrail: OutputGuardrail = None):
        super().__init__("TechnicalAgent")
        self.tools = [RestartServiceTool, CollectLogsTool]
        self.guardrail = guardrail

    async def handle(self, ctx: UserContext) -> Dict[str, Any]:
        msg = (ctx.raw_message or "").lower()
        chosen_tool = RestartServiceTool if "restart" in msg or "service" in msg else CollectLogsTool

        if not chosen_tool.is_enabled(ctx):
            out = f"Tool {chosen_tool.name} is not enabled for this context."
            if self.guardrail:
                ok, msg_or_err = self.guardrail.validate(out)
                if not ok:
                    return {"error": msg_or_err}
            return {"error": out}

        steps = []
        async for step in chosen_tool.stream_events(ctx):
            steps.append(step)
            print(f"[{self.name}::tool:{chosen_tool.name}] {step}")

        final = steps[-1] if steps else "No output"
        if self.guardrail:
            ok, msg_or_err = self.guardrail.validate(final)
            if not ok:
                return {"error": msg_or_err}
        return {"result": final, "tool": chosen_tool.name}
