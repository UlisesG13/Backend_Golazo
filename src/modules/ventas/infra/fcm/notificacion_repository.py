from src.core.messaging.fcm_service import FCMService
from src.modules.ventas.domain.ports import NotificationPort

class FCMNotificationRepository(NotificationPort):
    def __init__(self):
        self.fcm = FCMService()

    def send_new_promocion(self, token: str, codigo: str, descuento: str):
        self.fcm.send_new_promocion(token, codigo, descuento)
