from fastapi import Depends
from src.infra.db.database import get_session
from src.infra.db.repositories.categoria_repository import CategoriaRepository
from src.usecases.categoria_usecase import CategoriaUsecases


def get_categoria_repository(session=Depends(get_session)):
    return CategoriaRepository(session)

def get_categoria_service(repo=Depends(get_categoria_repository)):
    return CategoriaUsecases(repo)
