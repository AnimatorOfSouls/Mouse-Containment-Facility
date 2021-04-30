import sqlite3

### MODULES ###
def create_tables():
	#Connecting to database
	conn = sqlite3.connect("data/MouseDatabase.db")

	#Creating the tables
	conn.execute("CREATE TABLE IF NOT EXISTS Users(userId VARCHAR(18), workTime INT, coinEmbed INT, coinTheme INT, currentEmbedId INT, currentThemeId INT, embeds TEXT, themes TEXT, currentGroupId INT)")
	conn.execute("CREATE TABLE IF NOT EXISTS Groups(groupId INTEGER PRIMARY KEY AUTOINCREMENT, ownerId VARCHAR(18), name TEXT, password TEXT, description TEXT, schedule TEXT)")
	conn.execute("CREATE TABLE IF NOT EXISTS Embeds(embedId INT, name TEXT, emoji TEXT, colour TEXT)")
	conn.execute("CREATE TABLE IF NOT EXISTS Themes(themeId INT, name TEXT, emoji TEXT, coinEmbed TEXT, coinTheme TEXT)")

	#Closing the connection
	conn.close()



def populate_tables():
	#Connecting to database and creating a cursor to navigate the database
	conn = sqlite3.connect("data/MouseDatabase.db")
	cursor = conn.cursor()

	sql_embed = "INSERT INTO Embeds(embedId, name, emoji, colour) VALUES (?,?,?,?)"
	sql_theme = "INSERT INTO Themes(themeId, name, emoji, coinEmbed, coinTheme) VALUES (?,?,?,?,?)"

	#making lists of data to be added
	values_embeds = []
	#basic
	values_embeds.append([0,"Red","<:red:837765748670857287>","#FF0600"])
	values_embeds.append([1,"Orange","<:orange:837765758406230077>","#FF8000"])
	values_embeds.append([2,"Yellow","<:yellow:837765888802947092>","#FFED00"])
	values_embeds.append([3,"Green","<:green:837765897003073636>","#00FF1A"])
	values_embeds.append([4,"Blue","<:blue:837765904845635646>","#00EFFF"])
	values_embeds.append([5,"Purple","<:purple:837765914052263956>","#4D00FF"])
	values_embeds.append([6,"Pink","<:pink:837765922013708298>","#FF00F9"])
	#pastel
	values_embeds.append([7,"Pastel Red","<:pastel_red:837765963297587210>","#FFB1B0"])
	values_embeds.append([8,"Pastel Orange","<:pastel_orange:837765971245924412>","#FFDFB0"])
	values_embeds.append([9,"Pastel Yellow","<:pastel_yellow:837765978057080933>","#FEFFB0"])
	values_embeds.append([10,"Pastel Green","<:pastel_green:837765987969400882>","#B8FFB0"])
	values_embeds.append([11,"Pastel Blue","<:pastel_blue:837766002607128656>","#B0FFFA"])
	values_embeds.append([12,"Pastel Purple","<:pastel_purple:837766009851084811>","#D1B0FF"])
	values_embeds.append([13,"Pastel Pink","<:pastel_pink:837766018167603220>","#FAB0FF"])
	#greyscale
	values_embeds.append([14,"White","<:white:837766064892149800>","#FFFFFF"])
	values_embeds.append([15,"Light Grey","<:light_grey:837766074534854696>","#C4C4C4"])
	values_embeds.append([16,"Mid Grey","<:mid_grey:837766081846050816>","#868686"])
	values_embeds.append([17,"Dark Grey","<:dark_grey:837766090313957397>","#484848"])
	values_embeds.append([18,"Black","<:black:837766099566067772>","#000000"])

	values_themes = []
	values_themes.append([0,"Mouse",":mouse2:",":cheese:",":peanuts:"])
	values_themes.append([1,"Frog",":frog:",":fly:",":cricket:"])
	values_themes.append([2,"Spider",":spider:",":mosquito:",":butterfly:"])
	values_themes.append([3,"Duck",":duck:",":bread:",":snail:"])
	values_themes.append([4,"Seal",":seal:",":fish:",":lobster:"])
	values_themes.append([5,"Cat",":cat2:",":fish:",":mouse:"])
	values_themes.append([6,"Tiger",":tiger2:",":zebra:",":water_buffalo:"])
	values_themes.append([7,"Cow",":cow2:",":leafy_greens:",":chestnut:"])

	#inserting data
	for v in values_embeds:
		cursor.execute(sql_embed,v)
	for v in values_themes:
		cursor.execute(sql_theme,v)

	conn.commit()
	cursor.close()
	conn.close()



### MAIN ###
create_tables()
populate_tables()
