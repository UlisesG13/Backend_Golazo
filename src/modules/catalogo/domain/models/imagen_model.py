from dataclasses import dataclass
from typing import Optional

@dataclass
class ImagenModel:
    imagen_id: Optional[int]
    path: str
    orden: int

@dataclass
class ProductoImagenModel:
    producto_imagen_id: Optional[int]
    producto_id: str
    imagen_id: int
    es_principal: bool
