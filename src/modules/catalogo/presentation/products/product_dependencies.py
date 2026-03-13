from src.core.database import get_session
from fastapi import Depends

from src.modules.catalogo.infra.products.product_repository import ProductoRepository

from src.modules.catalogo.app.products import (
ListProducts,
GetProductoById,
GetProductoByCategoria,
CreateProducto,
DeleteProducto,
UpdateProducto,
ChangeStatus,
ChangeDestacado,
)

def get_all_productos_service(session = Depends(get_session)):
    repo = ProductoRepository(session)
    return ListProducts(repo)

def get_product_by_id_service(session = Depends(get_session)):
    repo = ProductoRepository(session)
    return GetProductoById(repo)

def get_producto_by_categoria_service(session = Depends(get_session)):
    repo = ProductoRepository(session)
    return GetProductoByCategoria(repo)

def create_producto_service(session = Depends(get_session)):
    repo = ProductoRepository(session)
    return CreateProducto(repo)

def delete_producto_service(session = Depends(get_session)):
    repo = ProductoRepository(session)
    return DeleteProducto(repo)

def update_producto_service(session = Depends(get_session)):
    repo = ProductoRepository(session)
    return UpdateProducto(repo)

def change_status_service(session = Depends(get_session)):
    repo = ProductoRepository(session)
    return ChangeStatus(repo)

def change_destacado_service(session = Depends(get_session)):
    repo = ProductoRepository(session)
    return ChangeDestacado(repo)