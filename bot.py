import os, discord, random
from discord.ext.commands import Bot

# We'll need to substitute the Prefix for an Enviroment Variable
BOT_PREFIX = os.environ['prefix'] # -Prfix is need to declare a Command in discord ex: !pizza "!" being the Prefix
TOKEN = os.environ['token'] # The token is also substituted for security reasons

client = Bot(command_prefix=BOT_PREFIX)

bot = commands.Bot(command_prefix='$')

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

@bot.command()
async def trial(ctx):
     author = ctx.message.author
     role = discord.utils.get(ctx.message.guild.roles, name="Team Recruiter")
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
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)

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

    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run('NTcyNDA2NTYzODczMjI2NzUz.XMgdsw.lYs2CiyK_I2ULYx_ammja-1O7VA')
