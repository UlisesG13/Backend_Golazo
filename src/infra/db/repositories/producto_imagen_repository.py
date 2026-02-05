from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.models.producto_imagen_model import ProductoImagenModel
from src.domain.ports.producto_imagen_port import ProductoImagenPort
from src.infra.db.models.producto_imagen_table import ProductoImagenTable
from src.core.exceptions import NotFoundError

class ProductoImagenRepository(ProductoImagenPort):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def _to_domain(self, r: ProductoImagenTable) -> ProductoImagenModel:
        return ProductoImagenModel(
            producto_imagen_id=r.producto_imagen_id,
            producto_id=r.producto_id,
            imagen_id=r.imagen_id,
            es_principal=r.es_principal
        )
    
    def create(self, r: ProductoImagenModel) -> ProductoImagenModel: 
        nueva_asociacion = ProductoImagenTable(
            producto_id=r.producto_id,
            imagen_id=r.imagen_id,
            es_principal=r.es_principal
        )
        self.db_session.add(nueva_asociacion)
        self.db_session.commit()
        self.db_session.refresh(nueva_asociacion)
        return self._to_domain(nueva_asociacion)
    
    def delete(self, producto_id: str, imagen_id: int) -> None:
        asociacion = self.db_session.query(ProductoImagenTable).filter_by(
            producto_id=producto_id,
            imagen_id=imagen_id
        ).first()
        if not asociacion:
            raise NotFoundError("La relación entre producto e imagen no existe")
        self.db_session.delete(asociacion)
        self.db_session.commit()

    def get_by_producto(self, producto_id: str) -> list[ProductoImagenModel]:
        asociaciones = self.db_session.query(ProductoImagenTable).filter_by(
            producto_id=producto_id
        ).all()
        return [self._to_domain(a) for a in asociaciones]
    
    def delete_by_producto(self, producto_id: str) -> None:
        asociaciones = self.db_session.query(ProductoImagenTable).filter_by(
            producto_id=producto_id
        ).all()
        for asociacion in asociaciones:
            self.db_session.delete(asociacion)
        self.db_session.commit()