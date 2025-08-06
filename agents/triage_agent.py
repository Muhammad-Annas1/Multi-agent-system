from .base_agent import BaseAgent
from models import UserContext
from typing import Dict, Any

class TriageAgent(BaseAgent):
    def __init__(self):
        super().__init__("TriageAgent")

    async def handle(self, ctx: UserContext) -> Dict[str, Any]:
        msg = (ctx.raw_message or "").lower()
        # Very simple keyword-based triage
        if any(k in msg for k in ["refund", "charge", "billing", "invoice"]):
            ctx.issue_type = "billing"
            return {"handoff_to": "BillingAgent", "reason": "Detected billing keywords."}
        if any(k in msg for k in ["restart", "service", "down", "error", "bug", "crash"]):
            ctx.issue_type = "technical"
            return {"handoff_to": "TechnicalAgent", "reason": "Detected technical keywords."}
        # default
        ctx.issue_type = "general"
        return {"handoff_to": "GeneralAgent", "reason": "Default fallback."}
