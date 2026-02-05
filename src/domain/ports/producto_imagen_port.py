from abc import ABC, abstractmethod
from typing import List
from src.domain.models.producto_imagen_model import ProductoImagenModel

class ProductoImagenPort(ABC):

    @abstractmethod
    def create(self, relation: ProductoImagenModel) -> ProductoImagenModel:
        """Crear la relación entre producto e imagen"""

    @abstractmethod
    def delete(self, producto_id: str, imagen_id: int) -> None:
        """Eliminar la relación entre producto e imagen"""

    @abstractmethod
    def get_by_producto(self, producto_id: str) -> list[ProductoImagenModel]:
        """Obtener las imágenes asociadas a un producto"""

    @abstractmethod
    def delete_by_producto(self, producto_id: str) -> None:
        """Eliminar todas las imágenes asociadas a un producto"""
