from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional, List

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