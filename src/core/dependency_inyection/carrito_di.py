from fastapi import Depends
from src.infra.db.database import get_session
from src.infra.db.repositories.carrito_repository import CarritoRepository
from src.usecases.carrito_usecase import CarritoUseCases


def get_carrito_repository(session=Depends(get_session)):
    return CarritoRepository(session)

def get_carrito_service(repo=Depends(get_carrito_repository)):
    return CarritoUseCases(repo)
