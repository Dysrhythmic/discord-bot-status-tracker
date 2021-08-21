import discord
import os
import json
from datetime import datetime
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix="!", intents=intents)
load_dotenv()
token = os.getenv("BOT_TOKEN")

status_log = {}


def update_log(m_id, m_name, date, last_status):
    status_log[str(m_id)] = {
        "name": m_name,
        "date": date,
        "last status": last_status,
    }
    try:
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
    except(FileNotFoundError):
        with open('data.json', 'w') as json_file:
            json.dump(status_log, json_file, indent=4, default=str)
    else:
        data.update(status_log)
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4, default=str)


def last_seen(last_online, now):
    last_seen_time = datetime.strptime(last_online, '%Y-%m-%d %H:%M:%S.%f')
    delta = now - last_seen_time
    return delta


def log_status(member):
    now = datetime.now()
    name = f'{member.name}#{member.discriminator}'
    update_log(member.id, name, now, str(member.status))
    

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.event
async def on_member_update(before, after):
    if before.status != after.status:
        log_status(after)


@bot.command(aliases=["ping"])
async def hello(ctx):
    await ctx.channel.send("Hello!")


@bot.command(aliases=["refresh"])
async def update(ctx):
    await ctx.channel.send("Updating Status Log:tm:...")
    now = datetime.now()
    for member in bot.get_all_members():
        if str(member.status) != "offline":
            name = f'{member.name}#{member.discriminator}'
            update_log(member.id, name, now, str(member.status))
    await ctx.channel.send("Update complete!")


@bot.command(aliases=["ls"])
async def lastseen(ctx):
    usernames = ctx.message.mentions
    with open('data.json', 'r') as json_file:
         data = json.load(json_file)
    for user in usernames:
        last_online = data[str(user.id)]['date']
        await ctx.channel.send(
            f"I last saw {user.name} {last_seen(last_online, datetime.now())} ago!"
        )


@bot.command()
async def status(ctx):
    usernames = ctx.message.mentions
    with open('data.json', 'r') as json_file:
         data = json.load(json_file)
    for user in usernames:
        await ctx.channel.send(
            f'The last status I saw for {user.name} was {data[str(user.id)]["last status"]}!'
        )


@bot.command(aliases=["pl"])
async def printlog(ctx):
    await ctx.channel.send("Here are the people I have logged:")
    with open('data.json', 'r') as json_file:
         data = json.load(json_file)
    for member_id in data:
        member_name = ctx.message.guild.get_member(int(member_id))
        await ctx.channel.send(member_name)
    await ctx.channel.send('...That\'s it!')


bot.run(token)
