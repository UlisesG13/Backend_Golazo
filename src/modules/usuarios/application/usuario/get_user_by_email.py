from src.modules.usuarios.domain.models import UserModel
from src.modules.usuarios.domain.ports import UserPort

class GetUserByEmail:
    def __init__(self, repo: UserPort):
        self.user_repository = repo
    
    def execute(self, email: str) -> UserModel:
        user = self.user_repository.get_by_email(email)
        if not user:
            raise ValueError(f"Usuario con email {email} no encontrado")
        return user