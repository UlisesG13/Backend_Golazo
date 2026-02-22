from datetime import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class AuthUser:
    usuario_id: str
    nombre: str
    email: str

    rol: str
    fecha_creacion: datetime
    is_authenticated: bool = False

    password: Optional[str] = None
    telefono: Optional[str] = ""
    google_id: Optional[str] = None
    fecha_eliminacion: Optional[datetime] = None

@dataclass
class AuthenticatedUser:
    usuario_id: str
    email: str
    rol: str

@dataclass
class TokenPayload:
    usuario_id: str
    email: str
    rol: str
    exp: datetime

@dataclass
class RecoveryCode:
    id: int | None
    usuario_id: str
    code: str
    expires_at: datetime

    def is_expired(self, now: datetime) -> bool:
        return now > self.expires_at
