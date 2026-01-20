from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.models.producto_talla_model import ProductoTallaModel
from src.domain.ports.producto_talla_port import ProductoTallaPort
from src.infra.db.models.producto_talla_table import ProductoTallaTable
from src.core.exceptions import NotFoundError

class ProductoTallaRepository(ProductoTallaPort):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def _to_domain(self, r: ProductoTallaTable) -> ProductoTallaModel:
        return ProductoTallaModel(
            producto_talla_id = r.producto_talla_id,
            producto_id = r.producto_id,
            talla_id = r.talla_id
        )

    def assign_talla_to_producto(self, p_talla: ProductoTallaModel) -> ProductoTallaModel:
        producto_talla = ProductoTallaTable(
            producto_id=p_talla.producto_id,
            talla_id=p_talla.talla_id
        )
        self.db_session.add(producto_talla)
        self.db_session.commit()
        self.db_session.refresh(producto_talla)
        return self._to_domain(producto_talla)

    def get_tallas_by_producto(self, producto_id: str) -> List[ProductoTallaModel]:
        producto_tallas = self.db_session.query(ProductoTallaTable).filter(ProductoTallaTable.producto_id == producto_id).all()
        return [self._to_domain(r) for r in producto_tallas]

    def remove_talla_from_producto(self, producto_id: str, talla_id: int) -> bool:
        producto_talla = self.db_session.query(ProductoTallaTable).filter(
            ProductoTallaTable.producto_id == producto_id,
            ProductoTallaTable.talla_id == talla_id
        ).first()
        if not producto_talla:
            raise NotFoundError(f"Asignación de talla con Producto ID {producto_id} y Talla ID {talla_id} no encontrada")
        self.db_session.delete(producto_talla)
        self.db_session.commit()
        return True

    def get_producto_talla_by_id(self, producto_talla_id: int) -> ProductoTallaModel:
        producto_talla = self.db_session.query(ProductoTallaTable).filter(ProductoTallaTable.producto_talla_id == producto_talla_id).first()
        if not producto_talla:
            raise NotFoundError(f"Asignación de talla con ID {producto_talla_id} no encontrada")
        return self._to_domain(producto_talla)