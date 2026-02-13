from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

class PromocionDTO(BaseModel):
    """Representación pública de una promoción para respuestas API."""

    promocion_id: int
    codigo: str
    descuento: float
    tipo_descuento: str
    contador_usos: int
    usos_maximos: int
    fecha_inicio: datetime
    fecha_expiracion: datetime
    esta_activa: bool
    
    class Config:
        from_attributes = True

class PromocionCreateDTO(BaseModel):
    """Payload para crear una promoción."""

    codigo: str = Field(..., example="PROMO123")
    descuento: float = Field(..., example=10.0)
    tipo_descuento: str = Field(..., example="porcentaje")
    contador_usos: int = Field(..., example=0)
    usos_maximos: int = Field(..., example=100)
    fecha_inicio: datetime = Field(..., example="2024-01-01T00:00:00")
    fecha_expiracion: datetime = Field(..., example="2024-12-31T23:59:59")
    esta_activa: bool = Field(..., example=True)

class PromocionUpdateDTO(BaseModel):
    """Payload para actualizar una promoción (todos campos opcionales)."""

    codigo: Optional[str] = Field(None, example="PROMO123")
    descuento: Optional[float] = Field(None, example=10.0)
    tipo_descuento: Optional[str] = Field(None, example="porcentaje")
    contador_usos: Optional[int] = Field(None, example=0)
    usos_maximos: Optional[int] = Field(None, example=100)
    fecha_inicio: Optional[datetime] = Field(None, example="2024-01-01T00:00:00")
    fecha_expiracion: Optional[datetime] = Field(None, example="2024-12-31T23:59:59")
    esta_activa: Optional[bool] = Field(None, example=True)
