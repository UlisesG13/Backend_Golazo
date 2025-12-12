from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

@dataclass
class UserModel:
    usuario_id: str
    nombre: str
    email: str

    rol: str = "cliente"
    fecha_creacion: datetime = field(default_factory=datetime.now)
    is_authenticated: bool = False

    password: Optional[str] = None
    telefono: Optional[str] = ""
    direccion_id: Optional[int] = None
    google_id: Optional[str] = None
