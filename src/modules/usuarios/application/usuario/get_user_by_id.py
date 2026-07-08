from src.modules.usuarios.domain.models import UserModel
from src.modules.usuarios.domain.ports import UserPort
from src.core.exceptions import NotFoundError

class GetUserById:
    def __init__(self, repo: UserPort):
        self.repo = repo

    async def execute(self, usuario_id: str) -> UserModel:
        user = await self.repo.get_by_id(usuario_id)
        if not user:
            raise NotFoundError(f"Usuario con ID {usuario_id} no encontrado")
        return user
