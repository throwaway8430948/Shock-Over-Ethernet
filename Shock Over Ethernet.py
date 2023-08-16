import discord
from discord.ext import commands
import pyautogui
import random
import time

TOKEN = ""

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
@commands.cooldown(rate=10, per=120, type=commands.BucketType.user)
async def shock(ctx):
    # Click the screen at the specified coordinates
    pyautogui.click(700, 500)
    
    # Send the message
    await ctx.send(f"Shocked the pet!")

@shock.error
async def shock_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        # Inform user of the cooldown
        await ctx.send("Wow! The pet is fried! The collar needs to discharge static electricity, cooldown mode lasts 2 minutes.")

bot.run(TOKEN)

