from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    nombre: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    usuario_id: str
    nombre: str
    email: EmailStr
    telefono: Optional[str]
    rol: Optional[str]
    fecha_creacion: datetime
    is_authenticated: bool | None = False
    google_id: Optional[str] | None = None
    password: Optional[str] | None = None
    fecha_eliminacion: Optional[datetime] | None = None

    class Config:
        from_attributes = True

class LoginResponseDTO(BaseModel):
    token: str
    usuario_id: str
    email: str
    rol: str