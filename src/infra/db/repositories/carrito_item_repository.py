from typing import List, Optional
from sqlalchemy.orm import Session
from domain.models.carrito_item_model import CarritoItemModel
from domain.ports.carrito_item_port import CarritoItemPort
from infra.db.models.carrito_item_table import CarritoItemTable
from infra.db.models.carrito_table import CarritoTable
from src.core.exceptions import NotFoundError

class CarritoItemRepository(CarritoItemPort):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def _to_domain(self, r: CarritoItemTable) -> CarritoItemModel:
        return CarritoItemModel(
            carrito_item_id=r.carrito_item_id,
            carrito_id=r.carrito_id,
            producto_id=r.producto_id,
            color_id=r.color_id,
            talla_id=r.talla_id,
            cantidad=r.cantidad,
            precio_unitario=r.precio_unitario
        )
    
    def add_item_to_carrito(self, carrito_id: str, item: CarritoItemModel) -> CarritoItemModel:
        db_item = CarritoItemTable(
            carrito_id=carrito_id,
            producto_id=item.producto_id,
            color_id=item.color_id,
            talla_id=item.talla_id,
            cantidad=item.cantidad,
            precio_unitario=item.precio_unitario
        )
        self.db_session.add(db_item)
        self.db_session.commit()
        self.db_session.refresh(db_item)
        return self._to_domain(db_item)
    
    def remove_item_from_carrito(self, carrito_id: str, item_id: str) -> None:
        db_item = self.db_session.query(CarritoItemTable).filter_by(carrito_id=carrito_id, carrito_item_id=item_id).first()
        if not db_item:
            raise NotFoundError(f"Item with ID {item_id} not found in carrito {carrito_id}")
        self.db_session.delete(db_item)
        self.db_session.commit()

    def update_item_in_carrito(self, carrito_id: str, item_id: str, updated_item: CarritoItemModel) -> CarritoItemModel:
        db_item = self.db_session.query(CarritoItemTable).filter_by(carrito_id=carrito_id, carrito_item_id=item_id).first()
        if not db_item:
            raise NotFoundError(f"Item with ID {item_id} not found in carrito {carrito_id}")
        
        db_item.producto_id = updated_item.producto_id
        db_item.color_id = updated_item.color_id
        db_item.talla_id = updated_item.talla_id
        db_item.cantidad = updated_item.cantidad
        db_item.precio_unitario = updated_item.precio_unitario
        
        self.db_session.commit()
        self.db_session.refresh(db_item)
        return self._to_domain(db_item)
    
    def get_items_by_carrito_id(self, carrito_id: str) -> List[CarritoItemModel]:
        carrito = self.db_session.query(CarritoTable).filter_by(carrito_id=carrito_id).first()
        if not carrito:
            raise NotFoundError(f"Carrito with ID {carrito_id} not found")

        db_items = self.db_session.query(CarritoItemTable).filter_by(carrito_id=carrito_id).all()
        if not db_items:
            raise NotFoundError(f"No se encontraron items para el carrito con ID {carrito_id}")
        return [self._to_domain(item) for item in carrito.items]