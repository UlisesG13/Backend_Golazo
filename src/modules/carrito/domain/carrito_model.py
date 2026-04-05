from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class CarritoItemModel:
    carrito_item_id: int | None
    producto_id: str
    color_id: int
    talla_id: int
    cantidad: int
    precio_unitario: float

    @property
    def subtotal(self) -> float:
        return self.cantidad * self.precio_unitario

@dataclass
class CarritoModel:
    carrito_id: str
    usuario_id: str
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    items: List[CarritoItemModel] = field(default_factory=list)

    @property
    def total(self) -> float:
        return sum(item.subtotal for item in self.items)