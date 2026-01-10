from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class ProductoModel:
    producto_id: str
    nombre: str
    precio: int 
    esta_activo: bool
    esta_destacado: bool
    fecha_creacion: datetime = field(default_factory=datetime.now)

    descripcion: Optional[str] = None
    categoria_id: Optional[int] = None
