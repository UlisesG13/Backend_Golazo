from src.modules.usuarios.domain.models import DireccionModel
from src.modules.usuarios.domain.ports import DireccionPort


class GetAllDirecciones:
    def __init__(self, repo: DireccionPort) -> None:
        self.repo = repo

    def execute(self, usuario_id: str) -> list[DireccionModel]:
        return self.repo.get_direcciones_by_usuario_id(usuario_id)