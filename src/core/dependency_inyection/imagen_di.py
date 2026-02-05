from fastapi import Depends
from src.infra.db.database import get_session
from src.infra.db.repositories.imagen_repository import ImagenRepository
from src.infra.db.repositories.producto_imagen_repository import ProductoImagenRepository
from src.infra.storage.repositories.supabase_storage_repository import SupabaseStorageRepository
from src.infra.storage.supabase import get_supabase_client
from src.usecases.imagen_usecase import ImagenUsecases

def get_imagen_repository(session=Depends(get_session)):
    return ImagenRepository(session)

def get_producto_imagen_repository(session=Depends(get_session)):
    return ProductoImagenRepository(session)

def get_imagen_storage_repository(client=Depends(get_supabase_client)):
    return SupabaseStorageRepository(client)

def get_imagen_service(
    imagen_repo=Depends(get_imagen_repository),
    producto_imagen_repo=Depends(get_producto_imagen_repository),
    storage_repo=Depends(get_imagen_storage_repository),
):
    return ImagenUsecases(imagen_repo, producto_imagen_repo, storage_repo)
