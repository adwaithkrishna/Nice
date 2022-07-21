import aiohttp
import discord
from discord.ext import commands
import jishaku

import config


class Nice(commands.Bot):
    
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="-", intents=intents)

    async def setup_hook(self) -> None:
        self.session = aiohttp.ClientSession()
        jishaku.Flags.NO_DM_TRACEBACK = True

    async def on_ready(self):
        print(f"Logged in as {bot.user}")


bot = Nice()


@bot.command()
async def hello(ctx):
    await ctx.send("hi")


@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    await bot.load_extension(extension)
    await ctx.send(f"Loaded {extension}")


@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    await bot.unload_extension(extension)
    await ctx.send(f"Unloaded {extension}")


@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    await bot.reload_extension(extension)
    await ctx.send(f"Reloaded {extension}")

if __name__ == '__main__':
    bot.run(config.token)
