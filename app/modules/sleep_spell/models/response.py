import os
import discord


class Response():

    def __init__(self, message, client):
        self.message = message
        self.client = client

    async def change_response(self, channel_name):
        os.environ["RESPONSE_CHANNEL"] = channel_name
        self.response_channel = discord.utils.get(
            self.message.guild.channels, name=os.environ.get("RESPONSE_CHANNEL"))
        await self.response_channel.send(f"your response channel has changed to {channel_name}")

    async def on_message(self):
        if self.message.content.startswith("!response"):
            channel_name = self.message.content.split(" ")[1]
            print(channel_name)
            return await self.change_response(channel_name)
