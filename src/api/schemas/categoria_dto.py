
from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

class CategoriaCreateDTO(BaseModel):
    """Payload para crear una categoria."""
    nombre: str = Field(..., example="Camisas")
    seccion_id: int = Field(..., example=1)

class CategoriaDTO(BaseModel):
    """Respuesta para las categorias."""
    categoria_id: int
    nombre: str
    seccion_id: int
    class Config:
        from_attributes = True

class CategoriaUpdateDTO(BaseModel):
    """Payload para actualizar una categoria (todos campos opcionales)."""

    nombre: Optional[str] = Field(None, example="Ropa")
    seccion_id: Optional[int] = Field(None, example=1)
