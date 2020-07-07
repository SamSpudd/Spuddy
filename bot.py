import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='-')

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
#
@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))
#
@client.command(pass_context=True)
async def help(ctx):
    
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.add_field(name='-ping', value='Gives ping to client (expressed in ms)', inline=False)
    embed.add_field(name='-kick', value='Kicks specified user', inline=False)
    embed.add_field(name='-ban', value='Bans specified user', inline=False)
    embed.add_field(name='-info', value='Gives information of a user', inline=False)
    embed.add_field(name='-invite', value='Returns invite link of the client', inline=False)
    embed.add_field(name='-clear', value='Clears an X amount of messages', inline=False)
    await client.send_message(author, embed=embed)
#
@client.command(pass_context=True)
async def clear(ctx, amount=10):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages deleted')
#
@client.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await client.send_typing(channel)
	t2 = time.perf_counter()
	embed=discord.Embed(title=None, description='Ping: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
	await client.say(embed=embed)

@client.command(pass_context=True)
async def info(ctx, user: discord.Member=None):
    if user is None:
        await client.say('Please input a user.')
    else:
        await client.say("The user's name is: {}".format(user.name) + "\nThe user's ID is: {}".format(user.id) + "\nThe user's current status is: {}".format(user.status) + "\nThe user's highest role is: {}".format(user.top_role) + "\nThe user joined at: {}".format(user.joined_at))

@client.command(pass_context=True)
async def kick(ctx, user: discord.Member=None):
    author = ctx.message.author
    if author.server_permissions.kick_members:
        if user is None:
            await client.say('Please input a user.')
        else:
            await client.say (":boot: Get kicked **{}**, Damn kid".format(user.name))
            await client.kick(user)
    else:
        await client.say('You lack permission to preform this action')

@client.command(pass_context=True)
async def ban(ctx, user: discord.Member=None):
    author = ctx.message.author
    if author.server_permissions.kick_members:
        if user is None:
            await client.say('Please input a user.')
        else:
            await client.say("Get banned **{}**, Damn kid".format(user.name))
            await client.ban(user)
    else:
        await client.say('You lack permission to preform this action')
#

client.run(token)
