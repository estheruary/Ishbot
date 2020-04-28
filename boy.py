import os

import discord
import random 
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='/i ')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event 
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the {member.guild} server! My name is Ishbot, your humble servant.'
    )


@bot.command(name = 'roll', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice, number_of_sides):
    try:
        number_of_dice = int(float(number_of_dice))
        number_of_sides = int(float(number_of_sides))
        dice = [
            str(random.choice(range(1, number_of_sides +1)))
            for _ in range(number_of_dice)
            ]
        await ctx.send(', '.join(dice))
    except:
        await ctx.send("I don't understand what you want me to do.")

@bot.command(name = 'blackjack', help='Play a game of Blackjack with Ishbot!')
async def deal(ctx):
    await ctx.send("I don't know how to play that yet, but I will soon!")

@bot.command(name = 'hookers', help="Wouldn't you like to know?")
async def hooker(ctx):
    await ctx.send("We don't have hookers just yet, sorry")



@bot.command(name = 'who_is_a_good_boy', help='Returns who is a good boy.')
async def who_is_a_good_boi(ctx):
    await ctx.send('*barks happily*')

bot.run(TOKEN)
