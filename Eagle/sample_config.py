import os
from dotenv import load_dotenv



load_dotenv("config.env")


class Config:
    LOGGER = True
    
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", None)
    
    TG_BOT = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
   
    MAX_MESSAGE_LENGTH = 4096
    
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "/")
    
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./DLS/")
    
    DB_URI = os.environ.get("DATABASE_URL", None)
    
    TG_URI = int(os.environ.get("TELEGRAM_URL", "-100"))
    
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    
    OWNER_ID = int(os.environ.get("OWNER_ID", None)
    
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    
    TG_MAX_SELECT_LEN = 100
    
    TG_IRU_S_M_ID = int(os.environ.get("TG_IRU_S_M_ID", "0"))
    WARN_DATA_ID = int(os.environ.get("WARN_DATA_ID", "0"))
    WARN_SETTINGS_ID = int(os.environ.get("WARN_SETTINGS_ID", "0"))
    
    A_PIN_MESSAGE_ID = int(os.environ.get("A_PIN_MESSAGE_ID", "3"))
    
    LAYER_FEED_CHAT = os.environ.get("LAYER_FEED_CHAT", None)
    LAYER_UPDATE_INTERVAL = os.environ.get("LAYER_UPDATE_INTERVAL", None)
    LAYER_UPDATE_MESSAGE_CAPTION = os.environ.get("LAYER_UPDATE_MESSAGE_CAPTION", None)


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
