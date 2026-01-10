from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.models.producto_model import ProductoModel
from src.domain.ports.producto_port import ProductoPort
from src.infra.db.models.producto_table import ProductoTable 
from src.core.exceptions import NotFoundError

class ProductoRepository(ProductoPort):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def _to_domain(self, r: ProductoTable) -> ProductoModel:
        return ProductoModel(
            producto_id=r.producto_id,
            nombre=r.nombre,
            precio=r.precio,
            descripcion=r.descripcion,
            esta_activo=r.esta_activo,
            esta_destacado=r.esta_destacado,
            categoria_id=r.categoria_id,
            fecha_creacion=r.fecha_creacion
        )
    
    def get_by_id(self, producto_id: str) -> Optional[ProductoModel]:
        r = self.db_session.query(ProductoTable).filter_by(producto_id=producto_id).first()
        if not r:
            raise NotFoundError(f"Producto with id {producto_id} not found")
        return self._to_domain(r)
    
    def get_all(self) -> List[ProductoModel]:
        results = self.db_session.query(ProductoTable).all()
        return [self._to_domain(r) for r in results]
    
    def get_by_categoria(self, categoria_id: int) -> List[ProductoModel]:
        results = self.db_session.query(ProductoTable).filter_by(categoria_id=categoria_id).all()
        return [self._to_domain(r) for r in results]
    
    def create_producto(self, producto: ProductoModel) -> ProductoModel:
        new_producto = ProductoTable(
            producto_id=producto.producto_id,
            nombre=producto.nombre,
            precio=producto.precio,
            descripcion=producto.descripcion,
            esta_activo=producto.esta_activo,
            esta_destacado=producto.esta_destacado,
            categoria_id=producto.categoria_id,
            fecha_creacion=producto.fecha_creacion
        )
        self.db_session.add(new_producto)
        self.db_session.commit()
        #self.db_session.refresh(new_producto) refresh no va porque generamos el id fuera de la bd
        return self._to_domain(new_producto)
    
    def update_producto(self, producto_id: str, producto: ProductoModel) -> ProductoModel:
        r = self.db_session.query(ProductoTable).filter_by(producto_id=producto_id).first()
        if not r:
            raise NotFoundError(f"Producto with id {producto_id} not found")
        
        r.nombre = producto.nombre
        r.precio = producto.precio
        r.descripcion = producto.descripcion
        r.esta_activo = producto.esta_activo
        r.esta_destacado = producto.esta_destacado
        r.categoria_id = producto.categoria_id
        # no se modifica ni el ID ni la fecha_creacion
        self.db_session.commit()
        return self._to_domain(r)
    
    def delete_producto(self, producto_id: str) -> None:
        r = self.db_session.query(ProductoTable).filter_by(producto_id=producto_id).first()
        if not r:
            raise NotFoundError(f"Producto with id {producto_id} not found")
        self.db_session.delete(r)
        self.db_session.commit()