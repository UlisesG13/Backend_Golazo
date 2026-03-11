from src.core.database import get_session
from fastapi import Depends

# repository
from src.modules.auth.infra.db.repositories.auth_repository import AuthRepository
from src.modules.auth.infra.security.password_service import PasswordService
from src.modules.usuarios.infra.user_repository import UserRepository
from src.modules.auth.infra.jwt.token_service import JwtTokenService

# usecases
from src.modules.usuarios.application.usuario.get_user_by_email import GetUserByEmail
from src.modules.usuarios.application.usuario.anonymize_user import AnonymizeUser
from src.modules.usuarios.application.usuario.get_user_by_id import GetUserById
from src.modules.usuarios.application.usuario.get_all_users import GetAllUsers
from src.modules.usuarios.application.usuario.create_admin import CreateAdmin
from src.modules.usuarios.application.usuario.get_admins import GetAllAdmins
from src.modules.usuarios.application.usuario.delete_user import DeleteUser
from src.modules.usuarios.application.usuario.update_user import UpdateUser

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