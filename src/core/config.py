import os
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SUPABASE_URL: str = os.getenv("SUPABASE_URL")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")
    MAIL_USERNAME: str = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD: str = os.getenv("MAIL_PASSWORD")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    TIME_MINUTES: int = int(os.getenv("TIME_MINUTES", "30"))
    GOOGLE_CLIENT_ID = str = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = str = os.getenv("GOOGLE_CLIENT_SECRET")
    GOOGLE_REDIRECT_URI = str = os.getenv("GOOGLE_REDIRECT_URI")
settings = Settings()

app = FastAPI(
    title="Golazo",
    description="Backend del e-commerce Golazo",
    version="1.0.5"
)
origins = [
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)
