from src.modules.ventas.domain import FacturaModel, FacturaPort


class GetById:
    def __init__(self, repo: FacturaPort):
        self.repo = repo

    def execute(self, factura_id: int) -> FacturaModel | None:
        factura = self.repo.get_by_id(factura_id)
        if not factura:
            raise ValueError(f"Factura {factura_id} not found")
        return factura
