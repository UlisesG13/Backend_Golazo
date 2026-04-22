from src.core.messaging.fcm_client import get_messaging


class FCMService:

    @staticmethod
    def send(token: str, title: str, body: str, data: dict | None = None):
        messaging = get_messaging()

        message = messaging.Message(
            token=token,
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            data=data or {},
        )

        return messaging.send(message)