from fastapi import Depends
from src.infra.db.database import get_session
from src.infra.db.repositories.producto_talla_repository import ProductoTallaRepository
from src.usecases.producto_talla_usecase import ProductoTallaUsecases

def get_producto_talla_repository(session=Depends(get_session)):
    return ProductoTallaRepository(session)

def get_producto_talla_service(repo=Depends(get_producto_talla_repository)):
    return ProductoTallaUsecases(repo)