from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserDTO(BaseModel):
    usuario_id: str
    nombre: str
    email: EmailStr
    telefono: Optional[str]
    rol: Optional[str]
    fecha_creacion: datetime
    fecha_eliminacion: Optional[datetime]

    class Config:
        from_attributes = True
        
class UserUpdateDTO(BaseModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None

class DireccionDTO(BaseModel):
    direccion_id: int
    calle: str
    colonia: str
    calle_uno: Optional[str]
    calle_dos: Optional[str]
    numero_casa: int
    codigo_postal: str
    referencia: Optional[str]
    usuario_id: str
    is_primary: bool

    class Config:
        from_attributes = True

class DireccionRequestDTO(BaseModel):
    calle: str
    colonia: str
    calle_uno: Optional[str]
    calle_dos: Optional[str]
    numero_casa: int
    codigo_postal: str
    referencia: Optional[str]
    is_primary: bool
