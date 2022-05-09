import os
import asyncio
from dotenv import load_dotenv

from client import DpyExample

load_dotenv()

if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


client = DpyExample()
client.run(os.environ["DISCORD_TOKEN"])
