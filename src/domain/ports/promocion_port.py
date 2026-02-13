from abc import ABC, abstractmethod
from src.domain.models.promocion_model import PromocionModel

class PromocionPort(ABC):
    @abstractmethod
    def create(self, promocion: PromocionModel) -> PromocionModel:
        """Crear una nueva promoción."""

    @abstractmethod
    def get_all(self) -> list[PromocionModel]:
        """Obtener todas las promociones."""

    @abstractmethod
    def get_by_id(self, promocion_id: int) -> PromocionModel:
        """Obtener una promoción por su ID."""
    
    @abstractmethod
    def delete(self, promocion_id: int) -> None:
        """Eliminar una promoción por su ID."""

    @abstractmethod
    def update(self, promocion_id: int, updated_data: PromocionModel) -> PromocionModel:
        """Actualizar una promoción por su ID."""

    @abstractmethod
    def activar(self, promocion_id: int) -> PromocionModel:
        """Activa una promoción por su ID."""

    @abstractmethod
    def desactivar(self, promocion_id: int) -> PromocionModel:
        """Desactiva una promoción por su ID."""