from typing import List

from fastapi import APIRouter, Depends, Query, status

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
from src.core.security import get_current_user

router = APIRouter()


@router.post("/", response_model=PedidoDTO, status_code=status.HTTP_201_CREATED)
async def create_pedido(
        dto: CreatePedidoDTO,
        uc: CreatePedido = Depends(get_create_pedido),
        user: AuthenticatedUser = Depends(get_current_user)
):
    pedido = await uc.execute(dto, user.usuario_id)
    return pedido


@router.get("/", response_model=List[PedidoDTO])
async def get_pedidos(
        status: EstadoPedido | None = Query(default=None),
        uc: GetPedidos = Depends(get_all_pedidos),
):
    return await uc.execute(status)


@router.get("/{pedido_id}", response_model=PedidoDTO)
async def get_pedido_by_id(
        pedido_id: int,
        uc: GetPedidoById = Depends(get_by_id),
):
    return await uc.execute(pedido_id)


@router.get("/user/{usuario_id}", response_model=List[PedidoDTO])
async def get_pedidos_by_user(
        usuario_id: str,
        uc: GetPedidosByUser = Depends(get_by_user),
):
    return await uc.execute(usuario_id)


@router.patch("/{pedido_id}/status")
async def change_status(
        pedido_id: int,
        dto: ChangeStatusDTO,
        uc: ChangePedidoStatus = Depends(get_change_status),
):
    await uc.execute(pedido_id, dto.status.value)
    return {"message": "Estado actualizado"}
