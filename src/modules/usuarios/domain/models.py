from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserModel:
    usuario_id: str
    nombre: str
    email: str

    rol: str
    fecha_creacion: datetime
    telefono: str | None = None
    fecha_eliminacion: datetime | None = None

@dataclass
class DireccionModel:
    direccion_id: int | None
    calle: str
    colonia: str
    calle_uno: str | None
    calle_dos: str | None
    numero_casa: int | None
    codigo_postal: str | None
    referencia: str | None
    usuario_id: str
    is_primary: bool