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
    if message.content == "-Clear":
        
      if message.channel.type == 'text':
        message.channel.fetchMessages()
        message.channel.bulkDelete(messages);
        messagesDeleted = messages.array().length;

        message.channel.sendMessage("Deletion of messages successful. Total messages deleted: "+messagesDeleted);
        console.log('Deletion of messages successful. Total messages deleted: '+messagesDeleted);
          
client.run(token)

