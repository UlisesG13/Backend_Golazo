from src.shared.domain.ports.messaging_port import MessagingPort
from src.shared.infra.messaging.fcm_service import FCMService

def get_fcm_service() -> MessagingPort:
    return FCMService()
