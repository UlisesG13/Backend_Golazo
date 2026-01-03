from fastapi import APIRouter, Depends
from typing import List
from src.usecases.seccion_usecase import SeccionUsecases
from core.dependency_inyection.seccion_di import get_seccion_service
from src.api.schemas.seccion_dto import SeccionDTO, SeccionCreateDTO, SeccionUpdateDTO

router = APIRouter(prefix="/api/secciones", tags=["secciones"])

@router.get("/", response_model=List[SeccionDTO])
def list_secciones(
    uc: SeccionUsecases = Depends(get_seccion_service)
):
    return uc.get_secciones()

@router.get("/{seccion_id}/", response_model=SeccionDTO)
def get_seccion_by_id(
    seccion_id: int,
    uc: SeccionUsecases = Depends(get_seccion_service)
):
    return uc.get_seccion_by_id(seccion_id)

@router.post("/", response_model=SeccionDTO)
def create_seccion(
    seccion: SeccionCreateDTO,
    uc: SeccionUsecases = Depends(get_seccion_service)
):
    return uc.create_seccion(seccion)

@router.put("/{seccion_id}/", response_model=SeccionDTO)
def update_seccion(
    seccion_id: int,
    seccion: SeccionUpdateDTO,
    uc: SeccionUsecases = Depends(get_seccion_service)
):
    return uc.update_seccion(seccion_id, seccion)

@router.delete("/{seccion_id}/", status_code=204)
def delete_seccion(
    seccion_id: int,
    uc: SeccionUsecases = Depends(get_seccion_service)
):
    uc.delete_seccion(seccion_id)