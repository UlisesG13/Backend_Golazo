from src.core.exceptions import NotFoundError
from src.modules.ventas.domain import FacturaModel, FacturaPort


class GetById:
    def __init__(self, repo: FacturaPort):
        self.repo = repo

    async def execute(self, factura_id: int) -> FacturaModel | None:
        factura = await self.repo.get_by_id(factura_id)
        if not factura:
            raise NotFoundError(f"Factura {factura_id} not found")
        return factura
