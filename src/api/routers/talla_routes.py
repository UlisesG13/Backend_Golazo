from fastapi import APIRouter, Depends
from typing import List
from src.usecases.talla_usecase import TallaUsecases
from src.core.dependency_inyection.tallas_di import get_talla_service
from src.api.schemas.talla_dto import TallaDTO, TallaCreateDTO, TallaUpdateDTO

router = APIRouter(prefix="/api/tallas", tags=["tallas"])

@router.get("/", response_model=List[TallaDTO])
def list_tallas(
    talla_service: TallaUsecases = Depends(get_talla_service)
):
    return talla_service.get_all_tallas()


@router.get("/{talla_id}", response_model=TallaDTO)
def get_talla_by_id(
    talla_id: int,
    talla_service: TallaUsecases = Depends(get_talla_service)
):
    return talla_service.get_talla_by_id(talla_id)


@router.post("/", response_model=TallaDTO)
def create_talla(
    dto: TallaCreateDTO,
    talla_service: TallaUsecases = Depends(get_talla_service)
):
    return talla_service.create_talla(dto)


@router.put("/{talla_id}", response_model=TallaDTO)
def update_talla(
    talla_id: int,
    dto: TallaUpdateDTO,
    talla_service: TallaUsecases = Depends(get_talla_service)
):
    return talla_service.update_talla(talla_id, dto)


@router.delete("/{talla_id}", response_model=bool)
def delete_talla(
    talla_id: int,
    talla_service: TallaUsecases = Depends(get_talla_service)
):
    return talla_service.delete_talla(talla_id)
