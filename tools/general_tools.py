from typing import AsyncGenerator
from models import UserContext

class FAQTool:
    name = "faq_lookup"

    @staticmethod
    def is_enabled(ctx: UserContext) -> bool:
        return True

    @staticmethod
    async def stream_events(ctx: UserContext) -> AsyncGenerator[str, None]:
        yield "Searching knowledge base for keywords..."
        await _async_sleep()
        yield "Found relevant FAQ: 'How to change password'"
        await _async_sleep()
        yield "Returning FAQ snippet."
        
async def _async_sleep():
    import asyncio
    await asyncio.sleep(0.4)
