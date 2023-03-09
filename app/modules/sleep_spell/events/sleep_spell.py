import discord
from app.config.config import Config
from app.modules.sleep_spell.controllers.sleep_spell import SleepController

config = Config()


class Bot():

    def __init__(self):
        self.intents = discord.Intents.default()
        self.intents.members = True
        self.intents.messages = True
        self.intents.guilds = True
        self.intents.message_content = True
        self.client = discord.Client(intents=self.intents)

    def start_bot(self):

        @self.client.event
        async def on_ready():
            print("logged in as {0.user}".format(self.client))

        @self.client.event
        async def on_message(message):
            prefix = message.content.split(" ")[0]
            if prefix.startswith("!"):
                await SleepController(message, self.client).on_message(prefix)

        self.client.run(config.DISCORD_TOKEN)
