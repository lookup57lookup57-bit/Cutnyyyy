import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
ADMIN_IDS = {int(x) for x in os.getenv("ADMIN_IDS").split(",")}
FERNET_KEY = os.getenv("FERNET_KEY")