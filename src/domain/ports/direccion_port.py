from abc import ABC, abstractmethod
from typing import Optional, List
from src.domain.models.direccion_model import DireccionModel

class DireccionPort(ABC):

    @abstractmethod
    def get_direccion_by_id(self, direccion_id: int) -> Optional[DireccionModel]:
        """Obtiene una dirección por su ID."""

    @abstractmethod
    def get_direcciones_by_usuario_id(self, usuario_id: str) -> List[DireccionModel]:
        """Obtiene una dirección por el ID del usuario."""

    @abstractmethod
    def create_direccion(self, direccion: DireccionModel) -> DireccionModel:
        """Crea una nueva dirección."""

    @abstractmethod
    def update_direccion(self, direccion_id: int, direccion: DireccionModel) -> DireccionModel:
        """Actualiza una dirección existente."""

    @abstractmethod
    def delete_direccion(self, direccion_id: int) -> None:
        """Elimina una dirección por su ID."""
