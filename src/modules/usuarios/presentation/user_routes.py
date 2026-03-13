from src.modules.usuarios.presentation.user_dependencies import get_user_by_id_service, get_user_by_email_service, anonymize_user_service, delete_user_service, get_all_users_service, update_user_service, register_admin_service, get_all_admins_service
from src.modules.usuarios.application import GetUserById, AnonymizeUser, GetUserByEmail, DeleteUser, GetAllUsers, UpdateUser, CreateAdmin, GetAllAdmins
from src.modules.auth.presentation.schemas import LoginResponseDTO, UserRegister
from src.modules.auth.domain.models import AuthenticatedUser
from src.shared.security import get_current_user
from src.modules.usuarios.presentation.schemas import UserDTO, UserUpdateDTO
from fastapi import APIRouter, Depends
from typing import List

router = APIRouter(prefix="/api/users", tags=["users"])

@router.get("/", response_model=List[UserDTO])
def list_users(uc: GetAllUsers = Depends(get_all_users_service)):
    return uc.execute()

@router.get("/by-id/{usuario_id}", response_model=UserDTO, status_code=200)
def get_user(
    usuario_id: str,
    uc: GetUserById = Depends(get_user_by_id_service),
):
    return uc.execute(usuario_id)

@router.get("/by-email/{email}/", response_model=UserDTO, status_code=200)
def get_user_by_email(
    email: str,
    uc: GetUserByEmail = Depends(get_user_by_email_service),
):
    return uc.execute(email)

@router.delete("/", status_code=204)
def delete_user(
    user: AuthenticatedUser = Depends(get_current_user),
    uc: DeleteUser = Depends(delete_user_service),
):
    return uc.execute(user.usuario_id)

@router.delete("/anonymize", status_code=204)
def anonymize_user(
    user: AuthenticatedUser = Depends(get_current_user),
    uc: AnonymizeUser = Depends(anonymize_user_service),
):
    return uc.execute(user.usuario_id)

@router.get("/profile/", status_code=200, response_model=UserDTO)
def perfil(
    user: AuthenticatedUser = Depends(get_current_user),
    uc: GetUserById = Depends(get_user_by_id_service)
):
    return uc.execute(user.usuario_id)

@router.put("/", response_model=UserDTO)
def update_user(
    user_update: UserUpdateDTO,
    user: AuthenticatedUser = Depends(get_current_user),
    uc: UpdateUser = Depends(update_user_service),
):
    return uc.execute(user.usuario_id, user_update)

@router.post("/admin", response_model=LoginResponseDTO)
def create_admin(
        user: UserRegister,
        uc: CreateAdmin = Depends(register_admin_service),
):
    return uc.execute(user)

@router.get("/admins", response_model=List[UserDTO])
def get_admins(
        uc: GetAllAdmins = Depends(get_all_admins_service)
):
    return uc.execute()