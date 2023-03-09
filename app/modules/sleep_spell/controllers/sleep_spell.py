from app.modules.sleep_spell.models.response import Response
from app.modules.sleep_spell.models.sleep_spell import SleepSpell


class SleepController():
    def __init__(self, message, client):
        self.message = message
        self.client = client
        self.VALID_PREFIXES = ["!sleep", "!response"]

    def validate_prefix(self, prefix):
        if prefix in self.VALID_PREFIXES:
            return prefix
        else:
            return False

    async def on_message(self, prefix):
        prefix = self.validate_prefix(prefix)
        if self.message.content.startswith(prefix):
            if prefix == "!sleep":
                spell = SleepSpell(self.message, self.client)
            elif prefix == "!response":
                spell = Response(self.message, self.client)
            await spell.on_message()
