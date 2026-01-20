from fastapi import Depends
from src.infra.db.database import get_session
from src.infra.db.repositories.producto_color_repository import ProductoColorRepository
from src.usecases.producto_color_usecase import ProductoColorUsecases

def get_producto_color_repository(session=Depends(get_session)):
    return ProductoColorRepository(session)

def get_producto_color_service(repo=Depends(get_producto_color_repository)):
    return ProductoColorUsecases(repo)