from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query

from src.modules.auth.domain.models import AuthenticatedUser
from src.modules.ventas.app.pedido import (
    CreatePedido,
    GetPedidos,
    GetPedidoById,
    GetPedidosByUser,
    ChangePedidoStatus,
)
from src.modules.ventas.infra.pedido.pedido_table import EstadoPedido
from src.modules.ventas.presentation.pedido.pedido_dependencies import (
    get_create_pedido,
    get_all_pedidos,
    get_by_id,
    get_by_user,
    get_change_status,
)
from src.modules.ventas.presentation.pedido.pedido_dto import CreatePedidoDTO, PedidoDTO, ChangeStatusDTO
from src.shared.security import get_current_user

router = APIRouter()


@router.post("/", response_model=PedidoDTO)
def create_pedido(
        dto: CreatePedidoDTO,
        uc: CreatePedido = Depends(get_create_pedido),
        user: AuthenticatedUser = Depends(get_current_user)
):
    try:
        pedido = uc.execute(dto, user.usuario_id)
        return pedido
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[PedidoDTO])
def get_pedidos(
        status: EstadoPedido | None = Query(default=None),
        uc: GetPedidos = Depends(get_all_pedidos),
):
    return uc.execute(status)


@router.get("/{pedido_id}", response_model=PedidoDTO)
def get_pedido_by_id(
        pedido_id: int,
        uc: GetPedidoById = Depends(get_by_id),
):
    try:
        return uc.execute(pedido_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/user/{usuario_id}", response_model=List[PedidoDTO])
def get_pedidos_by_user(
        usuario_id: str,
        uc: GetPedidosByUser = Depends(get_by_user),
):
    return uc.execute(usuario_id)


@router.patch("/{pedido_id}/status")
def change_status(
        pedido_id: int,
        dto: ChangeStatusDTO,
        uc: ChangePedidoStatus = Depends(get_change_status),
):
    uc.execute(pedido_id, dto.status.value)
    return {"message": "Estado actualizado"}
