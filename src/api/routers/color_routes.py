from fastapi import APIRouter, Depends
from typing import List
from src.usecases.color_usecase import ColorUsecases
from src.core.dependency_inyection.colores_di import get_color_service
from src.api.schemas.color_dto import ColorDTO, ColorCreateDTO, ColorUpdateDTO

router = APIRouter(prefix="/api/colores", tags=["colores"])

@router.get("/", response_model=List[ColorDTO])
def list_colors(
    color_service: ColorUsecases = Depends(get_color_service)
):
    return color_service.get_all_colors()

@router.get("/{color_id}", response_model=ColorDTO)
def get_color_by_id(
    color_id: int,
    color_service: ColorUsecases = Depends(get_color_service)
):
    return color_service.get_color_by_id(color_id)

@router.post("/", response_model=ColorDTO)
def create_color(
    dto: ColorCreateDTO,
    color_service: ColorUsecases = Depends(get_color_service)
):
    return color_service.create_color(dto)

@router.put("/{color_id}", response_model=ColorDTO)
def update_color(
    color_id: int,
    dto: ColorUpdateDTO,
    color_service: ColorUsecases = Depends(get_color_service)
):
    return color_service.update_color(color_id, dto)

@router.delete("/{color_id}", response_model=bool)
def delete_color(
    color_id: int,
    color_service: ColorUsecases = Depends(get_color_service)
):
    return color_service.delete_color(color_id)