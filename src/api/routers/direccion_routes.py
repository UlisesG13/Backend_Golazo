from fastapi import APIRouter, Depends
from typing import List
from src.core.security import crear_token
from src.usecases.direccion_usecase import DireccionUsecases
from src.core.dependency_inyection.direcciones_di import get_direccion_service
from src.api.schemas.direccion_dto import DireccionDTO, DireccionCreateDTO, DireccionUpdateDTO
from src.usecases.auth import auth

router = APIRouter(prefix="/api/users/direcciones", tags=["direcciones"])

@router.get("/", response_model=List[DireccionDTO])
def list_direcciones(user = Depends(auth), uc: DireccionUsecases = Depends(get_direccion_service)):
    return uc.get_direcciones(user.usuario_id)

@router.post("/", response_model=DireccionDTO)
def create_direccion(dto: DireccionCreateDTO, user = Depends(auth), uc: DireccionUsecases = Depends(get_direccion_service)):
    return uc.create_direccion(user.usuario_id, dto)

@router.put("/{direccion_id}", response_model=DireccionDTO)
def update_direccion(direccion_id: int, dto: DireccionUpdateDTO, user = Depends(auth), uc: DireccionUsecases = Depends(get_direccion_service)):
    return uc.update_direccion(direccion_id, dto)

@router.delete("/{direccion_id}")
def delete_direccion(direccion_id: int, user = Depends(auth), uc: DireccionUsecases = Depends(get_direccion_service)):
    uc.delete_direccion(direccion_id)
    return {"message": "Dirección eliminada correctamente"}

@router.post("/{direccion_id}/set_primary")
def set_primary_direccion(direccion_id: int, user = Depends(auth), uc: DireccionUsecases = Depends(get_direccion_service)):
    uc.set_primary_direccion(user.usuario_id, direccion_id)
    return {"message": "Dirección establecida como primaria correctamente"}