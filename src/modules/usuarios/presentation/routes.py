from src.modules.usuarios.application.container import build_get_user_by_id_service, build_get_user_by_email_service, anonymize_user_service, build_delete_user_service, build_get_all_users_service, build_update_user_service
from src.modules.usuarios.application import GetUserById, AnonymizeUser, GetUserByEmail, DeleteUser, GetAllUsers, UpdateUser
from src.modules.auth.domain.models import AuthenticatedUser
from src.shared.security import get_current_user
from src.api.schemas.user_dto import UserDTO, UserUpdateDTO
from fastapi import APIRouter, Depends
from typing import List

router = APIRouter(prefix="/api/users", tags=["users"])

@router.get("/", response_model=List[UserDTO])
def list_users(uc: GetAllUsers = Depends(build_get_all_users_service)):
    return uc.execute()

@router.get("/by-id/{usuario_id}", response_model=UserDTO, status_code=200)
def get_user(
    usuario_id: str,
    uc: GetUserById = Depends(build_get_user_by_id_service),
):
    return uc.execute(usuario_id)

@router.get("/by-email/{email}/", response_model=UserDTO, status_code=200)
def get_user_by_email(
    email: str,
    uc: GetUserByEmail = Depends(build_get_user_by_email_service),
):
    return uc.execute(email)

@router.delete("/", status_code=204)
def delete_user(
    user: AuthenticatedUser = Depends(get_current_user),
    uc: DeleteUser = Depends(build_delete_user_service),
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
    uc: GetUserById = Depends(build_get_user_by_id_service)
):
    return uc.execute(user.usuario_id)

@router.put("/", response_model=UserDTO)
def update_user(
    user_update: UserUpdateDTO,
    user: AuthenticatedUser = Depends(get_current_user),
    uc: UpdateUser = Depends(build_update_user_service),
):
    return uc.execute(user.usuario_id, user_update)