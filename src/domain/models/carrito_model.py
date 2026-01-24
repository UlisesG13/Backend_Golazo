from dataclasses import dataclass,field
from datetime import datetime

@dataclass
class CarritoModel:
    carrito_id: str
    usuario_id: str
    fecha_creacion: datetime = field(default_factory=datetime.now)
    fecha_actualizacion: datetime = field(default_factory=datetime.now)