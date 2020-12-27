import discord
from discord.ext import commands

TOKEN = "Bot's token here"
client = commands.Bot(command_prefix="Bot's prefix here")

client.run(TOKEN)