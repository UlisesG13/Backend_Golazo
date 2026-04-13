from src.modules.usuarios.domain.ports import DeviceTokenPort


class RegisterDeviceToken:
    def __init__(self, repo: DeviceTokenPort):
        self.repo = repo

    def execute(self, user_id: str, token: str):
        self.repo.save(user_id, token)
