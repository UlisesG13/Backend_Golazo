from abc import ABC, abstractmethod
from typing import List
from src.domain.models.color_model import ColorModel

class ColorPort(ABC):
    @abstractmethod
    def create_color(self, color: ColorModel) -> ColorModel:
        """Crea un nuevo color"""

    @abstractmethod
    def get_color_by_id(self, color_id: int) -> ColorModel:
        """Obtiene un color por su ID"""

    @abstractmethod
    def get_all_colors(self) -> List[ColorModel]:
        """Obtiene todos los colores"""

    @abstractmethod
    def update_color(self, color_id: int, color: ColorModel) -> ColorModel:
        """Actualiza un color existente"""

    @abstractmethod
    def delete_color(self, color_id: int) -> bool:
        """Elimina un color por su ID"""