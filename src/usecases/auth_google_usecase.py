from fastapi import Depends
from src.core.security import crear_token
from src.core.dependency_inyection.user_di import get_user_service
from src.usecases.user_usecase import UserUsecases

class AuthGoogleUseCase:
    def __init__(self, user_usecase: UserUsecases = Depends(get_user_service)):
        self.user_usecase = user_usecase

    def execute(self, user_info):
            uid = user_info["sub"]
            email = user_info.get("email")
            nombre = user_info.get("name") or user_info.get("given_name", "")

            user = self.user_usecase.get_by_google_id(uid, email, nombre)

            payload = {
                "usuario_id": user.usuario_id,
                "email": user.email,
                "rol": user.rol,
                "nombre": user.nombre,
                "sub": user.usuario_id
            }

            token = crear_token(payload)
            return token