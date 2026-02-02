from fastapi import Depends
from src.infra.db.database import get_session
from src.infra.db.repositories.carrito_item_repository import CarritoItemRepository
from src.usecases.carrito_item_usecase import CarritoItemUseCases

def get_carrito_item_repository(session=Depends(get_session)):
    return CarritoItemRepository(session)

def get_carrito_item_service(repo=Depends(get_carrito_item_repository)):
    from src.usecases.carrito_item_usecase import CarritoItemUseCases
    return CarritoItemUseCases(repo)