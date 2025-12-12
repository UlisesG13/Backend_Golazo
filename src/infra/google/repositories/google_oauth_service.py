import requests
from google.oauth2 import id_token
from google.auth.transport import requests as grequests
from urllib.parse import urlencode
from src.core.config import settings

class GoogleOAuthService:
    def build_auth_url(self):
        params = {
            "client_id": settings.GOOGLE_CLIENT_ID,
            "redirect_uri": settings.GOOGLE_REDIRECT_URI,
            "response_type": "code",
            "scope": "openid email profile",
            "access_type": "offline",
            "prompt": "consent"
        }
        return "https://accounts.google.com/o/oauth2/auth?" + urlencode(params)

    def exchange_code(self, code: str):
        url = "https://oauth2.googleapis.com/token"
        data = {
            "code": code,
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri": settings.GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code",
        }
        return requests.post(url, data=data).json()

    def verify_id(self, token_str: str):
        return id_token.verify_oauth2_token(
            token_str,
            grequests.Request(),
            settings.GOOGLE_CLIENT_ID
        )
