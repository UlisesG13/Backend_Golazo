from dataclasses import dataclass
from datetime import datetime

@dataclass
class PedidoModel:
    pedido_id: int
    usuario_id: str
    promocion_id: int
    estado: str 
    fecha_pedido: datetime
    fecha_actualizacion: datetime
    subtotal: float
    descuento: float
    total: float
    notas: str
    direccion: dict
