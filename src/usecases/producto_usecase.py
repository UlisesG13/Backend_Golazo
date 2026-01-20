from src.api.schemas.producto_dto import ProductoDTO, ProductoCreateDTO, ProductoUpdateDTO
from src.domain.models.producto_model import ProductoModel
from src.domain.ports.producto_port import ProductoPort
from uuid import uuid4
from datetime import datetime, timedelta, timezone

class ProductoUsecases:
    def __init__(self, repo: ProductoPort):
        self.repo = repo

    def list_productos(self) -> list[ProductoModel]:
        return self.repo.get_all()
    
    def get_producto_by_id(self, producto_id: str) -> ProductoModel:
        return self.repo.get_by_id(producto_id)
    
    def get_productos_by_categoria(self, categoria_id: int) -> list[ProductoModel]:
        return self.repo.get_by_categoria(categoria_id)
    
    def create_producto(self, dto: ProductoCreateDTO) -> ProductoModel:
        producto = ProductoModel(
            producto_id=str(uuid4()),
            nombre=dto.nombre,
            precio=dto.precio,
            descripcion=dto.descripcion,
            esta_activo=dto.esta_activo,
            esta_destacado=dto.esta_destacado,
            categoria_id=dto.categoria_id,
            fecha_creacion=datetime.now()
        )
        return self.repo.create_producto(producto)
    
    def update_producto(self, producto_id: str, dto: ProductoUpdateDTO) -> ProductoModel:
        producto = self.repo.get_by_id(producto_id) # si no lo encuentra lanza NotFoundError desde el repositorio
        producto.nombre = dto.nombre
        producto.precio = dto.precio
        producto.descripcion = dto.descripcion
        producto.esta_activo = dto.esta_activo
        producto.esta_destacado = dto.esta_destacado
        producto.categoria_id = dto.categoria_id
        return self.repo.update_producto(producto_id, producto)
    
    def delete_producto(self, producto_id: str) -> None:
        return self.repo.delete_producto(producto_id)
    
    def mark_producto_as_destacado(self, producto_id: str) -> ProductoModel:
        producto = self.repo.get_by_id(producto_id) # si no lo encuentra lanza NotFoundError desde el repositorio
        producto.esta_destacado = True
        return self.repo.update_producto(producto_id, producto)
    
    def unmark_producto_as_destacado(self, producto_id: str) -> ProductoModel:
        producto = self.repo.get_by_id(producto_id) # si no lo encuentra lanza NotFoundError desde el repositorio
        producto.esta_destacado = False
        return self.repo.update_producto(producto_id, producto)
    
    def desactivar_producto(self, producto_id: str) -> ProductoModel:
        producto = self.repo.get_by_id(producto_id) # si no lo encuentra lanza NotFoundError desde el repositorio
        producto.esta_activo = False
        return self.repo.update_producto(producto_id, producto)
    
    def activar_producto(self, producto_id: str) -> ProductoModel:
        producto = self.repo.get_by_id(producto_id) # si no lo encuentra lanza NotFoundError desde el repositorio
        producto.esta_activo = True
        return self.repo.update_producto(producto_id, producto)
