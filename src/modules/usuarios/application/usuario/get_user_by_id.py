from src.modules.usuarios.domain.models import UserModel
from src.modules.usuarios.domain.ports import UserPort

class GetUserById:
    def __init__(self, repo: UserPort):
        self.repo = repo

    def execute(self, usuario_id: str) -> UserModel:
        user = self.repo.get_by_id(usuario_id)
        if not user:
            raise ValueError(f"Usuario con ID {usuario_id} no encontrado")
        return user