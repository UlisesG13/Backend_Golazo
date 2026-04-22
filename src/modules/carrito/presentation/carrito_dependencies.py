from fastapi import Depends

from src.core.database import get_session
from src.modules.carrito.app import GetCartUseCase, AddItemUseCase, RemoveItemUseCase, RemoveCartUseCase, UpdateQuantityUseCase
from src.modules.carrito.infra.carrito_repository import CarritoRepository
from src.modules.catalogo.infra.products.product_repository import ProductoRepository


def get_cart(session=Depends(get_session)):
    repo = CarritoRepository(session)
    return GetCartUseCase(repo)

def add_item(session=Depends(get_session)):
    repo = CarritoRepository(session)
    p_repo = ProductoRepository(session)
    return AddItemUseCase(repo, p_repo)

def delete_item(session=Depends(get_session)):
    repo = CarritoRepository(session)
    return  RemoveItemUseCase(repo)

def delete_cart(session=Depends(get_session)):
    repo = CarritoRepository(session)
    return RemoveCartUseCase(repo)

def update_quantity(session=Depends(get_session)):
    repo = CarritoRepository(session)
    return UpdateQuantityUseCase(repo)