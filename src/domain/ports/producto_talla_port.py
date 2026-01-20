from abc import ABC, abstractmethod
from typing import List
from src.domain.models.producto_color_model import ProductoColorModel

class ProductoTallaPort(ABC):
    @abstractmethod
    def assign_talla_to_producto(self, producto_talla: ProductoColorModel) -> ProductoColorModel:
        """Asigna una talla a un producto"""

    @abstractmethod
    def get_tallas_by_producto(self, producto_id: str) -> List[ProductoColorModel]:
        """Obtiene todas las tallas de un producto"""

    @abstractmethod
    def remove_talla_from_producto(self, producto_id: str, talla_id: int) -> bool:
        """Desasigna una talla de un producto"""

    @abstractmethod
    def get_producto_talla_by_id(self, producto_talla_id: int) -> ProductoColorModel:
        """Obtiene una asignación específica"""