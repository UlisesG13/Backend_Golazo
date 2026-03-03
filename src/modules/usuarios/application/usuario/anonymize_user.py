from src.modules.usuarios.domain.ports import UserPort

class AnonymizeUser:
    def __init__(self, repo: UserPort):
        self.repo = repo

    def execute(self, usuario_id: str) -> bool:
        user = self.repo.get_by_id(usuario_id)
        if not user:
            raise ValueError("Usuario no encontrado")
        self.repo.anonymize_and_soft_delete(usuario_id)
        return True