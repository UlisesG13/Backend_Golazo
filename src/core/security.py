from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.modules.auth.presentation.dependencies import verify_token_service
from src.modules.auth.domain.models import AuthenticatedUser, TokenPayload
from fastapi import Depends

security = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    usecase=Depends(verify_token_service)
) -> AuthenticatedUser:

    token = credentials.credentials
    payload: TokenPayload = usecase.execute(token)

    return AuthenticatedUser(
        usuario_id=payload.usuario_id,
        email=payload.email,
        rol=payload.rol,
    )
