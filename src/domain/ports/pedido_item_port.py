from abc import ABC, abstractmethod
from src.domain.models.pedido_item_model import PedidoItemModel

class PedidoItemPort(ABC):
    @abstractmethod
    def add(self, item: PedidoItemModel) -> PedidoItemModel:
        """Agrega un producto al pedido con la cantidad especificada."""

    @abstractmethod
    def remove(self, item_id: int) -> None:
        """Elimina un producto del pedido."""

    @abstractmethod
    def update(self, item_id: int, item: PedidoItemModel) -> PedidoItemModel:
        """Actualiza un item del pedido"""

    @abstractmethod
    def list_items(self, pedido_id: int) -> list[PedidoItemModel]:
        """Lista todos los productos en el pedido."""