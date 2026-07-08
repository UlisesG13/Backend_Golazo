from fastapi import APIRouter, Depends

from src.modules.carrito.presentation.carrito_dto import CarritoResponse, AddItemRequest, UpdateItemQuantityRequest

from src.modules.carrito.presentation.carrito_dependencies import add_item, delete_cart, get_cart, delete_item, update_quantity
from src.modules.carrito.app import RemoveCartUseCase, GetCartUseCase, RemoveItemUseCase, AddItemUseCase, UpdateQuantityUseCase
from src.core.security import get_current_user

router = APIRouter()

@router.post("", response_model=CarritoResponse)
async def add_item_cart(
        request: AddItemRequest,
        uc: AddItemUseCase = Depends(add_item),
        user = Depends(get_current_user)
):
    carrito = await uc.execute(user.usuario_id, request)

    return carrito

@router.get("", response_model=CarritoResponse)
async def get_carrito(
    uc: GetCartUseCase = Depends(get_cart),
    user = Depends(get_current_user)
):
    return await uc.execute(user.usuario_id)

@router.delete("/items/{item_id}", status_code=204)
async def delete_item_cart(
    item_id: int,
    user = Depends(get_current_user),
    uc: RemoveItemUseCase = Depends(delete_item),
):
    await uc.execute(usuario_id=user.usuario_id, item_id=item_id)
    return None

@router.patch("/items/{item_id}", response_model=CarritoResponse)
async def update_quantity_cart(
    item_id: int,
    dto: UpdateItemQuantityRequest,
    uc: UpdateQuantityUseCase = Depends(update_quantity),
    user = Depends(get_current_user)
):
    return await uc.execute(user.usuario_id, item_id, dto.cantidad)

@router.delete("/{cart_id}", status_code=204)
async def delete_cart_user(
    cart_id: str,
    uc: RemoveCartUseCase = Depends(delete_cart),
):
    return await uc.execute(cart_id)
