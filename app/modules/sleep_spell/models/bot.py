import discord
from app.config.config import Config
from app.modules.sleep_spell.controllers.sleep_spell import SleepController

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guilds = True
intents.message_content = True
client = discord.Client(intents=intents)


class Bot():

    def start_bot(DISCORD_TOKEN):

        @client.event
        async def on_ready():
            print('Logged in as {0.user}'.format(client))

        @client.event
        async def on_message(message):
            await SleepController(message, client).on_message()

        client.run(DISCORD_TOKEN)
