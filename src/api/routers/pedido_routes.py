from typing import List
from fastapi import APIRouter, Depends, status

from src.domain.models.pedido_model import PedidoModel
from src.usecases.pedido_usecase import PedidoUsecases
from src.core.dependency_inyection.pedido_di import get_pedido_service
from src.api.schemas.pedido_dto import PedidoCreateDto, PedidoDto, PedidoUpdateDto

router = APIRouter(prefix="/api/pedidos", tags=["pedidos"])

@router.get("/", response_model=list[PedidoDto])
def get_pedidos(service: PedidoUsecases = Depends(get_pedido_service)) -> list[PedidoModel]:
    return service.get_all()

@router.get("/user/{user_id}", response_model=List[PedidoDto])
def get_pedidos_by_user_id(user_id: str, service: PedidoUsecases = Depends(get_pedido_service)):
    return service.get_pedidos_by_user_id(user_id)

@router.get("/{pedido_id}", response_model=PedidoDto)
def get_pedido_by_id(pedido_id: str, service: PedidoUsecases = Depends(get_pedido_service)):
    return service.get_pedido_by_id(pedido_id)

@router.post("/", response_model=PedidoDto, status_code=status.HTTP_201_CREATED)
def create_pedido(pedido_data: PedidoCreateDto, service: PedidoUsecases = Depends(get_pedido_service)):
    return service.create_pedido(pedido_data)

@router.put("/{pedido_id}", response_model=PedidoDto)
def update_pedido(pedido_id: str, updated_data: PedidoUpdateDto, service: PedidoUsecases = Depends(get_pedido_service)):
    return service.update_pedido(pedido_id, updated_data)

@router.delete("/{pedido_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pedido(pedido_id: str, service: PedidoUsecases = Depends(get_pedido_service)):
    return service.delete_pedido(pedido_id)

@router.put("/{pedido_id}/promocion/{promocion_id}", response_model=PedidoDto)
def update_pedido_promocion(pedido_id: str, promocion_id: int, service: PedidoUsecases = Depends(get_pedido_service)):
    return service.update_pedido_promocion(pedido_id, promocion_id)

@router.put("/{pedido_id}/estado/{estado}", response_model=PedidoDto)
def update_pedido_estado(pedido_id: str, estado: str, service: PedidoUsecases = Depends(get_pedido_service)):
    return service.update_pedido_estado(pedido_id, estado)