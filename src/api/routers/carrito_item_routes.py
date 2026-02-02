from fastapi import APIRouter, Depends
from src.usecases.carrito_item_usecase import CarritoItemUseCases
from src.core.dependency_inyection.carrito_item_di import get_carrito_item_service
from src.api.schemas.carrito_item_dto import CarritoItemCreateDTO, CarritoItemDTO, CarritoItemUpdateDTO

router = APIRouter(prefix="/api/carrito", tags=["carrito"])

@router.get("/{carrito_id}/items", response_model=list[CarritoItemDTO])
def get_carrito_items(
    carrito_id: str,
    service: CarritoItemUseCases = Depends(get_carrito_item_service),
):
    return service.get_items_by_carrito_id(carrito_id)

@router.post("/{carrito_id}/item", response_model=CarritoItemDTO)
def add_item_to_carrito(
    carrito_id: str,
    dto: CarritoItemCreateDTO,
    service: CarritoItemUseCases = Depends(get_carrito_item_service),
):
    return service.add_item_to_carrito(carrito_id, dto)

@router.put("/{carrito_id}/item/{item_id}", response_model=CarritoItemDTO)
def update_carrito_item(
    carrito_id: str,
    item_id: str,
    dto: CarritoItemUpdateDTO,
    service: CarritoItemUseCases = Depends(get_carrito_item_service),
):
    return service.update_item_in_carrito(carrito_id, item_id, dto)

@router.delete("/{carrito_id}/item/{item_id}", response_model=None)
def remove_item_from_carrito(
    carrito_id: str,
    item_id: str,
    service: CarritoItemUseCases = Depends(get_carrito_item_service),
):
    service.remove_item_from_carrito(carrito_id, item_id)