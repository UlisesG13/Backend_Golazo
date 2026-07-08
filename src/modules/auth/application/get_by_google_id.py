from src.modules.auth.domain.ports import AuthPort
from src.modules.auth.domain.models import AuthUser
from src.core.exceptions import NotFoundError

class GetByGoogle:

    def __init__(
        self,
        auth_repo: AuthPort
    ):
        self.auth_repo = auth_repo

    async def execute(self, uid: str) -> AuthUser:
        user = await self.auth_repo.get_by_google_id(uid)
        if not user:
            raise NotFoundError("Usuario no encontrado") # obteniendo el error en `user_routes.py` procedera a crear el usuario
        return user
