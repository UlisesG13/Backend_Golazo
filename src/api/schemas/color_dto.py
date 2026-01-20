from typing import Optional
from pydantic import BaseModel, Field

class ColorCreateDTO(BaseModel):
    """Payload para crear un color."""
    nombre: str = Field(..., example="Rojo")

class ColorDTO(BaseModel):
    """Respuesta para los colores."""
    color_id: int
    nombre: str
    class Config:
        from_attributes = True

class ColorUpdateDTO(BaseModel):
    """Payload para actualizar un color"""

    nombre: Optional[str] = Field(None, example="Verde")
