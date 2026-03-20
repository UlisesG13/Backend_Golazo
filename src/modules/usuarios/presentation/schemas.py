from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict

class UserDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    usuario_id: str
    nombre: str
    email: EmailStr
    fecha_creacion: datetime
    # Sintaxis moderna | None
    telefono: str | None = None
    rol: str | None = None
    fecha_eliminacion: datetime | None = None

class UserUpdateDTO(BaseModel):
    nombre: str | None = None
    telefono: str | None = None

class DireccionDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    direccion_id: int
    calle: str
    colonia: str
    numero_casa: int
    codigo_postal: str
    usuario_id: str
    is_primary: bool
    # Campos opcionales
    calle_uno: str | None = None
    calle_dos: str | None = None
    referencia: str | None = None

class DireccionRequestDTO(BaseModel):
    calle: str
    colonia: str
    numero_casa: int
    codigo_postal: str
    is_primary: bool
    # Al poner = None, el frontend puede omitirlos en el JSON
    calle_uno: str | None = None
    calle_dos: str | None = None
    referencia: str | None = None