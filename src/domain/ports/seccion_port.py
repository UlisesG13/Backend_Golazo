from abc import ABC, abstractmethod
from typing import Optional, List
from src.domain.models.seccion_model import SeccionModel

class SeccionPort(ABC):
    @abstractmethod
    def get_seccion_by_id(self, seccion_id: int) -> Optional[SeccionModel]:
        """Obtiene una sección por su ID."""

    @abstractmethod
    def get_secciones(self) -> List[SeccionModel]:
        """Obtiene todas las secciones."""
        
    @abstractmethod
    def create_seccion(self, seccion: SeccionModel) -> SeccionModel:
        """Crea una nueva sección."""

    @abstractmethod
    def update_seccion(self, seccion_id: int, seccion: SeccionModel) -> SeccionModel:
        """Actualiza una sección existente."""

    @abstractmethod
    def delete_seccion(self, seccion_id: int) -> None:
        """Elimina una sección por su ID."""