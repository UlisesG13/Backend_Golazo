from fastapi import Depends
from src.infra.db.database import get_session
from src.infra.db.repositories.direccion_repository import DireccionRepository
from src.usecases.direccion_usecase import DireccionUsecases

def get_direccion_repository(session=Depends(get_session)):
    return DireccionRepository(session)

def get_direccion_service(repo=Depends(get_direccion_repository)):
    return DireccionUsecases(repo)
