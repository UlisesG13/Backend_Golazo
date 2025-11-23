from fastapi import Depends
from src.infra.db.database import get_session
from src.infra.db.repositories.user_repository import UserRepository
from src.usecases.user_usecase import UserUsecases

def get_user_repository(session=Depends(get_session)):
    return UserRepository(session)

def get_user_service(repo=Depends(get_user_repository)):
    return UserUsecases(repo)
