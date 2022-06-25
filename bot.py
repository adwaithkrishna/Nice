import discord
from discord.ext import commands
import config
import jishaku

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='-', intents=intents)
jishaku.Flags.NO_DM_TRACEBACK = True


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def hello(ctx):
    await ctx.send("hi")


@bot.command()
async def load(ctx, extension):
    await bot.load_extension(extension)
    await ctx.send(f"Loaded {extension}")


@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(extension)
    await ctx.send(f"Unloaded {extension}")


@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(extension)
    await ctx.send(f"Reloaded {extension}")

bot.run(config.token)
