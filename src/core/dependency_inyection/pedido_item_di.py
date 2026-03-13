from fastapi import Depends
from src.core.database import get_session
from src.infra.db.repositories.pedido_item_repository import PedidoItemRepository
from src.usecases.pedido_item_usecase import PedidoItemUsecases

def get_pedido_item_repository(session=Depends(get_session)):
    return PedidoItemRepository(session)

def get_pedido_item_service(repo=Depends(get_pedido_item_repository)):
    return PedidoItemUsecases(repo)
