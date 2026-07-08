from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict

class UserDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    usuario_id: str
    nombre: str
    email: EmailStr
    fecha_creacion: datetime
    telefono: Optional[str] = None
    rol: Optional[str] = None
    fecha_eliminacion: Optional[datetime] = None

class UserUpdateDTO(BaseModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None

class DireccionDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    direccion_id: int  # TODO(L6): change to str to match UUID PK strategy
    calle: str
    colonia: str
    numero_casa: Optional[int] = None
    codigo_postal: str
    usuario_id: str
    is_primary: bool
    # Campos opcionales
    calle_uno: Optional[str] = None
    calle_dos: Optional[str] = None
    referencia: Optional[str] = None

class DireccionRequestDTO(BaseModel):
    calle: str
    colonia: str
    numero_casa: Optional[int] = None
    codigo_postal: str
    is_primary: bool
    # Al poner = None, el frontend puede omitirlos en el JSON
    calle_uno: Optional[str] = None
    calle_dos: Optional[str] = None
    referencia: Optional[str] = None