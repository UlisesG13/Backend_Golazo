from src.core.exceptions import NotFoundError, BadRequestError
from src.modules.ventas.domain.models import EstadoFactura, FacturaModel
from src.modules.ventas.domain.ports import FacturaPort


class ChangeStatus:
    def __init__(self, repo: FacturaPort):
        self.repo = repo

    async def execute(self, factura_id: int, status: EstadoFactura) -> FacturaModel:
        # 1. Obtener la factura
        factura = await self.repo.get_by_id(factura_id)
        if not factura:
            raise NotFoundError(f"Factura with ID {factura_id} not found")

        # 2. Actualizar el estado
        factura.estado = status

        # 3. Persistir (utilizando el méthodo update del port)
        updated = await self.repo.update(factura_id, factura)
        if not updated:
            raise BadRequestError(f"Could not update status for factura {factura_id}")
            
        return updated
