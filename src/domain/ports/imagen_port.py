from abc import ABC, abstractmethod
from typing import Optional
from src.domain.models.imagen_model import ImagenModel

class ImagenPort(ABC):

    @abstractmethod
    def create(self, imagen: ImagenModel) -> ImagenModel:
        """Subir la imagen a supabase y guardar la referencia en la base de datos."""

    @abstractmethod
    def get_by_id(self, imagen_id: int) -> ImagenModel | None:
        """obtener imagen por id"""

    @abstractmethod
    def delete(self, imagen_id: int) -> None:
        """Eliminar la imagen de supabase y la referencia en la base de datos."""

    