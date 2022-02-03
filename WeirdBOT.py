import os
from discord.ext import commands
from BOTrequiredDataPublic import *
from omegaMaker import *

weird_bot = commands.Bot(command_prefix="!")

chain_cooldown = 0
airstrike_controller = ""
ratio_cooldown = 0
ratio_enabled = True


@weird_bot.event
async def on_ready():
    print("Started Successfully")

weird_bot.remove_command("help")


@weird_bot.event
async def on_message(message):
    if message.author != weird_bot.user:
        global chain_cooldown, ratio_cooldown

        if message.author.id == weird_recipient:
            await message.add_reaction(emote_weird)

        if message.content == emote_pogD:
            if chain_cooldown == 0:
                chain_cooldown = 5
                await message.channel.send("<:botPogD:938659073669353494>")
        elif chain_cooldown != 0:
            chain_cooldown -= 1

        if "+" in message.content and ratio_cooldown == 0 and ratio_enabled:
            if ("L" in message.content.upper() or "RATIO" in message.content.upper()
                    or "WHITE" in message.content.upper() or "FELL OFF" in message.content.upper()):
                if "L" not in message.content.upper():
                    ratio_cooldown += 5
                    await message.channel.send("+ L")
                if "RATIO" not in message.content.upper():
                    ratio_cooldown += 5
                    await message.channel.send("+ ratio")
                if "WHITE" not in message.content.upper():
                    ratio_cooldown += 5
                    await message.channel.send("+ you're white")
                if "FELL" not in message.content.upper():
                    ratio_cooldown += 5
                    await message.channel.send("+ you fell off")
        elif ratio_cooldown != 0:
            ratio_cooldown -= 1
    await weird_bot.process_commands(message)


@weird_bot.event
async def on_reaction_add(reaction, user):
    global airstrike_controller
    if user == airstrike_controller:
        airstrike_controller = ""
        for i in range(0, 15):
            await reaction.message.add_reaction(airstrike_ammo[i])


@weird_bot.command()
async def ratiostate(ctx):
    global ratio_enabled, ratio_cooldown
    if ratio_enabled:
        ratio_enabled = False
        await ctx.message.channel.send("Auto ratio disabled", delete_after=5)
    else:
        ratio_enabled = True
        await ctx.message.channel.send("Auto ratio enabled", delete_after=5)
        ratio_cooldown = 0
    await ctx.message.delete()


@commands.cooldown(1, 15, commands.BucketType.guild)
@weird_bot.command()
async def airstrike(ctx):
    global airstrike_controller
    airstrike_controller = ctx.message.author
    await ctx.message.channel.send("Ready to fire. React to the airstrike target.", delete_after=5)
    await ctx.message.delete()


@commands.cooldown(1, 5, commands.BucketType.guild)
@weird_bot.command()
async def omegaconvert(ctx):
    await ctx.message.channel.send(omegalul_converter(ctx.message.content.lstrip("!omegaconvert ")))


@weird_bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("Command on cooldown", delete_after=5)
        await ctx.message.delete()

weird_bot.run(os.environ.get("BOTKEY"))

