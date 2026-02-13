from abc import ABC, abstractmethod
from src.domain.models.factura_model import FacturaModel

class FacturaPort(ABC):

    @abstractmethod
    def create(self, factura: FacturaModel) -> FacturaModel:
        """Crea una nueva factura en el sistema."""

    @abstractmethod
    def get_all(self) -> list[FacturaModel]:
        """Obtiene todas las facturas registradas en el sistema."""

    @abstractmethod
    def get_by_id(self, factura_id: int) -> FacturaModel:
        """Obtiene una factura por su ID."""

    @abstractmethod
    def get_by_folio(self, folio: str) -> FacturaModel:
        """Obtiene una factura por su folio."""

    @abstractmethod
    def update(self, factura_id: int, factura: FacturaModel) -> FacturaModel:
        """Actualiza una factura existente en el sistema."""

    @abstractmethod
    def delete(self, factura_id: int) -> None:
        """Elimina una factura del sistema por su ID."""