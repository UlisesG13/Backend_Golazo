from src.modules.ventas.domain import PedidoPort, PedidoModel


class GetPedidoById:

    def __init__(self, repo: PedidoPort):
        self.repo = repo

    def execute(self, pedido_id: int) -> PedidoModel:
        pedido = self.repo.get_by_id(pedido_id)

        if not pedido:
            raise ValueError("Pedido no encontrado")

        return pedido
