from fastapi import APIRouter, Depends
from typing import List
from src.core.security import crear_token
from src.usecases.promocion_usecase import PromocionUsecases
from src.core.dependency_inyection.promocion_di import get_promocion_service
from src.api.schemas.promocion_dto import PromocionDTO, PromocionCreateDTO, PromocionUpdateDTO

router = APIRouter()

@router.post("", response_model=PromocionDTO)
def create_promocion(promocion_data: PromocionCreateDTO, promocion_service: PromocionUsecases = Depends(get_promocion_service)):
    return promocion_service.create_promocion(promocion_data)

@router.get("", response_model=List[PromocionDTO])
def get_all_promociones(promocion_service: PromocionUsecases = Depends(get_promocion_service)):
    return promocion_service.get_all_promociones()

@router.post("/{promocion_id}/activar", response_model=PromocionDTO)
def activar_promocion(promocion_id: int, promocion_service: PromocionUsecases = Depends(get_promocion_service)):
    return promocion_service.activar_promocion(promocion_id)

@router.post("/{promocion_id}/desactivar", response_model=PromocionDTO)
def desactivar_promocion(promocion_id: int, promocion_service: PromocionUsecases = Depends(get_promocion_service)):
    return promocion_service.desactivar_promocion(promocion_id)

@router.get("/{promocion_id}", response_model=PromocionDTO)
def get_promocion_by_id(promocion_id: int, promocion_service: PromocionUsecases = Depends(get_promocion_service)):
    return promocion_service.get_by_id(promocion_id)

@router.put("/{promocion_id}", response_model=PromocionDTO)
def update_promocion(promocion_id: int, updated_data: PromocionUpdateDTO, promocion_service: PromocionUsecases = Depends(get_promocion_service)):
    return promocion_service.update_promocion(promocion_id, updated_data)

@router.delete("/{promocion_id}")
def delete_promocion(promocion_id: int, promocion_service: PromocionUsecases = Depends(get_promocion_service)):
    promocion_service.delete(promocion_id)
    return {"message": "Promoción eliminada exitosamente."}
