from abc import ABC, abstractmethod
from typing import List
from src.domain.models.producto_color_model import ProductoColorModel

class ProductoColorPort(ABC):
    @abstractmethod
    def assign_color_to_producto(self, producto_color: ProductoColorModel) -> ProductoColorModel:
        """Asigna un color a un producto"""

    @abstractmethod
    def get_colors_by_producto(self, producto_id: str) -> List[ProductoColorModel]:
        """Obtiene todos los colores de un producto"""

    @abstractmethod
    def remove_color_from_producto(self, producto_id: str, color_id: int) -> bool:
        """Desasigna un color de un producto"""

    @abstractmethod
    def get_producto_color_by_id(self, producto_color_id: int) -> ProductoColorModel:
        """Obtiene una asignación específica"""