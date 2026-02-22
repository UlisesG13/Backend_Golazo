from src.modules.usuarios.domain.ports import UserPort

class DeleteUser:
    def __init__(self, repo: UserPort):
        self.user_repository = repo

    def execute(self, usuario_id: str) -> bool:
            if not self.user_repository.get_by_id(usuario_id):
                raise ValueError(f"Usuario con ID {usuario_id} no encontrado")
            self.user_repository.delete(usuario_id)
            return True