
from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

class SeccionCreateDTO(BaseModel):
	"""Payload para crear una seccion."""

	nombre: str = Field(..., example="Ropa")

class SeccionDTO(BaseModel):
    """Respuesta para las secciones."""
      
    seccion_id: int
    nombre: str

    class Config:
        from_attributes = True

class SeccionUpdateDTO(BaseModel):
    """Payload para actualizar una seccion (todos campos opcionales)."""

    nombre: Optional[str] = Field(None, example="Ropa")