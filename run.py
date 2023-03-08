from app.modules.sleep_spell.models.bot import Bot
from app.config.config import Config
import subprocess

# subprocess.run(["pip", "install", "--upgrade", "pip"], capture_output=True)


Bot.start_bot(Config().DISCORD_TOKEN)
