from src.modules.ventas.domain import PedidoPort, PedidoModel
from src.modules.ventas.infra.pedido.pedido_table import EstadoPedido


class GetPedidos:

    def __init__(self, repo: PedidoPort):
        self.repo = repo

    async def execute(self, status: EstadoPedido | None) -> list[PedidoModel]:
        if status is None:
            return await self.repo.get_all()
        else:
            return await self.repo.get_by_status(status.value)
