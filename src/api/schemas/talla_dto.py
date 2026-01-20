from typing import Optional
from pydantic import BaseModel, Field

class TallaCreateDTO(BaseModel):
    """Payload para crear una talla."""
    nombre: str = Field(..., example="M")

class TallaDTO(BaseModel):
    """Respuesta para las tallas."""
    talla_id: int
    nombre: str
    class Config:
        from_attributes = True

class TallaUpdateDTO(BaseModel):
    """Payload para actualizar una talla"""

    nombre: Optional[str] = Field(None, example="L")