from src.modules.ventas.domain.ports import NotificationPort
from src.shared.domain.ports.messaging_port import MessagingPort


class FCMNotificationRepository(NotificationPort):
    def __init__(self, messaging_service: MessagingPort):
        self.fcm = messaging_service

    def send_new_promocion(self, token: str, codigo: str, descuento: str):
        self.fcm.send(
            token=token,
            title="Nueva Promoción",
            body=f"Usa el código {codigo} y obtén un {descuento}% de descuento",
            data={
                "type": "NEW_PROMO",
                "codigo": codigo,
                "descuento": descuento
            }
        )
