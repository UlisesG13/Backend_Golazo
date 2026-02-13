from fastapi import Depends
from src.infra.db.database import get_session
from src.infra.db.repositories.factura_repository import FacturaRepository
from src.usecases.factura_uescase import FacturaUsecases

def get_factura_repository(session=Depends(get_session)):
    return FacturaRepository(session)

def get_factura_service(repo=Depends(get_factura_repository)):
    return FacturaUsecases(repo)
