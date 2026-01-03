from fastapi import APIRouter, Depends
from typing import List
from src.usecases.categoria_usecase import CategoriaUsecases
from src.core.dependency_inyection.categorias_di import get_categoria_service
from src.api.schemas.categoria_dto import CategoriaDTO, CategoriaCreateDTO, CategoriaUpdateDTO

router = APIRouter(prefix="/api/categorias", tags=["categorias"])


@router.get("/", response_model=List[CategoriaDTO])
def list_categorias(
    uc: CategoriaUsecases = Depends(get_categoria_service)
):
    return uc.get_categorias()


@router.get("/{categoria_id}/", response_model=CategoriaDTO)
def get_categoria_by_id(
    categoria_id: int,
    uc: CategoriaUsecases = Depends(get_categoria_service)
):
    return uc.get_categoria_by_id(categoria_id)


@router.get("/by-seccion/{seccion_id}/", response_model=List[CategoriaDTO])
def get_categorias_by_seccion(
    seccion_id: int,
    uc: CategoriaUsecases = Depends(get_categoria_service)
):
    return uc.get_categorias_by_seccion_id(seccion_id)


@router.post("/", response_model=CategoriaDTO)
def create_categoria(
    categoria: CategoriaCreateDTO,
    uc: CategoriaUsecases = Depends(get_categoria_service)
):
    return uc.create_categoria(categoria)


@router.put("/{categoria_id}/", response_model=CategoriaDTO)
def update_categoria(
    categoria_id: int,
    categoria: CategoriaUpdateDTO,
    uc: CategoriaUsecases = Depends(get_categoria_service)
):
    return uc.update_categoria(categoria_id, categoria)


@router.delete("/{categoria_id}/", status_code=204)
def delete_categoria(
    categoria_id: int,
    uc: CategoriaUsecases = Depends(get_categoria_service)
):
    uc.delete_categoria(categoria_id)
