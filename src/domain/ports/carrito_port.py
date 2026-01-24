from abc import ABC, abstractmethod
from src.domain.models.carrito_model import CarritoModel

class CarritoPort(ABC):
    
    @abstractmethod
    def get_by_user_id(self, user_id: str) -> CarritoModel:
        """Obtiene el carrito del usuario por su ID"""
    
    @abstractmethod
    def create_carrito(self, carrito: CarritoModel) -> CarritoModel:
        """Crea un nuevo carrito"""

    @abstractmethod
    def udate_carrito(self, carrito_id: str, updated_data: CarritoModel) -> CarritoModel:
        """Actualiza un carrito existente"""
    
    @abstractmethod
    def delete_carrito(self, carrito_id: str) -> None:
        """Elimina un carrito por su ID"""
