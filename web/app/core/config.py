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

    DJANGO_SECRET_KEY: str = os.getenv("DJANGO_SECRET_KEY")
    DEBUG_MODE = b(os.getenv("USE_DEBUG_MODE"))
    USE_SSL = b(os.getenv("USE_SSL"))

    SUPERUSER_PASS = os.getenv("SUPERUSER_PASS")
    SUPERUSER_NAME = os.getenv("SUPERUSER_NAME")
    SUPERUSER_EMAIL = os.getenv("SUPERUSER_EMAIL")

    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")
    URLS = os.getenv("URLS", "").split(",")

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


    


    BOT_API_URL: str = os.getenv("BOT_API_URL")



configs = Configs()