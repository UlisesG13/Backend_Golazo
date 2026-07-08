from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from src.modules.ventas.infra.pedido.pedido_table import EstadoPedido


class CreatePedidoDTO(BaseModel):
    direccion_id: int
    promocion: Optional[str] = None
    notas: Optional[str] = None


class ChangeStatusDTO(BaseModel):
    status: EstadoPedido


class PedidoItemDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    producto_id: str
    nombre_producto: str
    color_id: Optional[int]
    talla_id: Optional[int]
    cantidad: int
    precio_unitario: float
    subtotal: float


class PedidoDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    pedido_id: int
    usuario_id: str
    estado: str
    fecha_pedido: datetime
    subtotal: float
    descuento: float
    total: float
    direccion: dict
    items: list[PedidoItemDTO]
    notas: Optional[str]
