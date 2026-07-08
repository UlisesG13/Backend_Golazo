from src.core.exceptions import NotFoundError
from src.modules.ventas.domain import PromocionModel, PromocionPort


class ChangeStatus:
    def __init__(self, repo: PromocionPort):
        self.repo = repo

    async def execute(self,promocion_id: int, status: bool) -> PromocionModel | None:
        current = await self.repo.get_by_id(promocion_id)
        if not current:
            raise NotFoundError(f"Promocion {promocion_id} no existe")
        current.esta_activa = status
        return current
