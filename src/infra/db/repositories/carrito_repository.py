from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.models.carrito_model import CarritoModel
from src.domain.ports.carrito_port import CarritoPort
from src.infra.db.models.carrito_table import CarritoTable
from src.core.exceptions import NotFoundError

class CarritoRepository(CarritoPort):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def _to_domain(self, r: CarritoTable) -> CarritoModel:
        return CarritoModel(
            carrito_id=r.carrito_id,
            usuario_id=r.usuario_id,
            fecha_creacion=r.fecha_creacion,
            fecha_actualizacion=r.fecha_actualizacion
        )
    
    def get_by_user_id(self, user_id: str) -> CarritoModel:
        carrito = self.db_session.query(CarritoTable).filter_by(usuario_id=user_id).first()
        if not carrito:
            raise NotFoundError("Carrito no encontrado")
        return self._to_domain(carrito)
        
    def create_carrito(self, carrito: CarritoModel) -> CarritoModel:
        nuevo_carrito = CarritoTable(
            usuario_id=carrito.usuario_id,
            fecha_creacion=carrito.fecha_creacion,
            fecha_actualizacion=carrito.fecha_actualizacion
        )
        self.db_session.add(nuevo_carrito)
        self.db_session.commit()
        self.db_session.refresh(nuevo_carrito)
        return self._to_domain(nuevo_carrito)
    
    def udate_carrito(self, carrito_id: str, updated_data: CarritoModel) -> CarritoModel:
        carrito_db = self.db_session.query(CarritoTable).filter_by(carrito_id=carrito_id).first()
        if not carrito_db:
            raise NotFoundError("Carrito no encontrado")
        
        carrito_db.fecha_actualizacion = updated_data.fecha_actualizacion
        
        self.db_session.commit()
        return self._to_domain(carrito_db)
    
    def delete_carrito(self, carrito_id: str) -> None:
        carrito_db = self.db_session.query(CarritoTable).filter_by(carrito_id=carrito_id).first()
        if not carrito_db:
            raise NotFoundError("Carrito no encontrado")
        
        self.db_session.delete(carrito_db)
        self.db_session.commit()