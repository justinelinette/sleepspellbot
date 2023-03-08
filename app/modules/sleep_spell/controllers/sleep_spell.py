from app.modules.sleep_spell.models.sleep_spell import SleepSpell


class SleepController():
    def __init__(self, message, client):
        self.message = message
        self.client = client

    async def on_message(self):
        if self.message.content.startswith('!sleep'):
            spell = SleepSpell(self.message, self.client)
            await spell.on_message()
