import os, discord, random
from discord.ext import commands
from discord.utils import get

# We'll need to substitute the Prefix for an Enviroment Variable
BOT_PREFIX = os.environ['prefix'] # -Prfix is need to declare a Command in discord ex: !pizza "!" being the Prefix
TOKEN = os.environ['token'] # The token is also substituted for security reasons
LOGO = os.environ['logo']

bot = commands.Bot(command_prefix=BOT_PREFIX)


@bot.event
async def on_ready():
    print('discord version:')
    print(discord.__version__)
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print('Owner: Kirbae#0001')
    print('------')
    servers = list(bot.guilds)
    print('Connected on '+ str(len(servers)) + ' servers:')
    print('\n'.join('>'+ server.name for server in servers))
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)
    
@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command(pass_context=True)
@commands.has_role("Team Recruiter \U0001F3AE") # This must be exactly the name of the appropriate role
async def accept(ctx, user: discord.Member):
    author = ctx.message.author
    role = discord.utils.get(ctx.message.guild.roles, name="Trial")
    await user.add_roles(role)    
    await ctx.send("Congratulations, Contact {}".format(author.mention) + " or your assigned recruiter to arange a date and time")
    
@bot.command(pass_context=True)
async def trial(ctx):
     author = ctx.message.author
     role = discord.utils.get(ctx.message.guild.roles, name="Team Recruiter \U0001F3AE")
     if role is None:
        await bot.say('There is no "Team Recruiter" role on this server!')
        return
     else:
        tag = random.choice(role.members)
        print('selected ' + str(tag) + ' as recruiter for ' + str(author))
        await ctx.send("Welcome {}".format(author.mention) + ", thanks for applying. Recruiter {}".format(tag.mention) + " has been assigned to you.")
        
        
@bot.command()
async def logo(ctx):
    await ctx.send(LOGO)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="JDM Application bot", description="Tags recruiters because we cba.", color=0xeee657)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/553318357563080704/564915982544666634/jdmlogo.png")
# give info about you here
    embed.add_field(name="Author", value="<@160455573324824576>")

# Shows the number of servers the bot is member of.
    embed.add_field(name="Slide's twitch channel", value="[Twitch](<https://www.twitch.tv/mobyinkface>)")

    embed.add_field(name="This bot is open source", value="[Github link](<https://github.com/Kirbae00/jdm-disc-bot>)")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="JDM Application bot", description="Bot for us lazy admins. List of commands are:", color=0xeee657)
    
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/553318357563080704/564915982544666634/jdmlogo.png")
    embed.add_field(name=BOT_PREFIX + "trial", value="tags a random recruiter", inline=False)
    embed.add_field(name=BOT_PREFIX + "accept", value="accepts the user and adds their trial role. Usage: " + BOT_PREFIX + "accept @user", inline=False)
    embed.add_field(name=BOT_PREFIX + "logo", value="Displays the logo", inline=False)
    embed.add_field(name=BOT_PREFIX + "info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name=BOT_PREFIX + "help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run(TOKEN)
