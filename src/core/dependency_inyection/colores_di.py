from fastapi import Depends
from src.infra.db.database import get_session
from src.infra.db.repositories.color_repository import ColorRepository
from src.usecases.color_usecase import ColorUsecases

def get_color_repository(session=Depends(get_session)):
    return ColorRepository(session)

def get_color_service(repo=Depends(get_color_repository)):
    return ColorUsecases(repo)