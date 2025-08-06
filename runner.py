import asyncio
from agents.triage_agent import TriageAgent
from agents.billing_agent import BillingAgent
from agents.technical_agent import TechnicalAgent
from agents.general_agent import GeneralAgent
from models import UserContext
from guardrails import OutputGuardrail

class Runner:
    def __init__(self, guardrail_enabled: bool = False):
        self.triage = TriageAgent()
        self.guardrail = OutputGuardrail() if guardrail_enabled else None
        self.agents = {
            "BillingAgent": BillingAgent(self.guardrail),
            "TechnicalAgent": TechnicalAgent(self.guardrail),
            "GeneralAgent": GeneralAgent(self.guardrail),
        }

    async def process(self, ctx: UserContext):
        print("[Runner] Receiving message:", ctx.raw_message)
        triage_out = await self.triage.handle(ctx)
        handoff_to = triage_out.get("handoff_to")
        reason = triage_out.get("reason")
        print(f"[Runner] Triage decided: {handoff_to} (reason: {reason})")
        agent = self.agents.get(handoff_to)
        if not agent:
            return {"error": "No agent found to handle this request."}

        print(f"[Runner] HANDOFF → {handoff_to}")
        result = await agent.handle(ctx)
        return result
