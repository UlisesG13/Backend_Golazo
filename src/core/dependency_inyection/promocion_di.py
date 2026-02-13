from fastapi import Depends
from src.infra.db.database import get_session
from src.infra.db.repositories.promocion_repository import PromocionRepository
from src.usecases.promocion_usecase import PromocionUsecases

def get_promocion_repository(session=Depends(get_session)):
    return PromocionRepository(session)

def get_promocion_service(repo=Depends(get_promocion_repository)):
    return PromocionUsecases(repo)
