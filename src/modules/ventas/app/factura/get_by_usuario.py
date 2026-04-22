from src.modules.ventas.domain import FacturaPort, FacturaModel


class GetByUsuario:
    def __init__(self, repo: FacturaPort):
        self.repo = repo

    def execute(self, usuario_id: str) -> list[FacturaModel]:
        return self.repo.get_by_usuario_id(usuario_id)