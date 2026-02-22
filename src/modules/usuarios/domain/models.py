from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class UserModel:
    usuario_id: str
    nombre: str
    email: str

    rol: str
    fecha_creacion: datetime
    telefono: Optional[str] = None
    fecha_eliminacion: Optional[datetime] = None