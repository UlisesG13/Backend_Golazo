from abc import ABC, abstractmethod
from typing import Optional, List
from src.domain.models.categoria_model import CategoriaModel

class CategoriaPort(ABC):
    @abstractmethod
    def get_categoria_by_id(self, categoria_id: int) -> Optional[CategoriaModel]:
        """Obtiene una categoría por su ID."""

    @abstractmethod
    def get_categorias(self) -> List[CategoriaModel]:
        """Obtiene todas las categorías."""

    @abstractmethod
    def get_categorias_by_seccion(self, seccion_id: int) -> List[CategoriaModel]:
        """Obtiene categorías por ID de sección."""
        
    @abstractmethod
    def create_categoria(self, categoria: CategoriaModel) -> CategoriaModel:
        """Crea una nueva categoría."""

    @abstractmethod
    def update_categoria(self, categoria_id: int, categoria: CategoriaModel) -> CategoriaModel:
        """Actualiza una categoría existente."""

    @abstractmethod
    def delete_categoria(self, categoria_id: int) -> None:
        """Elimina una categoría por su ID."""