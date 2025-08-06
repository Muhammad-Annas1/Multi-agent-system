import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", None)

async def print_stream(prefix: str, agen):
    # agen is an async generator
    async for step in agen:
        print(f"{prefix}{step}")
        await asyncio.sleep(0)  # yield
