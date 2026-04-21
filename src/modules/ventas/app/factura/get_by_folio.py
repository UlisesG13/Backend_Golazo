from src.modules.ventas.domain import FacturaPort, FacturaModel


class GetByFolio:
    def __init__(self, repo: FacturaPort):
        self.repo = repo

    def execute(self, folio: str) -> FacturaModel | None:
        factura = self.repo.get_by_folio(folio)
        if not factura:
            raise ValueError(f"Factura {folio} not found")
        return factura
