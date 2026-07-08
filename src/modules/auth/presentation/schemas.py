from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict, Field


class UserRegister(BaseModel):
    nombre: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    # Usamos ConfigDict (Estándar de Pydantic V2)
    model_config = ConfigDict(from_attributes=True)

    usuario_id: str
    nombre: str
    email: EmailStr
    fecha_creacion: datetime

    telefono: Optional[str] = None
    rol: Optional[str] = "cliente"
    is_authenticated: bool = False
    google_id: Optional[str] = None
    password: Optional[str] = None
    fecha_eliminacion: Optional[datetime] = None


class LoginResponseDTO(BaseModel):
    token: str
    usuario_id: str
    email: str
    rol: str