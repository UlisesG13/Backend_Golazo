from fastapi import Depends
from src.core.database import get_session
from src.infra.db.repositories.pedido_repository import PedidoRepository
from src.usecases.pedido_usecase import PedidoUsecases

def get_pedido_repository(session=Depends(get_session)):
    return PedidoRepository(session)

def get_pedido_service(repo=Depends(get_pedido_repository)):
    return PedidoUsecases(repo)