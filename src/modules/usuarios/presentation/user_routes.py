from fastapi import APIRouter, Depends, status

from src.modules.auth.domain.models import AuthenticatedUser
from src.modules.auth.presentation.schemas import LoginResponseDTO, UserRegister
from src.modules.usuarios.application import RegisterDeviceToken, GetUserById, AnonymizeUser, GetUserByEmail, \
    DeleteUser, GetAllUsers, UpdateUser, CreateAdmin, GetAllAdmins
from src.modules.usuarios.presentation.schemas import UserDTO, UserUpdateDTO
from src.modules.usuarios.presentation.user_dependencies import get_user_by_id_service, get_user_by_email_service, \
    anonymize_user_service, delete_user_service, get_all_users_service, update_user_service, register_admin_service, \
    get_all_admins_service, register_token_service
from src.core.security import get_current_user

router = APIRouter()


# Estas rutas usan 'get_current_user' y no necesitan IDs en la URL
@router.get("/profile", response_model=UserDTO)
async def perfil(
        user: AuthenticatedUser = Depends(get_current_user),
        uc: GetUserById = Depends(get_user_by_id_service)
):
    return await uc.execute(user.usuario_id)


@router.put("", response_model=UserDTO)
async def update_user(
        user_update: UserUpdateDTO,
        user: AuthenticatedUser = Depends(get_current_user),
        uc: UpdateUser = Depends(update_user_service),
):
    return await uc.execute(user.usuario_id, user_update)


@router.delete("", status_code=204)
async def delete_user(
        user: AuthenticatedUser = Depends(get_current_user),
        uc: DeleteUser = Depends(delete_user_service),
):
    return await uc.execute(user.usuario_id)


@router.delete("/anonymize", status_code=204)
async def anonymize_user(
        user: AuthenticatedUser = Depends(get_current_user),
        uc: AnonymizeUser = Depends(anonymize_user_service),
):
    return await uc.execute(user.usuario_id)


# Usamos prefijos específicos para que no choquen con las rutas de raíz
@router.get("", response_model=list[UserDTO])
async def list_users(uc: GetAllUsers = Depends(get_all_users_service)):
    return await uc.execute()


@router.get("/by-id/{usuario_id}", response_model=UserDTO)
async def get_user(usuario_id: str, uc: GetUserById = Depends(get_user_by_id_service)):
    return await uc.execute(usuario_id)


@router.get("/by-email/{email}", response_model=UserDTO)
async def get_user_by_email(email: str, uc: GetUserByEmail = Depends(get_user_by_email_service)):
    return await uc.execute(email)


# --- GESTIÓN DE ADMINISTRADORES ---
@router.get("/admins", response_model=list[UserDTO])
async def get_admins(uc: GetAllAdmins = Depends(get_all_admins_service)):
    return await uc.execute()


@router.post("/admins", response_model=LoginResponseDTO, status_code=status.HTTP_201_CREATED)
async def create_admin(user: UserRegister, uc: CreateAdmin = Depends(register_admin_service)):
    return await uc.execute(user)


@router.put("/admins/{usuario_id}", response_model=UserDTO)
async def update_admin(usuario_id: str, user_update: UserUpdateDTO, uc: UpdateUser = Depends(update_user_service)):
    return await uc.execute(usuario_id, user_update)


@router.delete("/admins/{usuario_id}", status_code=204)
async def delete_admin(usuario_id: str, uc: DeleteUser = Depends(delete_user_service)):
    return await uc.execute(usuario_id)


@router.post("/device-token", status_code=status.HTTP_201_CREATED)
async def register_token(
        token: str,
        user : AuthenticatedUser=Depends(get_current_user),
        usecase: RegisterDeviceToken = Depends(register_token_service)
):
    await usecase.execute(user.usuario_id, token)
    return {"ok": True}
