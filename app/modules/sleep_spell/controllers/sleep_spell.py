
import discord
from app.modules.sleep_spell.models.sleep_spell import calc_results
from app.modules.sleep_spell.models.enemy import Enemy


class SleepController():

    def __init__(self, message, client):
        self.message = message
        self.response_channel = discord.utils.get(
            self.message.guild.channels, name="general")
        self.client = client

    async def sleep_dmg(self):
        # collect user inputs one by one
        await self.message.channel.send("enter sleep damage:")
        sleep_dmg = await self.client.wait_for('message')
        return int(sleep_dmg.content)

    async def enemy_hps(self):
        await self.message.channel.send(f"enter enemy hps separated by commas (ie. '10, 20, 30' ):")
        user_hp_input = await self.client.wait_for('message')
        return user_hp_input.content.split(',')

    async def create_enemies(self, enemy_hps):
        enemies = []
        for i, enemy_hp in enumerate(enemy_hps):
            name = f"enemy {i+1}"
            enemies.append(Enemy(name, int(enemy_hp)))
        enemies.sort(key=lambda x: int(x.hp), reverse=True)
        return enemies

    async def response(self, result):
        if "is asleep." in result:
            emoji = ":zzz:"
        else:
            emoji = ":alarm_clock:"
        await self.response_channel.send(f"\u2022  {emoji}  {result} \n")

    async def results(self, enemies, sleep_dmg):
        for result in calc_results(enemies, sleep_dmg):
            await self.response(result)

    async def on_message(self):
        if self.message.content.startswith('!sleep'):
            sleep_dmg = await self.sleep_dmg()
            enemy_hps = await self.enemy_hps()
            enemies = await self.create_enemies(enemy_hps)
            return await self.results(enemies, sleep_dmg)
