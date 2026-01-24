from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

class CreateCarritoDTO(BaseModel):
    """Payload para crear un carrito."""
    usuario_id: str = Field(..., example="user123")

class UpdateCarritoDTO(BaseModel):
    """Payload para actualizar un carrito (todos campos opcionales)."""
    usuario_id: Optional[str] = Field(None, example="user123")

class CarritoDTO(BaseModel):
    """Payload para obtener un carrito."""
    carrito_id: str = Field(..., example="carrito456")
    usuario_id: str = Field(..., example="user123")
    fecha_creacion: datetime = Field(..., example="2023-10-01T12:00:00Z")
    fecha_actualizacion: Optional[datetime] = Field(..., example="2023-10-01T12:00:00Z")