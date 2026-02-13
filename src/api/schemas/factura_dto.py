from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

class FacturaDTO(BaseModel):
    """Representación pública de una factura para respuestas API."""

    factura_id: int
    pedido_id: int
    fecha_emision: datetime
    subtotal: float
    folio: str
    descuento: float
    total: float
    
    class Config:
        from_attributes = True

class FacturaCreateDTO(BaseModel):
    """Payload para crear una factura."""

    pedido_id: int = Field(..., example=1)
    subtotal: float = Field(..., example=1500.50)
    descuento: float = Field(..., example=0.0)

class FacturaUpdateDTO(BaseModel):
    """Payload para actualizar una factura (todos campos opcionales)."""

    pedido_id: Optional[int] = Field(None, example=1)
    subtotal: Optional[float] = Field(None, example=1500.50)
    folio: Optional[str] = Field(None, example="F123456")
    descuento: Optional[float] = Field(None, example=0.0)
