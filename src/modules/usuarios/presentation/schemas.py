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
