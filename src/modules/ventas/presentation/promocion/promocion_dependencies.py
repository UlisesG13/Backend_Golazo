from fastapi import Depends

from src.core.database import get_session
from src.modules.ventas.app.promocion import (
    GetById,
    GetAll,
    ChangeStatus,
    CreatePromocion,
    DeletePromocion,
    UpdatePromocion
)
from src.modules.ventas.infra.promocion.promocion_repository import PromocionRepository


def get_promocion_by_id(session=Depends(get_session)):
    repo = PromocionRepository(session)
    return GetById(repo)


def get_all_promociones(session=Depends(get_session)):
    repo = PromocionRepository(session)
    return GetAll(repo)


def create_promocion(session=Depends(get_session)):
    repo = PromocionRepository(session)
    return CreatePromocion(repo)


def update_promocion(session=Depends(get_session)):
    repo = PromocionRepository(session)
    return UpdatePromocion(repo)


def delete_promocion(session=Depends(get_session)):
    repo = PromocionRepository(session)
    return DeletePromocion(repo)


def change_promocion_status(session=Depends(get_session)):
    repo = PromocionRepository(session)
    return ChangeStatus(repo)
