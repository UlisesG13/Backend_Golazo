from abc import ABC, abstractmethod
from typing import Optional, List
from src.domain.models.producto_model import ProductoModel

class ProductoPort(ABC):
    @abstractmethod
    def get_by_id(self, producto_id: str) -> Optional[ProductoModel]:
        """Obtiene producto por id"""

    @abstractmethod
    def get_all(self) -> List[ProductoModel]:
        """Obtiene todos lo productos"""

    @abstractmethod
    def get_by_categoria(self, categoria_id: int) -> List[ProductoModel]:
        """Obtiene todos los productos por categoria"""

    @abstractmethod
    def create_producto(self, producto: ProductoModel) -> ProductoModel:
        """Crea un producto"""

    @abstractmethod
    def update_producto(self, producto_id: str, producto: ProductoModel) -> ProductoModel:
        """Actualiza los campos de un producto"""

    @abstractmethod
    def delete_producto(self, producto_id: str) -> None:
        """Elimina un producto por su id"""