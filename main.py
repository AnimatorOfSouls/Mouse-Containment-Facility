import discord
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import commands

import os
from dotenv import load_dotenv

#-----------------------------MAIN------------------------------#
extensions = ["cogs.info", "cogs.groups", "cogs.upgrades"]

bot = commands.Bot(command_prefix=",m ", intents=discord.Intents.default())
bot.remove_command("help")

if __name__ == "__main__":
	for extension in extensions:
		bot.load_extension(extension)

'''
@bot.event
async def on_ready():
	print("Connected as "+bot.user.name)

	#changes watching status
	await bot.change_presence(activity=discord.Game(name=",m", type=3))
'''


#-------------------------TOKEN---------------------------------#
load_dotenv()
bot.run(os.getenv("TOKEN"))
