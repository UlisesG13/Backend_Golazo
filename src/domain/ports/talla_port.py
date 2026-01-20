from abc import ABC, abstractmethod
from typing import List
from src.domain.models.color_model import ColorModel

class TallaPort(ABC):
    @abstractmethod
    def create_talla(self, talla: ColorModel) -> ColorModel:
        """Crea una nueva talla"""

    @abstractmethod
    def get_talla_by_id(self, talla_id: int) -> ColorModel:
        """Obtiene una talla por su ID"""

    @abstractmethod
    def get_all_tallas(self) -> List[ColorModel]:
        """Obtiene todas las tallas"""

    @abstractmethod
    def update_talla(self, talla_id: int, talla: ColorModel) -> ColorModel:
        """Actualiza una talla existente"""

    @abstractmethod
    def delete_talla(self, talla_id: int) -> bool:
        """Elimina una talla por su ID"""