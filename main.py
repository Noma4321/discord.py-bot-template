import os
from typing import Generator
import discord
from discord.ext import commands
import random
import time
import json
import string

#config load

with open("config.json", "r") as f:
    config = json.load(f)


token = config["token"]

owner = config["ownerid"]

def get_prefix(client, message):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]



client = commands.Bot(command_prefix = get_prefix)

def allguilds():
    print("======================")
    print("here is all the guilds:")
    for guild in client.guilds:
        print("------------")
        print('name: ' + guild.name)
        print(f'id: {guild.id}')
        print(f'members amount:{guild.member_count}')
        print("------------")
    print("======================")

def makeprefixes():
    for guild in client.guilds:
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        if not str(guild.id) in prefixes or len(prefixes[str(guild.id)]) == 0:
            with open("mainprefix.json", "r") as file:
                mainprefixes = json.load(file)
                prefix = mainprefixes[str("prefix")]
            prefixes[str(guild.id)] = prefix
        with open("prefixes.json", "w") as f:
            json.dump(prefixes,f)
            print("we have another guild!")
            print(guild.name)
    else:
            print()


print("prefix: idk")

@client.event
async def on_guild_join(guild):
    print("joined another guild!")
    print(guild.name)

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = ">"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)




@client.command()
@commands.has_permissions(administrator = True)
async def changeprefix(ctx, prefix):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)   
    await ctx.send(f"The prefix was changed to {prefix}")


@client.command()
async def changemainprefix(ctx, prefix):
    id = int(ctx.author.id)
    if id == int(owner):
        
        with open("mainprefix.json", "r") as f:
            prefixes = json.load(f)
        prefixes[str("prefix")] = prefix
        with open("mainprefixes.json", "w") as f:
            json.dump(prefixes,f)    
        await ctx.send(f"The main prefix was changed to {prefix}")
    else:
        await ctx.send("only owners allowed to use this!")


@client.command()
async def ping(ctx):
    await ctx.send(client.latency)

@client.event
async def on_message(msg):
    try:
        if msg.mentions[0] == client.user:

            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)

            pre = prefixes[str(msg.guild.id)] 

            await msg.channel.send(f"My prefix for this server is {pre}")

    except:
        pass

    await client.process_commands(msg)


@client.command(aliases=["sd"])
async def command_name(ctx):
    if ctx.author.id == owner:
        await ctx.send("Shutting down...")
        time.sleep(3)
        quit("shutted down")
    else:
        await ctx.send("This is a owner only command")



@client.event
async def on_ready():
    allguilds()
    makeprefixes()
    print("======================")
    print("   Logged on as:")
    print(f"   {client.user}")
    print("======================")
    
    print("The dev of this template is noma4321#0035")
    print("youtube: https://www.youtube.com/channel/UC4diJpbj8WT80uzCdK3BtvA")
    print("credit me if you are sharing this template")

try:
    client.run(token)
except:
    print("Pls make sure the token is working and all configured correctly")