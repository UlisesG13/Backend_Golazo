from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.modules.auth.presentation.dependencies import verify_token_service
from src.modules.auth.domain.models import AuthenticatedUser
from fastapi import Depends, HTTPException
from jose import JWTError

security = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    usecase=Depends(verify_token_service)
) -> AuthenticatedUser:

    token = credentials.credentials

    try:
        payload = await usecase.execute(token)

        return AuthenticatedUser(
            usuario_id=payload.usuario_id,
            email= payload.email,
            rol=payload.rol
        )

    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
