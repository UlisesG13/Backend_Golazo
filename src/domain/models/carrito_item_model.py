from dataclasses import dataclass,field

@dataclass
class CarritoItemModel:
    carrito_item_id: int
    carrito_id: str
    producto_id: str
    color_id: int
    talla_id: int
    cantidad: int
    precio_unitario: float
