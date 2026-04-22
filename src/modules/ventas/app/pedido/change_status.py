from datetime import datetime

from src.modules.ventas.domain import PedidoPort


class ChangePedidoStatus:

    VALID_STATUS = {"pendiente", "procesando", "camino", "completado", "cancelado"}

    def __init__(self, repo: PedidoPort):
        self.repo = repo

    def execute(self, pedido_id: int, status: str) -> None:

        if status not in self.VALID_STATUS:
            raise ValueError("Estado inválido")
        self.repo.update_status(pedido_id, status, datetime.now())