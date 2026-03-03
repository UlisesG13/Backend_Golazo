from src.modules.usuarios.domain.models import DireccionModel
from src.modules.usuarios.domain.ports import DireccionPort

class SetPrimaryDireccion:
    def __init__(self, repo: DireccionPort):
        self.repo = repo

    def execute(self, direccion_id: int, usuario_id: str) -> None:
        direccion = self.repo.get_direccion_by_id(direccion_id, usuario_id)
        if not direccion:
            return None
        return self.repo.set_primary(direccion_id, usuario_id)