from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class FacturaModel:
    factura_id: Optional[int]
    pedido_id: int
    folio: str
    fecha_emision: datetime
    subtotal: float
    descuento: float
    total: float