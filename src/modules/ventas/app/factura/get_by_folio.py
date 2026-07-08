from src.core.exceptions import NotFoundError
from src.modules.ventas.domain import FacturaPort, FacturaModel


class GetByFolio:
    def __init__(self, repo: FacturaPort):
        self.repo = repo

    async def execute(self, folio: str) -> FacturaModel | None:
        factura = await self.repo.get_by_folio(folio)
        if not factura:
            raise NotFoundError(f"Factura {folio} not found")
        return factura
