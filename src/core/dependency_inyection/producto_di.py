from fastapi import Depends
from src.infra.db.database import get_session
from src.infra.db.repositories.producto_repository import ProductoRepository
from src.usecases.producto_usecase import ProductoUsecases

def get_producto_repository(session=Depends(get_session)):
    return ProductoRepository(session)

def get_producto_service(repo=Depends(get_producto_repository)):
    return ProductoUsecases(repo)
