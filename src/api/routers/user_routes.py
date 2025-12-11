from fastapi import APIRouter, Depends
from typing import List
from src.usecases.user_usecase import UserUsecases
from src.core.dependency_inyection.user_di import get_user_service
from src.api.schemas.user_dto import UserDTO, UserUpdateDTO, UserCreateDTO, UserLoginDTO

router = APIRouter(prefix="/api/users", tags=["users"])

@router.get("/", response_model=List[UserDTO])
def list_users(uc: UserUsecases = Depends(get_user_service)):
    return uc.list_users()

@router.get("/{usuario_id}", response_model=UserDTO)
def get_user(usuario_id: str, uc: UserUsecases = Depends(get_user_service)):
    return uc.get_user_by_id(usuario_id)

@router.get("/{email}/", response_model=UserDTO)
def get_user_by_email(email: str, uc: UserUsecases = Depends(get_user_service)):
    return uc.get_user_by_email(email)

@router.post("/auth/login/", response_model=UserDTO)
def login(user_login: UserLoginDTO, uc: UserUsecases = Depends(get_user_service)):
    return uc.login(user_login)

@router.post("/", response_model=UserDTO)
def create_user(user: UserCreateDTO, uc: UserUsecases = Depends(get_user_service)):
    return uc.create_user(user)

@router.post("/auth/request-code/")
def request_password_reset_code(email: str, uc: UserUsecases = Depends(get_user_service)):
    user = uc.get_user_by_email(email)
    code = uc.generate_code(user.usuario_id)
    return uc.send_recovery_email(email, code)

@router.post("/auth/verify-code/")
def verify_code(user_id: str, code: str, uc: UserUsecases = Depends(get_user_service)):
    return uc.is_code_valid(user_id, code)