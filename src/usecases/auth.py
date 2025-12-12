from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.api.schemas.user_dto import TokenUserDTO
from src.core.security import verificar_token
from jose import JWTError

security = HTTPBearer()

def auth(credentials: HTTPAuthorizationCredentials = Depends(security)): 
    token = credentials .credentials
    try:
        payload = verificar_token(token)
        return TokenUserDTO(**payload)
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")