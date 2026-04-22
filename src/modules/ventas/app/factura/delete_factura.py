from src.modules.ventas.domain.ports import FacturaPort


class DeleteFactura:
    def __init__(self, repo: FacturaPort):
        self.repo = repo

    def execute(self, factura_id: int) -> bool:
        if not self.repo.delete(factura_id):
            raise ValueError(f"Factura with ID {factura_id} not found or could not be deleted")
        return True
