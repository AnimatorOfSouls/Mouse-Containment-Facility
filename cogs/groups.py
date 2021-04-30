import discord
from discord.ext import commands

class Groups(commands.Cog):
	def __init__(self, bot):
		self.bot = bot



	# Creates a new group which can be set public/private
	@commands.command()
	async def new(self, ctx):
	    embed = discord.Embed(title="New Group:", color=0xFFFA9E)
	    embed.add_field(name="text", value="text", inline=False)

	    await ctx.message.channel.send(embed=embed)

	# Join a group
	@commands.command()
	async def join(self, ctx):
	    embed = discord.Embed(title="Join Group:", color=0xFFFA9E)
	    embed.add_field(name="text", value="text", inline=False)

	    await ctx.message.channel.send(embed=embed)

	# View/edit the group the user is in
	@commands.command()
	async def group(self, ctx):
	    embed = discord.Embed(title="Current Group:", color=0xFFFA9E)
	    embed.add_field(name="text", value="text", inline=False)

	    await ctx.message.channel.send(embed=embed)



def setup(bot):
	bot.add_cog(Groups(bot))
