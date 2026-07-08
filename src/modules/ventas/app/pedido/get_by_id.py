from src.core.exceptions import NotFoundError
from src.modules.ventas.domain import PedidoPort, PedidoModel


class GetPedidoById:

    def __init__(self, repo: PedidoPort):
        self.repo = repo

    async def execute(self, pedido_id: int) -> PedidoModel:
        pedido = await self.repo.get_by_id(pedido_id)

        if not pedido:
            raise NotFoundError("Pedido no encontrado")

        return pedido
