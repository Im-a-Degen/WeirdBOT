import discord

client = discord.Client()
recipient = "Im A Degen#4444" #"becca#9670"
emote_weird = "botWEIRD:937752793886912512"

@client.event
async def on_ready():
    print("Started Successfully")


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.author == recipient:
        print("yes")
        await message.add_reaction(":botWEIRD:")

    if message.content == "test":
        print("yes")
        await message.add_reaction(emote_weird)


client.run("OTM3NzUzNDM1OTQ2Nzc0NTU4.YfgU8Q.V_MphgmHMnqavECAb2nKIk4NE20")
