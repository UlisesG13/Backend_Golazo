from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    usuario_id: str
    nombre: str
    email: str
    password: str
    telefono: str | None
    direccion_id: int | None
    rol: str
    fecha_creacion: datetime