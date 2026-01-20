from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.models.producto_color_model import ProductoColorModel
from src.domain.ports.producto_color_port import ProductoColorPort
from src.infra.db.models.producto_color_table import ProductoColorTable
from src.core.exceptions import NotFoundError

class ProductoColorRepository(ProductoColorPort):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def _to_domain(self, r: ProductoColorTable) -> ProductoColorModel:
        return ProductoColorModel(
            producto_color_id = r.producto_color_id,
            producto_id = r.producto_id,
            color_id = r.color_id
        )
    
    def assign_color_to_producto(self, p_color: ProductoColorModel) -> ProductoColorModel:
        producto_color = ProductoColorTable(
            producto_id=p_color.producto_id,
            color_id=p_color.color_id
        )
        self.db_session.add(producto_color)
        self.db_session.commit()
        self.db_session.refresh(producto_color)
        return self._to_domain(producto_color)
    
    def get_colors_by_producto(self, producto_id: str) -> List[ProductoColorModel]:
        producto_colors = self.db_session.query(ProductoColorTable).filter(ProductoColorTable.producto_id == producto_id).all()
        return [self._to_domain(r) for r in producto_colors]
    
    def remove_color_from_producto(self, producto_id: str, color_id: int) -> bool:
        producto_color = self.db_session.query(ProductoColorTable).filter(
            ProductoColorTable.producto_id == producto_id,
            ProductoColorTable.color_id == color_id
        ).first()
        if not producto_color:
            raise NotFoundError(f"Asignación de color con Producto ID {producto_id} y Color ID {color_id} no encontrada")
        self.db_session.delete(producto_color)
        self.db_session.commit()
        return True
    
    def get_producto_color_by_id(self, producto_color_id: int) -> ProductoColorModel:
        producto_color = self.db_session.query(ProductoColorTable).filter(ProductoColorTable.producto_color_id == producto_color_id).first()
        if not producto_color:
            raise NotFoundError(f"Asignación de color con ID {producto_color_id} no encontrada")
        return self._to_domain(producto_color)