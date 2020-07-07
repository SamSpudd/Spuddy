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
#@commands.cooldown(1, 10, BucketType.user)
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello":
         await message.channel.send('Hi!')
#if message.content == "-help":
         embed = discord.Embed(title="Commands", description="Here are the commands that work with the bot!", color=0x00ff00)
         embed.add_field(name="Generate Spotify", value="-gen spotify", inline=True)
         embed.add_field(name="Generate Hulu", value="-gen hulu", inline=True)
         embed.add_field(name="Generate Crunchyroll", value="-gen crunchyroll", inline=True)   
         embed.add_field(name="Generate NordVPN", value="-gen nordvpn", inline=True)
         embed.add_field(name="Generate Wakanim", value="-gen wakanim", inline=True)
         embed.add_field(name="Generate Nitro", value="-gen nitro", inline=True)
         embed.add_field(name="Generate DisneyPlus", value="-gen disney", inline=True)   
         await message.channel.send(embed=embed)
#if "Paid Spotify Premium" in [role.name for role in message.author.roles]:
    #if message.content == "-gen spotify":
        if os.path.exists('spotify.txt'):
           lines = open('spotify.txt', encoding='utf-8').read().splitlines()
           text = random.choice(lines)
           await message.author.send(text)
        else:
            await message.channel.send("File Error. This shouldn't happen @SamSpudd#8226!")
#           
    #if message.content == "-gen hulu":
        if os.path.exists('hulu.txt'):
           lines = open('hulu.txt', encoding='utf-8').read().splitlines()
           text = random.choice(lines)
           await message.author.send(text)
        else:
            await message.channel.send("File Error. This shouldn't happen @SamSpudd#8226!")
#            
    #if message.content == "-gen crunchyroll":
        if os.path.exists('crunchyroll.txt'):
           lines = open('crunchyroll.txt', encoding='utf-8').read().splitlines()
           text = random.choice(lines)
           await message.author.send(text)
        else:
            await message.channel.send("File Error. This shouldn't happen @SamSpudd#8226!")
#
    #if message.content == "-gen nordvpn":
        if os.path.exists('nordvpn.txt'):
           lines = open('nordvpn.txt', encoding='utf-8').read().splitlines()
           text = random.choice(lines)
           await message.author.send(text)
        else:
           await message.channel.send("File Error. This shouldn't happen @SamSpudd#8226!")
#      
    #if message.content == "-gen wakanim":
        if os.path.exists('wakanim.txt'):
           lines = open('wakanim.txt', encoding='utf-8').read().splitlines()
           text = random.choice(lines)
           await message.author.send(text)
        else:
           await message.channel.send("File Error. This shouldn't happen @SamSpudd#8226!")
#      
    #if message.content == "-gen nitro":
        if os.path.exists('nitro.txt'):
           lines = open('nitro.txt', encoding='utf-8').read().splitlines()
           text = random.choice(lines)
           await message.author.send(text)
        else:
           await message.channel.send("File Error. This shouldn't happen @SamSpudd#8226!")
#  
    #if message.content == "-gen disney+":
        if os.path.exists('disney.txt'):
           lines = open('disney.txt', encoding='utf-8').read().splitlines()
           text = random.choice(lines)
           await message.author.send(text)
        else:
           await message.channel.send("File Error. This shouldn't happen @SamSpudd#8226!")
# 
const args = message.content.split(' ').slice(1); // All arguments behind the command name with the prefix
const amount = args.join(' '); // Amount of messages which should be deleted

if (!amount) return msg.reply('You haven\'t given an amount of messages which should be deleted!'); // Checks if the `amount` parameter is given
if (isNaN(amount)) return msg.reply('The amount parameter isn`t a number!'); // Checks if the `amount` parameter is a number. If not, the command throws an error

if (amount > 100) return msg.reply('You can`t delete more than 100 messages at once!'); // Checks if the `amount` integer is bigger than 100
if (amount < 1) return msg.reply('You have to delete at least 1 message!'); // Checks if the `amount` integer is smaller than 1

await msg.channel.messages.fetch({ limit: amount }).then(messages => { // Fetches the messages
    msg.channel.bulkDelete(messages // Bulk deletes all messages that have been fetched and are not older than 14 days (due to the Discord API)
)});
#
client.run(token)
