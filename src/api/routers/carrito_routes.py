from fastapi import APIRouter, Depends
from src.usecases.carrito_usecase import CarritoUseCases
from src.core.dependency_inyection.carrito_di import get_carrito_service
from src.api.schemas.carrito_dto import CreateCarritoDTO, UpdateCarritoDTO, CarritoDTO

router = APIRouter()

@router.post("", response_model=CarritoDTO)
def create_carrito(
    dto: CreateCarritoDTO,
    service: CarritoUseCases = Depends(get_carrito_service),
):
    return service.create_carrito(dto)

@router.get("/usuario/{usuario_id}", response_model=CarritoDTO)
def get_carrito_by_user(
    usuario_id: str,
    service: CarritoUseCases = Depends(get_carrito_service),
):
    return service.get_carrito_by_user_id(usuario_id)

@router.delete("/usuario/{usuario_id}", status_code=204)
def delete_carrito(
    usuario_id: str,
    service: CarritoUseCases = Depends(get_carrito_service),
):
    service.delete_carrito(usuario_id)
