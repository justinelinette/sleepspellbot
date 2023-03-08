import discord
from app.config.config import Config
from app.modules.sleep_spell.controllers.sleep_spell import SleepController


class Bot():

    def __init__(self):
        self.intents = discord.Intents.default()
        self.intents.members = True
        self.intents.messages = True
        self.intents.guilds = True
        self.intents.message_content = True
        self.client = discord.Client(intents=self.intents)

    def start_bot(self, DISCORD_TOKEN):

        @self.client.event
        async def on_ready():
            print('logged in as {0.user}'.format(self.client))

        @self.client.event
        async def on_message(message):
            await SleepController(message, self.client).on_message()

        self.client.run(DISCORD_TOKEN)
