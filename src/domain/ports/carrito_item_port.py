from abc import ABC, abstractmethod
from src.domain.models.carrito_item_model import CarritoItemModel

class CarritoItemPort(ABC):
    
    @abstractmethod
    def add_item_to_carrito(self, carrito_id: str, item: CarritoItemModel) -> CarritoItemModel:
        """Agrega un ítem al carrito"""
    
    @abstractmethod
    def remove_item_from_carrito(self, carrito_id: str, item_id: str) -> None:
        """Elimina un ítem del carrito por su ID"""

    @abstractmethod
    def update_item_in_carrito(self, carrito_id: str, item_id: str, updated_item: CarritoItemModel) -> CarritoItemModel:
        """Actualiza un ítem existente en el carrito p. ej. color, talla o cantidad"""

    @abstractmethod
    def get_items_by_carrito_id(self, carrito_id: str) -> list[CarritoItemModel]:
        """Obtiene todos los ítems asociados a un carrito específico"""