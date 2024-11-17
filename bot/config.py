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

    WEB_APP_URL:str = "https://3eac-95-26-124-223.ngrok-free.app/"
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    ADMIN_ID: int = 6768853571



configs = Configs()