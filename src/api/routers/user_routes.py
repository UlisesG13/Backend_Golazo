from fastapi import APIRouter, Depends
from typing import List
from src.core.security import crear_token
from src.usecases.user_usecase import UserUsecases
from src.core.dependency_inyection.user_di import get_user_service
from src.api.schemas.user_dto import TokenUserDTO, UserDTO, UserUpdateDTO, UserCreateDTO, UserLoginDTO, LoginResponseDTO
from src.usecases.auth import auth

router = APIRouter(prefix="/api/users", tags=["users"])

@router.get("/", response_model=List[UserDTO])
def list_users(uc: UserUsecases = Depends(get_user_service)):
    return uc.list_users()

@router.get("/by-id/", response_model=UserDTO)
def get_user(
    user = Depends(auth),
    uc: UserUsecases = Depends(get_user_service),
):
    return uc.get_user_by_id(user.usuario_id)

@router.get("/by-email/{email}/", response_model=UserDTO)
def get_user_by_email(
    email: str,
    uc: UserUsecases = Depends(get_user_service),
):
    return uc.get_user_by_email(email)

@router.post("/auth/login/", response_model=LoginResponseDTO)
def login(usuario: UserLoginDTO, uc: UserUsecases = Depends(get_user_service)):
    user = uc.login(usuario)
    dto = TokenUserDTO(
        usuario_id=user.usuario_id,
        email=user.email,
        rol=user.rol
    )
    token = crear_token(dto.model_dump())
    return LoginResponseDTO(
            token=token,
            usuario_id=user.usuario_id,
            email=user.email,
            rol=user.rol
        )
@router.post("/", response_model=UserDTO)
def create_user(user: UserCreateDTO, uc: UserUsecases = Depends(get_user_service)):
    return uc.create_user(user)

@router.post("/auth/request-code/")
def request_code(email: str, uc: UserUsecases = Depends(get_user_service)):
    user = uc.get_user_by_email(email)
    code = uc.generate_code(user.usuario_id)
    return uc.send_recovery_email(email, code)

@router.post("/auth/verify-code/")
def verify_code(user_id: str, code: str, uc: UserUsecases = Depends(get_user_service)):
    return uc.is_code_valid(user_id, code)

@router.delete("/", status_code=204)
def delete_user(
    user = Depends(auth),
    uc: UserUsecases = Depends(get_user_service),
):
    return uc.delete_user(user.usuario_id)

@router.post("/auth/authenticate/", response_model=UserDTO)
def authenticate_user(usuario_id: str, code: str, uc: UserUsecases = Depends(get_user_service)):
    return uc.authenticate_user(usuario_id, code)

@router.get("/profile/")
def perfil(user = Depends(auth)):
    return user

@router.put("/", response_model=UserDTO)
def update_user(
    user_update: UserUpdateDTO,
    user = Depends(auth),
    uc: UserUsecases = Depends(get_user_service),
):
    return uc.update_user(user.usuario_id, user_update)