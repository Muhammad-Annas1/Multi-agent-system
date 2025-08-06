import asyncio
import os
from dotenv import load_dotenv
from runner import Runner
from models import UserContext
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Read Gemini API key from .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("⚠️ GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

async def main():
    guardrail_choice = input("Enable output guardrail to block apologies? (y/N): ").strip().lower() == "y"
    runner = Runner(guardrail_enabled=guardrail_choice)

    print("Multi-agent console. Type 'exit' to quit.")
    name = input("Enter your name: ").strip() or "User"

    while True:
        user_msg = input(f"\n{name}> ").strip()
        if user_msg.lower() in ("exit", "quit"):
            print("Goodbye.")
            break

        # For demo, ask if user is premium
        is_premium = input("Are you a premium user? (y/N): ").strip().lower() == "y"

        ctx = UserContext(
            name=name,
            is_premium_user=is_premium,
            raw_message=user_msg
        )

        result = await runner.process(ctx)
        print("→ Final result:", result)

if __name__ == "__main__":
    asyncio.run(main())
