import os
from typing import List

from dotenv import load_dotenv

load_dotenv()

def bo(s:str, default = False):
    if(s):
        if s.lower() in ("true", "1", "yes"): return True
        else: return False
    else: return default

class Configs:

    MAIN_HOST: str = os.getenv("MAIN_HOST")
    MAIN_PORT: str = os.getenv("MAIN_PORT")

    WEB_APP_URL:str = os.getenv("WEB_APP_URL") #"https://t.me/C000lBot/larian"
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    ADMIN_ID: int = os.getenv("ADMIN_ID") #435037519



configs = Configs()