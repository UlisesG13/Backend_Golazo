from dataclasses import dataclass

@dataclass
class ProductoColorModel:
    producto_color_id: int
    producto_id: str
    color_id: int