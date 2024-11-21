import os
from typing import List

from dotenv import load_dotenv

load_dotenv()

def b(s:str, default = False):
    if(s):
        if s.lower() in ("true", "1", "yes"): return True
        else: return False
    else: return default

class Configs:
    PROJECT_NAME: str = "mailing_core"

    API: str = "/api"

    PROJECT_ROOT: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    DEBUG_MODE = b(os.getenv("USE_DEBUG_MODE"))
    USE_SSL = b(os.getenv("USE_SSL"))

    MAIN_HOST = os.getenv("MAIN_HOST")
    MAIN_URL = os.getenv("MAIN_HURL")

    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    DB_ENGINE_MAPPER: dict = {
        "postgresql": "postgresql+",
        "mysql": "mysql+pymysql",
    }


    
    

    class DB:
        USER: str = os.getenv("DB_USER")
        PASSWORD: str = os.getenv("DB_PASSWORD")
        HOST: str = os.getenv("DB_HOST")
        PORT: str = os.getenv("DB_PORT")
        ENGINE: str = "postgresql+asyncpg"
        NAME: str =  os.getenv("DB_NAME")


        URL_FORMAT: str = "{db_engine}://{user}:{password}@{host}:{port}/{database}"

        URL = "{db_engine}://{user}:{password}@{host}:{port}/{database}".format(
            db_engine=ENGINE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            database=NAME,
        )


    DJANGO_SECRET_KEY: str = os.getenv("DJANGO_SECRET_KEY")


    BOT_API_URL: str = os.getenv("BOT_API_URL")



configs = Configs()