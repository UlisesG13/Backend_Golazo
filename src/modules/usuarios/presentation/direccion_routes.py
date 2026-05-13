from fastapi import APIRouter, Depends

from src.modules.auth.domain.models import AuthenticatedUser
from src.modules.usuarios.presentation.schemas import DireccionDTO, DireccionRequestDTO
from src.core.security import get_current_user
from src.modules.usuarios.presentation.direccion_dependencies import get_all_direcciones_service, get_direccion_service, create_direccion_service, update_direccion_service, delete_direccion_service, set_primary_service
from src.modules.usuarios.application.direccion import GetAllDirecciones, GetDireccionById, CreateDireccion, UpdateDireccion, DeleteDireccion, SetPrimaryDireccion

router = APIRouter()

@router.get("", response_model=list[DireccionDTO])
def list_direcciones(user = Depends(get_current_user), uc: GetAllDirecciones = Depends(get_all_direcciones_service)):
    return uc.execute(user.usuario_id)

@router.post("", response_model=DireccionDTO)
def create_direccion(dto: DireccionRequestDTO, user = Depends(get_current_user), uc: CreateDireccion = Depends(create_direccion_service)):
    return uc.execute(user.usuario_id, dto)

@router.post("/{direccion_id}/set_primary")
def set_primary_direccion(direccion_id: int, user: AuthenticatedUser = Depends(get_current_user), uc: SetPrimaryDireccion = Depends(set_primary_service)):
    uc.execute(direccion_id, user.usuario_id)
    return {"message": "Dirección establecida como primaria correctamente"}

@router.get("/{direccion_id}", response_model=list[DireccionDTO])
def get_direccion(direccion_id: int, user = Depends(get_current_user), uc: GetDireccionById = Depends(get_direccion_service)):
    return uc.execute(direccion_id, user.usuario_id)

@router.put("/{direccion_id}", response_model=DireccionDTO)
def update_direccion(direccion_id: int, dto: DireccionRequestDTO, user = Depends(get_current_user), uc: UpdateDireccion = Depends(update_direccion_service)):
    return uc.execute(direccion_id, dto, user.usuario_id)

@router.delete("/{direccion_id}")
def delete_direccion(direccion_id: int, user: AuthenticatedUser = Depends(get_current_user), uc: DeleteDireccion = Depends(delete_direccion_service)):
    uc.execute(direccion_id, user.usuario_id)
    return {"message": "Dirección eliminada correctamente"}
