from __future__ import annotations

from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

class DireccionDTO(BaseModel):
    """Representación pública de una dirección para respuestas API."""

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

class DireccionCreateDTO(BaseModel):
    """Payload para crear una dirección."""

    calle: str = Field(..., example="Calle Principal")
    colonia: str = Field(..., example="Springfield")
    calle_uno: Optional[str] = Field(None, example="Calle Falsa 123")
    calle_dos: Optional[str] = Field(None, example="Calle Verdadera 456")
    numero_casa: int = Field(..., example=742)
    codigo_postal: str = Field(..., example="12345")
    referencia: Optional[str] = Field(None, example="Cerca del parque")
    is_primary: bool = Field(False, example=True)

class DireccionUpdateDTO(BaseModel):
    """Payload para actualizar una dirección (todos campos opcionales)."""

    calle: Optional[str] = Field(None, example="Calle Principal")
    colonia: Optional[str] = Field(None, example="Springfield")
    calle_uno: Optional[str] = Field(None, example="Calle Falsa 123")
    calle_dos: Optional[str] = Field(None, example="Calle Verdadera 456")
    numero_casa: Optional[int] = Field(None, example=742)
    codigo_postal: Optional[str] = Field(None, example="12345")
    referencia: Optional[str] = Field(None, example="Cerca del parque")
    is_primary: Optional[bool] = Field(None, example=True)