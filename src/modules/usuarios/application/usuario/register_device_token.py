from src.modules.usuarios.domain.ports import DeviceTokenPort


class RegisterDeviceToken:
    def __init__(self, repo: DeviceTokenPort):
        self.repo = repo

    async def execute(self, user_id: str, token: str):
        await self.repo.save(user_id, token)
