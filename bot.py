import os, discord, random
from discord.ext import commands
from discord.utils import get

# We'll need to substitute the Prefix for an Enviroment Variable
BOT_PREFIX = os.environ['prefix'] # -Prfix is need to declare a Command in discord ex: !pizza "!" being the Prefix
TOKEN = os.environ['token'] # The token is also substituted for security reasons

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
    await ctx.send("Congratulations, Contact {}".format(author.mention) + "Recruiter to arange a date and time")
    
@bot.command(pass_context=True)
async def trial(ctx):
     author = ctx.message.author
     role = discord.utils.get(ctx.message.guild.roles, name="Team Recruiter \U0001F3AE")
     if role is None:
        await bot.say('There is no "Team Recruiter" role on this server!')
        return
     else:
        tag = random.choice(role.members)
        print(str(tag))
        await ctx.send("Hi {}".format(tag.mention) + ", the application of {}".format(author.mention) + " has been assigned to you.")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="JDM Application bot", description="Tags recruiters because we cba.", color=0xeee657)

# give info about you here
    embed.add_field(name="Author", value="<@160455573324824576>")

# Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

# give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](<https://discordapp.com/api/oauth2/authorize?client_id=572406563873226753&permissions=2048&scope=bot>)")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name="$trial", value="tags a random recruiter", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run(TOKEN)
