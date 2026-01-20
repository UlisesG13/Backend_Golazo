from fastapi import APIRouter, Depends
from typing import List
from src.usecases.producto_color_usecase import ProductoColorUsecases
from src.core.dependency_inyection.producto_color_di import get_producto_color_service
from src.api.schemas.producto_color_dto import ProductoColorCreateDTO, ProductoColorDTO

router = APIRouter(prefix="/api/productos", tags=["productos-colores"])

@router.get("/{producto_id}/colores", response_model=List[ProductoColorDTO])
def get_colors_by_producto(
    producto_id: str,
    service: ProductoColorUsecases = Depends(get_producto_color_service)
):
    return service.get_colors_by_producto(producto_id)

@router.post("/colores", response_model=ProductoColorDTO)
def assign_color_to_producto(
    dto: ProductoColorCreateDTO,
    service: ProductoColorUsecases = Depends(get_producto_color_service)
):
    return service.assign_color_to_producto(dto)

@router.delete("/{producto_id}/colores/{color_id}", response_model=bool)
def remove_color_from_producto(
    producto_id: str,
    color_id: int,
    service: ProductoColorUsecases = Depends(get_producto_color_service)
):
    return service.remove_color_from_producto(producto_id, color_id)

@router.get("/colores/{producto_color_id}", response_model=ProductoColorDTO)
def get_producto_color_by_id(
    producto_color_id: int,
    service: ProductoColorUsecases = Depends(get_producto_color_service)
):
    return service.get_producto_color_by_id(producto_color_id)