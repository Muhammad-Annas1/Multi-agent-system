from typing import AsyncGenerator
from models import UserContext

class RestartServiceTool:
    name = "restart_service"

    @staticmethod
    def is_enabled(ctx: UserContext) -> bool:
        # Only enabled if issue_type is 'technical'
        return ctx.issue_type == "technical"

    @staticmethod
    async def stream_events(ctx: UserContext) -> AsyncGenerator[str, None]:
        yield "Authenticating admin session..."
        await __async_sleep()
        yield "Sending restart command to user's service..."
        await __async_sleep()
        yield "Waiting for service to come back..."
        await __async_sleep()
        yield "Service restarted successfully."

class CollectLogsTool:
    name = "collect_logs"

    @staticmethod
    def is_enabled(ctx: UserContext) -> bool:
        return True

    @staticmethod
    async def stream_events(ctx: UserContext):
        yield "Collecting logs for last 1 hour..."
        await _async_sleep()
        yield "Compressing logs..."
        await _async_sleep()
        yield "Logs ready: /tmp/user-logs-123.tar.gz"

async def _async_sleep():
    import asyncio
    await asyncio.sleep(0.4)
