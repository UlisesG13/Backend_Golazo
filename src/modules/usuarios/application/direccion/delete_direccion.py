from src.modules.usuarios.domain.ports import DireccionPort
from src.core.exceptions import NotFoundError

class DeleteDireccion:
    def __init__(self, repo: DireccionPort) -> None:
        self.repo = repo

    async def execute(self, direccion_id: int, usuario_id: str) -> None:
        direccion = await self.repo.get_direccion_by_id(direccion_id, usuario_id)
        if not direccion:
            raise NotFoundError(f"Dirección con ID {direccion_id} no encontrada")
        return await self.repo.delete_direccion(direccion_id, usuario_id)
