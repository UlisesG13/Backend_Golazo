from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.models.pedido_item_model import PedidoItemModel
from src.domain.ports.pedido_item_port import PedidoItemPort
from src.infra.db.models.pedido_item_table import PedidoItemTable
from src.core.exceptions import NotFoundError

class PedidoItemRepository(PedidoItemPort):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def __to_domain(self, r: PedidoItemTable) -> PedidoItemModel:
        return PedidoItemModel(
            pedido_item_id=r.pedido_item_id,
            pedido_id=r.pedido_id,
            producto_id=r.producto_id,
            color_id=r.color_id,
            talla_id=r.talla_id,
            cantidad=r.cantidad,
        )
    
    def add(self, item: PedidoItemModel) -> PedidoItemModel:
        new_item = PedidoItemTable(
            pedido_id=item.pedido_id,
            producto_id=item.producto_id,
            color_id=item.color_id,
            talla_id=item.talla_id,
            cantidad=item.cantidad,
        )
        self.db_session.add(new_item)
        self.db_session.commit()
        self.db_session.refresh(new_item)
        return self.__to_domain(new_item)
    
    def remove(self, item_id: int) -> None:
        item = self.db_session.query(PedidoItemTable).filter_by(pedido_item_id=item_id).first()
        if not item:
            raise NotFoundError(f"PedidoItem with id {item_id} not found")
        self.db_session.delete(item)
        self.db_session.commit()

    def update(self, item_id: int, item: PedidoItemModel) -> PedidoItemModel:
        existing_item = self.db_session.query(PedidoItemTable).filter_by(pedido_item_id=item_id).first()
        if not existing_item:
            raise NotFoundError(f"PedidoItem with id {item_id} not found")
        
        existing_item.producto_id = item.producto_id
        existing_item.color_id = item.color_id
        existing_item.talla_id = item.talla_id
        existing_item.cantidad = item.cantidad
        
        self.db_session.commit()
        self.db_session.refresh(existing_item)
        return self.__to_domain(existing_item)
    
    def list_items(self, pedido_id: int) -> List[PedidoItemModel]:
        items = self.db_session.query(PedidoItemTable).filter_by(pedido_id=pedido_id).all()
        return [self.__to_domain(item) for item in items]
