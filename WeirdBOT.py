import discord
from BOTrequiredData import *

client = discord.Client()


@client.event
async def on_ready():
    print("Started Successfully")


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.author == recipient:
        print("yes")
        await message.add_reaction(emote_weird)

    if message.content == "test":
        print("yes")
        await message.add_reaction(emote_weird)


client.run(bot_key)
