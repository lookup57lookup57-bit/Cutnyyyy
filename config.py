import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
JOIN_CHANNEL_ID = int(os.getenv("JOIN_CHANNEL_ID"))
JOIN_CHANNEL_USERNAME = os.getenv("JOIN_CHANNEL_USERNAME")
ADMIN_IDS = {int(x) for x in os.getenv("ADMIN_IDS").split(",")}