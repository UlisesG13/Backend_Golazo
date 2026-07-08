from src.modules.usuarios.domain.models import UserModel
from src.modules.usuarios.domain.ports import UserPort

class GetAllAdmins:
    def __init__(self, repo: UserPort):
        self.user_repository = repo

    async def execute(self) -> list[UserModel]:
        return await self.user_repository.get_all_admins()
