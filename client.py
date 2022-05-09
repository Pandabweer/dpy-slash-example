import os
from extensions import EXTENSIONS

import discord
from discord import Client, Intents
from discord.app_commands import CommandTree


class DpyExample(Client):
    def __init__(self) -> None:
        self.owner_id = int(os.environ["DISCORD_BOT_OWNER_ID"])
        super().__init__(
            intents=Intents(),
            application_id=os.environ["DISCORD_APP_ID"],
            owner_id=self.owner_id
        )
        self.tree = CommandTree(self)

    async def setup_hook(self) -> None:
        for x in EXTENSIONS:
            self.tree.add_command(x(), guild=discord.Object(id=os.environ["DISCORD_DEV_GUILD"]))
        await self.tree.sync(guild=discord.Object(id=os.environ["DISCORD_DEV_GUILD"]))

    @staticmethod
    async def on_ready() -> None:
        print("Ready")
