import discord
from discord.ui import Button, View, Select
from discord import app_commands
from discord.ext import commands
import os
import logging
import logging.handlers

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
API_URL = os.getenv("API_URL")

GUILD = os.getenv("DISCORD_GUILD")

GAMES = []
ROLES_WOLF_PACK= [
    {
        'name': 'Alpha Wolf',
        'faction': 'Wolf Pack',
        'emoji': '🐺',
        'corrupted': True,
    },
    {
        'name': 'Pack Wolf',
        'faction': 'Wolf Pack',
        'emoji': '🐺',
        'corrupted': True,
    },

    {
        'name': 'Wolf Pup',
        'faction': 'Wolf Pack',
        'emoji': '🐺🐕',
        'corrupted': True,
    },
    {
        'name': 'Defector',
        'faction': 'Wolf Pack',
        'emoji': '🔄',
    },
]

ROLES_VILLAGE = [
    {
        'name': 'Farmer',
        'secret_role': 'Hero Farmer',
        'faction': 'Village',
        'emoji': '🧑‍🌾',
        'secret_emoji': '💪🧑‍🌾',
    },
    {
        'name': 'Farmer',
        'secret_role': 'Wolf Farmer',
        'faction': 'Village',
        'emoji': '🧑‍🌾',
        'secret_emoji': '🐺🧑‍🌾',
    },
    {
        'name': 'Clairvoyant',
        'faction': 'Village',
        'mystic': True,
        'emoji': '🔮',
    },
    {
        'name': 'Witch',
        'faction': 'Village',
        'mystic': True,
        'emoji': '🧙‍♀️',
    },
    {
        'name': 'Medium',
        'faction': 'Village',
        'mystic': True,
        'emoji': '👻',
    },
    {
        'name': 'Healer',
        'faction': 'Village',
        'mystic': True,
        'emoji': '💖',
    },
    {
        'name': 'Bard',
        'faction': 'Village',
        'emoji': '🎤',
    },
    {
        'name': 'Innkeeper',
        'faction': 'Village',
        'emoji': '🍻',
    },
    {
        'name': 'Hermit',
        'faction': 'Village',
        'emoji': '🏠',
    },
    {
        'name': 'Monk',
        'faction': 'Village',
        'emoji': '🙏',
    },
    {
        'name': 'Priest',
        'faction': 'Village',
        'emoji': '✝️',
    },
    {
        'name': 'Sinner ',
        'faction': 'Village',
        'corrupted': True,
        'emoji': '😈',
    },
    {
        'name': 'Seducer',
        'faction': 'Village',
        'corrupted': True,
        'emoji': '💋',
    },
    {
        'name': 'Madman',
        'faction': 'Third Party',
        'emoji': '🌀',
    },
    {
        'name': 'Jester',
        'faction': 'Third Party',
        'emoji': '🎭',
    },
]
ROLES = ROLES_WOLF_PACK + ROLES_VILLAGE

def roles_to_verbose(roles):
    verbose_lines = ''
    for role in roles:
        verbose_lines.append(
            f'{role['name']} {role['emoji']} ({role['faction']}) {🖤 if role.get("corrupted") else ""} {✨ if role.get("mystic") else ""}'
        )
    return '\n'.join(verbose_lines)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD))
    print(f'We have logged in as {client.user}')

async def intialize_game(
        interaction,
        data={},
    ):
    game_id = 1
    if game_id in GAMES:
        roles = ROLES
        GAMES[game_id] = {
            'stage': 'role_distribution',
            'initial_roles': roles
            'players': [],
            'moderators': [],
        }
    current_game = GAMES[game_id]
    embed = discord.Embed(
        title="Lets Play!",
        description="Roles at play:\n"+ roles_to_verbose()
    )
    #if image:
    #    embed.set_image()
    await interaction.response.send_message(embed=embed)



class GameSelect(Select):
    stage_name = 'prop'
    data = {}

    def __init__(self, stage_name, data, **kwargs):
        self.data = data
        self.stage_name = stage_name
        return super().__init__(**kwargs)
            
    
    async def callback(self, interaction: discord.Interaction):
        self.data[self.stage_name] = self.values[0]
        stage = get_stage_by_name(self.stage_name)
        next_stage_name = stage['get_next_step'](**self.data)
        return await discord_predictions(
            interaction=interaction,
            stage_name=next_stage_name,
            selected_value=self.values[0],
            data=self.data,
        )


class BetView(View):

    def __init__(self, stage_name=None, data={}, select={}):
        
        super().__init__()
        self.add_item(
            GameSelect(stage_name, data, **select)
        )


@tree.command(name="play", description="Starts a game", guild=discord.Object(id=GUILD))
async def slash_command(interaction:discord.Interaction):
    try:
        await intialize_game(interaction=interaction, data={})
    except Exception as e:
        logger.error(e)
        await interaction.response.send_message("Server Error")


client.run(os.getenv("DISCORD_TOKEN"))
