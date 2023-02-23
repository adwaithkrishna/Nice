from typing import Literal

import discord
from discord import app_commands
from discord.ext import commands


class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.translate_menu = app_commands.ContextMenu(name="Translate", callback=self.translate)
        self.bot.tree.add_command(self.translate_menu)

    async def translate(self, interaction: discord.Interaction, message: discord.Message):
        resp = await self.bot.session.get(f"https://api.popcat.xyz/translate?to=en&text={message.content}")
        resp_json = await resp.json()
        await interaction.response.send_message(resp_json["translated"])

    @app_commands.command()
    @app_commands.describe(member="The member to wish")
    async def wish(
            self,
            interaction: discord.Interaction,
            member: discord.Member,
            thing: Literal['birthday', 'christmas', 'day', 'easter']
    ):
        """Wishes someone

        Parameters
        ----------
        interaction
        member : discord.Member
            The member to wish
        thing
            The reason to wish
        """
        await interaction.response.send_message(f"Happy {thing} {member.mention}")


async def setup(bot):
    await bot.add_cog(Fun(bot))
