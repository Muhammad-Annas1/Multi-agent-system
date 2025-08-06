from typing import AsyncGenerator
from models import UserContext

class RefundTool:
    name = "refund"

    @staticmethod
    def is_enabled(ctx: UserContext) -> bool:
        # Enabled only for premium users
        return bool(ctx.is_premium_user)

    @staticmethod
    async def stream_events(ctx: UserContext) -> AsyncGenerator[str, None]:
        yield "Validating refund policy..."
        await __async_sleep()
        yield f"Looking up transactions for user {ctx.name}..."
        await __async_sleep()
        yield "Creating refund record..."
        await __async_sleep()
        yield "Refund processed: $42.00 (demo)"
        # return final string by last yield

class InvoiceTool:
    name = "invoice_lookup"

    @staticmethod
    def is_enabled(ctx: UserContext) -> bool:
        return True

    @staticmethod
    async def stream_events(ctx: UserContext):
        yield "Searching invoices..."
        await _async_sleep()
        yield "Found invoice #12345 — amount $42.00"
        await _async_sleep()
        yield "Invoice details displayed."

async def _async_sleep():
    import asyncio
    await asyncio.sleep(0.4)
