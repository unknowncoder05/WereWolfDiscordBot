import discord
from discord.ui import Button, View, Select
from discord import app_commands
from discord.ext import commands
import os
import logging
import logging.handlers
from polls import intialize_vote
from game import intialize_game

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
API_URL = os.getenv("API_URL")

GUILD = os.getenv("DISCORD_GUILD")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD))
    print(f'We have logged in as {client.user}')


@tree.command(name="play", description="Starts a game", guild=discord.Object(id=GUILD))
async def start_game(interaction:discord.Interaction):
    try:
        await intialize_game(interaction=interaction, data={})
    except Exception as e:
        logger.error(e)
        await interaction.response.send_message("Server Error")


@tree.command(name="vote", description="Starts a vote", guild=discord.Object(id=GUILD))
async def start_vote(interaction:discord.Interaction):
    try:
        await intialize_vote(interaction=interaction, data={})
    except Exception as e:
        logger.error(e)
        await interaction.response.send_message("Server Error")


client.run(os.getenv("DISCORD_TOKEN"))
