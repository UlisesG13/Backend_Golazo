from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional, List
from .imagen_model import ImagenModel

@dataclass
class ProductoModel:
    producto_id: str
    nombre: str
    precio: int
    esta_activo: bool
    esta_destacado: bool
    fecha_creacion: datetime

    imagenes: List[ImagenModel] = field(default_factory=list)

    descripcion: Optional[str] = None
    categoria_id: Optional[int] = None