from src.core.database import get_session
from fastapi import Depends

# repository
from src.modules.usuarios.infra.repositories import UserRepository

# usecases
from src.modules.usuarios.application.get_user_by_email import GetUserByEmail
from src.modules.usuarios.application.anonymize_user import AnonymizeUser
from src.modules.usuarios.application.get_user_by_id import GetUserById
from src.modules.usuarios.application.get_all_users import GetAllUsers
from src.modules.usuarios.application.delete_user import DeleteUser
from src.modules.usuarios.application.update_user import UpdateUser

def anonymize_user_service(session=Depends(get_session)):
    repo = UserRepository(session)
    return AnonymizeUser(repo)

def build_get_user_by_email_service(session=Depends(get_session)):
    repo = UserRepository(session)
    return GetUserByEmail(repo)

def build_get_user_by_id_service(session=Depends(get_session)):
    repo = UserRepository(session)
    return GetUserById(repo)

def build_delete_user_service(session=Depends(get_session)):
    repo = UserRepository(session)
    return DeleteUser(repo)

def build_get_all_users_service(session=Depends(get_session)):
    repo = UserRepository(session)
    return GetAllUsers(repo)

def build_update_user_service(session=Depends(get_session)):
    repo = UserRepository(session)
    return UpdateUser(repo)