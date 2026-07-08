from src.modules.usuarios.domain.models import UserModel
from src.modules.usuarios.domain.ports import UserPort
from src.core.exceptions import NotFoundError

class GetUserByEmail:
    def __init__(self, repo: UserPort):
        self.user_repository = repo
    
    async def execute(self, email: str) -> UserModel:
        user = await self.user_repository.get_by_email(email)
        if not user:
            raise NotFoundError(f"Usuario con email {email} no encontrado")
        return user
