from datetime import datetime

from src.core.exceptions import BadRequestError
from src.modules.ventas.domain import PedidoPort


class ChangePedidoStatus:

    VALID_STATUS = {"pendiente", "procesando", "camino", "completado", "cancelado"}

    def __init__(self, repo: PedidoPort):
        self.repo = repo

    async def execute(self, pedido_id: int, status: str) -> None:

        if status not in self.VALID_STATUS:
            raise BadRequestError("Estado inválido")
        await self.repo.update_status(pedido_id, status, datetime.now())
