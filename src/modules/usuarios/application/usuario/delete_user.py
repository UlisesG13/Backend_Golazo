from src.modules.usuarios.domain.ports import UserPort
from src.core.exceptions import NotFoundError

class DeleteUser:
    def __init__(self, repo: UserPort):
        self.user_repository = repo

    async def execute(self, usuario_id: str) -> bool:
            if not await self.user_repository.get_by_id(usuario_id):
                raise NotFoundError(f"Usuario con ID {usuario_id} no encontrado")
            await self.user_repository.delete(usuario_id)
            return True
