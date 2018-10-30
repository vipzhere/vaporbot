import discord
from discord.ext import commands
import asyncio
from itertools import cycle


TOKEN = 'NTA2NTA2NDA3NTAwMTg1NjIw.DrjJXQ.munSyGEw33DImUeZ0JFXSGOUJ5c'

client = commands.Bot(command_prefix = "!")
client.remove_command('help')
status = ['!help', 'vaporbot.com', 'created by ViPz']

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(5)


@client.event
async def on_ready():
    print("Vapor is now online, and is ready to use.")

@client.command()
async def ving():
    await client.say("vong!")

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

@client.command(pass_context=True)
async def clear(ctx, amount=50):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say("Messages succesfully removed.")

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Member')
    await client.add_roles(member, role)

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.purple()
    )

    embed.set_author(name='Vapor Commands')
    embed.add_field(name='!ving', value='Returns the word vong.', inline=False)
    embed.add_field(name='!echo', value="Type in some text after it, and it will return the text you've entered.", inline=False)
    embed.add_field(name='!clear', value='Clear messages from 1 - 49.', inline=False)


    await client.send_message(author, embed=embed)

@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@client.event
async def on_reaction_remove(reaction, user):
        channel = reaction.message.channel
        await client.send_message(channel, '{} has removed {} from the message: {}'.format(user.name, reaction.emoji, reaction.message.content))



client.loop.create_task(change_status())
client.run(TOKEN)
