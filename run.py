
from app.config.config import Config
from app.modules.sleep_spell.events.sleep_spell import Bot


# subprocess.run(["pip", "install", "--upgrade", "pip"], capture_output=True)

Bot().start_bot(Config().DISCORD_TOKEN)
