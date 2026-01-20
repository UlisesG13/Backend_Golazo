from fastapi import APIRouter, Depends
from typing import List
from src.usecases.producto_talla_usecase import ProductoTallaUsecases
from src.core.dependency_inyection.producto_talla_di import get_producto_talla_service
from src.api.schemas.producto_talla_dto import ProductoTallaCreateDTO, ProductoTallaDTO

router = APIRouter(prefix="/api/productos", tags=["productos-tallas"])

@router.get("/{producto_id}/tallas", response_model=List[ProductoTallaDTO])
def get_tallas_by_producto(
    producto_id: str,
    service: ProductoTallaUsecases = Depends(get_producto_talla_service),
):
    return service.get_tallas_by_producto(producto_id)


@router.post("/tallas", response_model=ProductoTallaDTO)
def assign_talla_to_producto(
    dto: ProductoTallaCreateDTO,
    service: ProductoTallaUsecases = Depends(get_producto_talla_service),
):
    return service.assign_talla_to_producto(dto)


@router.delete("/{producto_id}/tallas/{talla_id}", response_model=bool)
def remove_talla_from_producto(
    producto_id: str,
    talla_id: int,
    service: ProductoTallaUsecases = Depends(get_producto_talla_service),
):
    return service.remove_talla_from_producto(producto_id, talla_id)


@router.get("/tallas/{producto_talla_id}", response_model=ProductoTallaDTO)
def get_producto_talla_by_id(
    producto_talla_id: int,
    service: ProductoTallaUsecases = Depends(get_producto_talla_service),
):
    return service.get_producto_talla_by_id(producto_talla_id)
