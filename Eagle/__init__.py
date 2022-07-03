import logging
import uvloop
import time
from pyrogram import Client
from config import API_HASH, API_ID, SESSION
import logging

import logging

logging.basicConfig(
    filename="app.txt",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
LOGGER = logging.getLogger(__name__)

HELP = {}
CMD_HELP = {}

StartTime = time.time()

app = Client(name="eagle", session_string=SESSION, api_id=API_ID, api_hash=API_HASH)

uvloop.install()
