from fastapi import Depends
from src.infra.db.database import get_session
from src.infra.db.repositories.talla_repository import TallaRepository
from src.usecases.talla_usecase import TallaUsecases

def get_talla_repository(session=Depends(get_session)):
    return TallaRepository(session)

def get_talla_service(repo=Depends(get_talla_repository)):
    return TallaUsecases(repo)