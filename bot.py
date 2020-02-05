import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello":
         await message.channel.send('Hi!')
    if message.content == "-help":
         await message.channel.send('Commands: -gen spotify, -gen hulu, -gen crunchyroll, -gen nordvpn')
#if "Paid Spotify Premium" in [role.name for role in message.author.roles]:
    if message.content == "-gen spotify":
        if os.path.exists('spotify.txt'):
           lines = open('spotify.txt', encoding='utf-8').read().splitlines()
           text = random.choice(lines)
           await message.author.send(text)
        else:
            await message.channel.send("File Error. This shouldn't happen @SamSpudd#8226!")
#           
    if message.content == "-gen hulu":
        if os.path.exists('hulu.txt'):
           lines = open('hulu.txt', encoding='utf-8').read().splitlines()
           text = random.choice(lines)
           await message.author.send(text)
        else:
            await message.channel.send("File Error. This shouldn't happen @SamSpudd#8226!")
#            
    if message.content == "-gen crunchyroll":
        if os.path.exists('crunchyroll.txt'):
           lines = open('crunchyroll.txt', encoding='utf-8').read().splitlines()
           text = random.choice(lines)
           await message.author.send(text)
        else:
            await message.channel.send("File Error. This shouldn't happen @SamSpudd#8226!")
#
    if message.content == "-gen nordvpn":
        if os.path.exists('nordvpn.txt'):
           lines = open('nordvpn.txt', encoding='utf-8').read().splitlines()
           text = random.choice(lines)
           await message.author.send(text)
        else:
           await message.channel.send("File Error. This shouldn't happen @SamSpudd#8226!")
#      
if message.content == "-gen wakanim":
        if os.path.exists('wakanim.txt'):
           lines = open('wakanim.txt', encoding='utf-8').read().splitlines()
           text = random.choice(lines)
           await message.author.send(text)
        else:
           await message.channel.send("File Error. This shouldn't happen @SamSpudd#8226!")
#           
client.run(token)
