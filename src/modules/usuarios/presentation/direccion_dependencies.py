from src.core.database import get_session
from fastapi import Depends

# repository
from src.modules.usuarios.infra.direccion_repository import DireccionRepository

# usecases
from src.modules.usuarios.application.direccion.get_all_direcciones import GetAllDirecciones
from src.modules.usuarios.application.direccion.get_direccion_by_id import GetDireccionById
from src.modules.usuarios.application.direccion.create_direccion import CreateDireccion
from src.modules.usuarios.application.direccion.update_direccion import UpdateDireccion
from src.modules.usuarios.application.direccion.delete_direccion import DeleteDireccion
from src.modules.usuarios.application.direccion.set_primary import SetPrimaryDireccion

def get_all_direcciones_service(session=Depends(get_session)):
    repo = DireccionRepository(session)
    return GetAllDirecciones(repo)

def get_direccion_service(session=Depends(get_session)):
    repo = DireccionRepository(session)
    return GetDireccionById(repo)

def create_direccion_service(session=Depends(get_session)):
    repo = DireccionRepository(session)
    return CreateDireccion(repo)

def update_direccion_service(session=Depends(get_session)):
    repo = DireccionRepository(session)
    return UpdateDireccion(repo)

def delete_direccion_service(session=Depends(get_session)):
    repo = DireccionRepository(session)
    return DeleteDireccion(repo)

def set_primary_service(session=Depends(get_session)):
    repo = DireccionRepository(session)
    return SetPrimaryDireccion(repo)