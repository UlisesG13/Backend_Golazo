import firebase_admin
from firebase_admin import credentials, messaging
from src.core.config import settings

def init_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
        firebase_admin.initialize_app(cred)

def get_messaging():
    init_firebase()
    return messaging
