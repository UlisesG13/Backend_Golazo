from src.domain.ports.pedido_item_port import PedidoItemPort
from src.api.schemas.pedido_item_dto import PedidoItemCreateDto
from src.domain.models.pedido_item_model import PedidoItemModel
from src.domain.ports.pedido_item_port import PedidoItemModel

class PedidoItemUsecases:
    def __init__(self, repo: PedidoItemPort):
        self.repo = repo

    def add_item_to_pedido(self, item_data: PedidoItemCreateDto) -> PedidoItemModel:
        new_item = PedidoItemModel(
            pedido_item_id=None,
            pedido_id=item_data.pedido_id,
            producto_id=item_data.producto_id,
            color_id=item_data.color_id,
            talla_id=item_data.talla_id,
            cantidad=item_data.cantidad
        )
        return self.repo.add(new_item)
    
    def get_items(self, pedido_id: int) -> list[PedidoItemModel]:
        return self.repo.list_items(pedido_id)
    
    def remove_item_from_pedido(self, pedido_item_id: int) -> None:
        return self.repo.remove(pedido_item_id)
    