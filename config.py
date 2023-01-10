# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "25972502"))
API_HASH = os.environ.get("API_HASH", "7709c5db2be15ec7380e2ad6a612e3d7")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5893897086:AAFrKja66WfeMmjR5xsjvNqSsdUmtJR-xpE")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5178783941")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "a2zbackup")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Abhigupta77:<password>@cluster0.ccb8umw.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5178783941")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5178783941)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001866027601")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Gplinks") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
