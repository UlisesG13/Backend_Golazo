from fastapi import Depends
from src.infra.db.database import get_session
from src.infra.db.repositories.seccion_repository import SeccionRepository
from src.usecases.seccion_usecase import SeccionUsecases

def get_seccion_repository(session=Depends(get_session)):
    return SeccionRepository(session)

def get_seccion_service(repo=Depends(get_seccion_repository)):
    return SeccionUsecases(repo)
