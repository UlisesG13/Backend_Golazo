from src.modules.ventas.domain import PedidoPort, PedidoModel


class GetPedidosByUser:

    def __init__(self, repo: PedidoPort):
        self.repo = repo

    def execute(self, usuario_id: str) -> list[PedidoModel]:
        return self.repo.get_by_user_id(usuario_id)