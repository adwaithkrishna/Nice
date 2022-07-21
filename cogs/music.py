import discord
from discord.ext import commands


class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lyrics(self, ctx, *, title):
        async with ctx.typing():
            resp = await self.bot.session.get(f"https://api.popcat.xyz/lyrics?song={title}")
            resp_json = await resp.json()
            embed = discord.Embed(color=0x03fcf8, title=resp_json["title"], description=resp_json["lyrics"])
            embed.set_thumbnail(url=resp_json["image"])
            embed.set_footer(text=resp_json["artist"])
            await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Music(bot))
