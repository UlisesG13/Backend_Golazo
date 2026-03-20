from typing import List
from fastapi import APIRouter, Depends, status
from src.usecases.pedido_item_usecase import PedidoItemUsecases
from src.core.dependency_inyection.pedido_item_di import get_pedido_item_service
from src.api.schemas.pedido_item_dto import PedidoItemCreateDto, PedidoItemDto

router = APIRouter()

@router.post("/items", response_model=PedidoItemDto, status_code=status.HTTP_201_CREATED)
def add_pedido_item(item_data: PedidoItemCreateDto, service: PedidoItemUsecases = Depends(get_pedido_item_service)):
    return service.add_item_to_pedido(item_data)

@router.delete("/items/{pedido_item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_pedido_item(pedido_item_id: int, service: PedidoItemUsecases = Depends(get_pedido_item_service)):
    return service.remove_item_from_pedido(pedido_item_id)

@router.get("/{pedido_id}/items", response_model=List[PedidoItemDto])
def list_pedido_items(pedido_id: int, service: PedidoItemUsecases = Depends(get_pedido_item_service)):
    return service.get_items(pedido_id)
