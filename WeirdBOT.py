import discord
from BOTrequiredDataPrivate import *

client = discord.Client()


@client.event
async def on_ready():
    print("Started Successfully")


@client.event
async def on_message(message):
    if message.author != client.user:

        if str(message.author) == weird_recipient:
            print("yes")
            await message.add_reaction(emote_weird)


client.run(bot_key)
