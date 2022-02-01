import discord
from BOTrequiredDataPrivate import *

client = discord.Client()
pogD_token = True


@client.event
async def on_ready():
    print("Started Successfully")


@client.event
async def on_message(message):
    if message.author != client.user:

        if str(message.author) == weird_recipient:
            print("yes")
            await message.add_reaction(emote_weird)

        if message.content == emote_pogD:
            print("pogD detected")
            global pogD_token
            if pogD_token:
                print("pogD time")
                pogD_token = False
                await message.channel.send("<:botPogD:937903199698952233>")
        else:
            pogD_token = True


client.run(bot_key)
