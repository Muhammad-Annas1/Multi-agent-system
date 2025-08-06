from .base_agent import BaseAgent
from models import UserContext
from tools.billing_tools import RefundTool, InvoiceTool
from guardrails import OutputGuardrail
from typing import Dict, Any
import asyncio

class BillingAgent(BaseAgent):
    def __init__(self, guardrail: OutputGuardrail = None):
        super().__init__("BillingAgent")
        self.tools = [RefundTool, InvoiceTool]
        self.guardrail = guardrail

    async def handle(self, ctx: UserContext) -> Dict[str, Any]:
        # choose tool based on keywords
        msg = (ctx.raw_message or "").lower()
        chosen_tool = None
        if "refund" in msg:
            chosen_tool = RefundTool
        else:
            chosen_tool = InvoiceTool

        # check is_enabled
        if not chosen_tool.is_enabled(ctx):
            out = f"Tool {chosen_tool.name} is not enabled for this user/context."
            if self.guardrail:
                ok, msg_or_err = self.guardrail.validate(out)
                if not ok:
                    return {"error": msg_or_err}
            return {"error": out}

        # run stream_events
        steps = []
        async for step in chosen_tool.stream_events(ctx):
            steps.append(step)
            print(f"[{self.name}::tool:{chosen_tool.name}] {step}")

        final = steps[-1] if steps else "No output from tool."
        if self.guardrail:
            ok, msg_or_err = self.guardrail.validate(final)
            if not ok:
                return {"error": msg_or_err}
        return {"result": final, "tool": chosen_tool.name}
