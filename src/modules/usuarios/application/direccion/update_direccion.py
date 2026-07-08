from src.modules.usuarios.presentation.schemas import DireccionRequestDTO
from src.modules.usuarios.domain.models import DireccionModel
from src.modules.usuarios.domain.ports import DireccionPort
from src.core.exceptions import NotFoundError

class UpdateDireccion:
    def __init__(self, repo: DireccionPort):
        self.repo = repo

    async def execute(self, direccion_id: int, data: DireccionRequestDTO, usuario_id: str) -> DireccionModel:
        existing = await self.repo.get_direccion_by_id(direccion_id, usuario_id)
        if not existing:
            raise NotFoundError(f"Dirección con ID {direccion_id} no encontrada")
        updated = DireccionModel(
            direccion_id=existing.direccion_id,
            calle=data.calle if data.calle is not None else existing.calle,
            calle_uno=data.calle_uno if data.calle_uno is not None else existing.calle_uno,
            calle_dos=data.calle_dos if data.calle_dos is not None else existing.calle_dos,
            usuario_id=existing.usuario_id,
            colonia=data.colonia if data.colonia is not None else existing.colonia,
            numero_casa=data.numero_casa if data.numero_casa is not None else existing.numero_casa,
            codigo_postal=data.codigo_postal if data.codigo_postal is not None else existing.codigo_postal,
            referencia=data.referencia if data.referencia is not None else existing.referencia,
            is_primary=data.is_primary if data.is_primary is not None else existing.is_primary,
        )
        return await self.repo.update_direccion(direccion_id, updated, usuario_id)
