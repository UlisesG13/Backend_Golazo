from abc import ABC, abstractmethod
from src.domain.models.pedido_model import PedidoModel

class PedidoPort(ABC):

    @abstractmethod
    def get_by_user_id(self, user_id: str) -> list[PedidoModel]:
        """Obtiene los pedidos del usuario"""

    @abstractmethod
    def get_all(self) -> list[PedidoModel]:
        """Obtiene todos los pedidos"""

    @abstractmethod
    def get_by_id(self, pedido_id: int) -> PedidoModel:
        """Obtiene un pedido por su ID"""

    @abstractmethod
    def create(self, pedido: PedidoModel) -> PedidoModel:
        """Crea un nuevo pedido"""

    @abstractmethod
    def delete(self, pedido_id: int) -> None:
        """Elimina un pedido por su ID / Cancelar pedido"""

    @abstractmethod
    def update(self, pedido_id: int, updated_data: PedidoModel) -> PedidoModel:
        """Actualiza un pedido existente"""
    