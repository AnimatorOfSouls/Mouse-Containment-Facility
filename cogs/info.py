import discord
from discord.ext import commands

import sqlite3

class Info(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	# A list of commands
	@commands.command(aliases=["h","commands"])
	async def help(self, ctx):
		embed = discord.Embed(title="Commands:", color=0xFFFA9E)
		embed.add_field(name=":mag_right: Info:", value="`help` `profile` `list`", inline=False)
		embed.add_field(name=":books: Groups:", value="`new [group name] [public/private] [description]` `join [code]` `group` `group schedule` `group leave`", inline=False)
		embed.add_field(name=":arrow_up: Upgrades:", value="`shop embed` `shop theme` `buy [embed/theme]` `embeds [id]` `themes [id]`", inline=False)

		await ctx.message.channel.send(embed=embed)


	# Displays the statistics of the user
	@commands.command(aliases=["p"])
	async def profile(self, ctx):
		conn = sqlite3.connect("data/MouseDatabase.db")
		cursor = conn.cursor()

		#Getting data from Users table
		cursor.execute("SELECT workTime, coinEmbed, coinTheme, currentThemeId, currentGroupId FROM Users WHERE userId = '" + str(ctx.message.author.id) + "'")
		result = cursor.fetchall()
		if result != []:
			workTime = result[0][0]
			coin_embed = result[0][1]
			coin_theme = result[0][2]
			current_theme_id = result[0][3]
			current_group_id = result[0][4]
		else:
			#adding new user to Users table
			sql = "INSERT INTO Users(userId, workTime, coinEmbed, coinTheme, currentEmbedId, currentThemeId, embeds, themes, currentGroupId) VALUES (?,?,?,?,?,?,?,?,?)"
			values = [str(ctx.message.author.id),0,0,0,0,0,"","",-1]

			cursor.execute(sql,values)	#Inserting the data
			conn.commit()				#Saving the entry

			#getting default values
			workTime = 0
			coin_embed = 0
			coin_theme = 0
			current_theme_id = 0

		#Getting coin icons from Themes table
		cursor.execute("SELECT emoji, coinEmbed, coinTheme FROM Themes WHERE themeId = '" + str(current_theme_id) + "'")
		result = cursor.fetchall()
		theme_emoji = result[0][0]
		coin_embed_emoji = result[0][1]
		coin_theme_emoji = result[0][2]

		#Getting group information
		if current_group_id == -1:
			group_name = "Not in group"
		else:
			cursor.execute("SELECT name FROM Groups WHERE groupId = '" + str(current_group_id) + "'")
			result = cursor.fetchone()
			group_name = result[0]


		#Closing the connections
		cursor.close()
		conn.close()

		level = round((workTime-(workTime%120))/120)

		embed = discord.Embed(title="Profile:", color=0xFFFA9E)
		embed.set_thumbnail(url=ctx.message.author.avatar_url)
		embed.add_field(name=str(ctx.message.author)[:-5], value="Time Worked: `"+str(workTime)+" mins`\nCurrent Group: `"+group_name+"`\n"+coin_embed_emoji+" `"+str(coin_embed)+"`\t"+coin_theme_emoji+" `"+str(coin_theme)+"`", inline=False)
		embed.add_field(name=theme_emoji+" Mouse", value="Level: `"+str(level)+"`\n"+coin_embed_emoji+" per hour: `"+str(round((level)*0.8))+"`", inline=False)

		await ctx.message.channel.send(embed=embed)


	# Displays a list of all public groups
	@commands.command(aliases=["ls","groups"])
	async def list(self, ctx):
		conn = sqlite3.connect("data/MouseDatabase.db")
		cursor = conn.cursor()

		#getting list of public groups
		cursor.execute("SELECT groupId, name FROM Groups WHERE password IS NULL")
		result = cursor.fetchall()
		groups = []
		if result != []:
			for r in result:
				record = []
				record.append(r[1])

				cursor.execute("SELECT COUNT(*) FROM Users WHERE currentGroupId = '" + str(r[0]) + "'")
				num_users = cursor.fetchone()
				record.append(num_users[0])

				groups.append(record)

		groups_list = ""
		if groups == []:
			groups_list += "No public groups are currently available."
		else:
			for g in groups:
				print(g)
				groups_list += g[0]+" `Users: "+str(g[1])+"`\n"

		embed = discord.Embed(title="Public Groups:", color=0xFFFA9E)
		embed.add_field(name="Groups", value=groups_list, inline=False)

		await ctx.message.channel.send(embed=embed)


def setup(bot):
	bot.add_cog(Info(bot))
