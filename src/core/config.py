import secrets
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()
CORE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # SUPABASE
    DATABASE_URL: str = ""
    SUPABASE_URL: str = ""
    SUPABASE_KEY: str = ""
    SUPABASE_BUCKET: str = ""

    # GOOGLE OAUTH
    MAIL_USERNAME: str = ""
    MAIL_PASSWORD: str = ""
    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""
    GOOGLE_REDIRECT_URI: str = ""

    # JWT CONFIGURATION
    SECRET_KEY: str = secrets.token_hex(32)
    ALGORITHM: str = "HS256"
    TIME_MINUTES: int = 30

    FIREBASE_CREDENTIALS_PATH: str = str(CORE_DIR / "golazo-b1c36-firebase-adminsdk-fbsvc-33611d463a.json")

    origins: list[str] = [
        "*",
        "http://localhost:5173",
    ]

    LOG_LEVEL: str = "INFO"


settings = Settings()
