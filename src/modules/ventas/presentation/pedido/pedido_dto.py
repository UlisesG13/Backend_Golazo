from datetime import datetime

from pydantic import BaseModel, ConfigDict

from src.modules.ventas.infra.pedido.pedido_table import EstadoPedido


class CreatePedidoDTO(BaseModel):
    direccion_id: int
    promocion: str | None = None
    notas: str | None = None


class ChangeStatusDTO(BaseModel):
    status: EstadoPedido


class PedidoItemDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    producto_id: str
    nombre_producto: str
    color_id: int | None
    talla_id: int | None
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
    notas: str | None
