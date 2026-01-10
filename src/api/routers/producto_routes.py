from fastapi import APIRouter, Depends
from typing import List
from src.usecases.producto_usecase import ProductoUsecases
from src.core.dependency_inyection.producto_di import get_producto_service
from src.api.schemas.producto_dto import ProductoDTO, ProductoCreateDTO, ProductoUpdateDTO

router = APIRouter(prefix="/api/productos", tags=["productos"])

@router.get("/", response_model=List[ProductoDTO])
def list_productos(uc: ProductoUsecases = Depends(get_producto_service)):
    return uc.list_productos()

@router.get("/{producto_id}/", response_model=ProductoDTO)
def get_producto_by_id(producto_id: str, uc: ProductoUsecases = Depends(get_producto_service)):
    return uc.get_producto_by_id(producto_id)

@router.get("/by-categoria/{categoria_id}/", response_model=List[ProductoDTO])
def get_productos_by_categoria(categoria_id: int, uc: ProductoUsecases = Depends(get_producto_service)):
    return uc.get_productos_by_categoria(categoria_id)

@router.post("/", response_model=ProductoDTO)
def create_producto(dto: ProductoCreateDTO, uc: ProductoUsecases = Depends(get_producto_service)):
    return uc.create_producto(dto)

@router.put("/{producto_id}/", response_model=ProductoDTO)
def update_producto(producto_id: str, dto: ProductoUpdateDTO, uc: ProductoUsecases = Depends(get_producto_service)):
    return uc.update_producto(producto_id, dto)

@router.delete("/{producto_id}/", status_code=204)
def delete_producto(producto_id: str, uc: ProductoUsecases = Depends(get_producto_service)):
    uc.delete_producto(producto_id)

@router.post("/{producto_id}/destacar/", response_model=ProductoDTO)
def mark_producto_as_destacado(producto_id: str, uc: ProductoUsecases = Depends(get_producto_service)):
    return uc.mark_producto_as_destacado(producto_id)

@router.post("/{producto_id}/quitar_destacado/", response_model=ProductoDTO)
def unmark_producto_as_destacado(producto_id: str, uc: ProductoUsecases = Depends(get_producto_service)):
    return uc.unmark_producto_as_destacado(producto_id)

@router.post("/{producto_id}/activar/", response_model=ProductoDTO)
def activar_producto(producto_id: str, uc: ProductoUsecases = Depends(get_producto_service)):
    return uc.activar_producto(producto_id)

@router.post("/{producto_id}/desactivar/", response_model=ProductoDTO)
def desactivar_producto(producto_id: str, uc: ProductoUsecases = Depends(get_producto_service)):
    return uc.desactivar_producto(producto_id)