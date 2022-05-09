from decorators import is_bot_owner

from discord import Interaction
from discord.app_commands import Group, command, check


class Core(Group, name="core"):
    """Core functionality of the bot"""

    @command(name="test", description="Debug command")
    @check(is_bot_owner)
    async def _debug_cmd(self, interaction: Interaction) -> None:
        await interaction.response.send_message("Yeey")
