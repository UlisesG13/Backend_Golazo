import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
CORE_DIR = Path(__file__).resolve().parent


class Settings:
    # SUPABASE
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SUPABASE_URL: str = os.getenv("SUPABASE_URL")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")
    SUPABASE_BUCKET: str = os.getenv("SUPABASE_BUCKET")

    # GOOGLE OAUTH
    MAIL_USERNAME: str = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD: str = os.getenv("MAIL_PASSWORD")
    GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET: str = os.getenv("GOOGLE_CLIENT_SECRET")
    GOOGLE_REDIRECT_URI: str = os.getenv("GOOGLE_REDIRECT_URI")

    # JWT CONFIGURATION
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    TIME_MINUTES: int = int(os.getenv("TIME_MINUTES", "30"))

    BCRYPT_ROUNDS: int = int(os.getenv("BCRYPT_ROUNDS", "12"))

    FIREBASE_CREDENTIALS_PATH = str(CORE_DIR / "golazo-b1c36-firebase-adminsdk-fbsvc-33611d463a.json")
    origins = [
        "*",
        "http://localhost: 5173"
    ]

    LOG_LEVEL: str = "INFO"

settings = Settings()
