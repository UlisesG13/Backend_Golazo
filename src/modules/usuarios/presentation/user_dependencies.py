from fastapi import Depends

from src.core.database import get_session
# repository
from src.modules.auth.infra.db.repositories.auth_repository import AuthRepository
from src.modules.auth.infra.jwt.token_service import JwtTokenService
from src.modules.auth.infra.security.password_service import PasswordService
# usecases
from src.modules.usuarios.application.usuario import GetUserByEmail, AnonymizeUser, GetUserById, GetAllUsers, \
    CreateAdmin, GetAllAdmins, DeleteUser, UpdateUser, RegisterDeviceToken
from src.modules.usuarios.infra.fcm_repository import DeviceTokenRepository
from src.modules.usuarios.infra.user_repository import UserRepository


def anonymize_user_service(session=Depends(get_session)):
    repo = UserRepository(session)
    return AnonymizeUser(repo)


def get_user_by_email_service(session=Depends(get_session)):
    repo = UserRepository(session)
    return GetUserByEmail(repo)


def get_user_by_id_service(session=Depends(get_session)):
    repo = UserRepository(session)
    return GetUserById(repo)


def delete_user_service(session=Depends(get_session)):
    repo = UserRepository(session)
    return DeleteUser(repo)


def get_all_users_service(session=Depends(get_session)):
    repo = UserRepository(session)
    return GetAllUsers(repo)


def update_user_service(session=Depends(get_session)):
    repo = UserRepository(session)
    return UpdateUser(repo)


def register_admin_service(session=Depends(get_session)):
    repo = AuthRepository(session)
    password_service = PasswordService()
    token_service = JwtTokenService()
    return CreateAdmin(repo, password_service, token_service)


def get_all_admins_service(session=Depends(get_session)):
    repo = UserRepository(session)
    return GetAllAdmins(repo)


def register_token_service(session=Depends(get_session)):
    repo = DeviceTokenRepository(session)
    return RegisterDeviceToken(repo)
