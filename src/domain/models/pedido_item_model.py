from dataclasses import dataclass

@dataclass
class PedidoItemModel:
    pedido_item_id: int
    pedido_id: int
    producto_id: str
    color_id: int
    talla_id: int
    cantidad: int