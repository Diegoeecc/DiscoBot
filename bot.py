import discord
from bot_logic import gen_pass
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("HI!")

@bot.command()
async def bye(ctx):
    await ctx.send(":(")

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

bot.run("Token")
