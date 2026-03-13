from datetime import datetime
from dataclasses import dataclass
from typing import Optional

@dataclass
class ProductoModel:
    producto_id: str
    nombre: str
    precio: int
    esta_activo: bool
    esta_destacado: bool
    fecha_creacion: datetime

    descripcion: Optional[str] = None
    categoria_id: Optional[int] = None

@dataclass
class ImagenModel:
    imagen_id: int
    path: str
    orden: int