import discord
from discord.ext import commands

class Upgrades(commands.Cog):
	def __init__(self, bot):
		self.bot = bot



	# View the things available in the shop
	@commands.command()
	async def shop(self, ctx):
	    embed = discord.Embed(title="Shop:", color=0xFFFA9E)
	    embed.add_field(name="text", value="text", inline=False)

	    await ctx.message.channel.send(embed=embed)

	# Buy things from the shop
	@commands.command()
	async def buy(self, ctx):
	    embed = discord.Embed(title="Buy:", color=0xFFFA9E)
	    embed.add_field(name="text", value="text", inline=False)

	    await ctx.message.channel.send(embed=embed)

	# View unlocked embed colours and change the current colour
	@commands.command()
	async def embeds(self, ctx):
	    embed = discord.Embed(title="Embeds:", color=0xFFFA9E)
	    embed.add_field(name="text", value="text", inline=False)

	    await ctx.message.channel.send(embed=embed)

	# View unlocked themes and change the current theme
	@commands.command()
	async def themes(self, ctx):
	    embed = discord.Embed(title="Themes:", color=0xFFFA9E)
	    embed.add_field(name="text", value="text", inline=False)

	    await ctx.message.channel.send(embed=embed)



def setup(bot):
	bot.add_cog(Upgrades(bot))
