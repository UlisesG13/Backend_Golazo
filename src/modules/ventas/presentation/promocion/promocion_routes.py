from fastapi import APIRouter, Depends, status

from src.modules.ventas.app.promocion import (
    CreatePromocion,
    UpdatePromocion,
    DeletePromocion,
    GetById,
    GetAll,
    ChangeStatus
)
from src.modules.ventas.presentation.promocion.promocion_dependencies import (
    create_promocion,
    update_promocion,
    delete_promocion,
    get_promocion_by_id,
    get_all_promociones,
    change_promocion_status
)
from src.modules.ventas.presentation.promocion.promocion_dto import PromocionCreateDTO, PromocionUpdateDTO, PromocionDTO

router = APIRouter()


@router.get("", response_model=list[PromocionDTO])
async def get_promociones(
        uc: GetAll = Depends(get_all_promociones)
):
    return await uc.execute()


@router.post("", response_model=PromocionDTO, status_code=status.HTTP_201_CREATED)
async def create_promocion_route(
        dto: PromocionCreateDTO,
        uc: CreatePromocion = Depends(create_promocion)
):
    return await uc.execute(dto)


@router.get("/{promocion_id}", response_model=PromocionDTO)
async def get_promocion_by_id_route(
        promocion_id: int,
        uc: GetById = Depends(get_promocion_by_id)
):
    return await uc.execute(promocion_id)


@router.put("/{promocion_id}", response_model=PromocionDTO)
async def update_promocion_route(
        promocion_id: int,
        dto: PromocionUpdateDTO,
        uc: UpdatePromocion = Depends(update_promocion)
):
    return await uc.execute(promocion_id, dto)


@router.delete("/{promocion_id}", status_code=204)
async def delete_promocion_route(
        promocion_id: int,
        uc: DeletePromocion = Depends(delete_promocion)
):
    await uc.execute(promocion_id)


@router.patch("/{promocion_id}/status", response_model=PromocionDTO)
async def change_status_route(
        promocion_id: int,
        nuevo_estado: bool,
        uc: ChangeStatus = Depends(change_promocion_status)
):
    return await uc.execute(promocion_id, nuevo_estado)
