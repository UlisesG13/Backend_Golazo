from src.modules.usuarios.domain.ports import UserPort
from src.core.exceptions import NotFoundError

class AnonymizeUser:
    def __init__(self, repo: UserPort):
        self.repo = repo

    async def execute(self, usuario_id: str) -> bool:
        user = await self.repo.get_by_id(usuario_id)
        if not user:
            raise NotFoundError("Usuario no encontrado")
        await self.repo.anonymize_and_soft_delete(usuario_id)
        return True
