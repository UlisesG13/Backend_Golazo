from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class PedidoDto(BaseModel):
    pedido_id: int = Field(None, example=1)
    usuario_id: str = Field(..., example="USER12345")
    promocion_id: Optional[int] = Field(None, example=1)
    estado: str = Field(None, example="pendiente")
    fecha_pedido: datetime = Field(None, example="2024-01-01T12:00:00Z")
    fecha_actualizacion: datetime = Field(None, example="2024-01-01T12:00:00Z")
    subtotal: float = Field(None, example=100.0)
    descuento: Optional[float] = Field(None, example=10.0)
    total: Optional[float] = Field(None, example=90.0)
    notas: str = Field(None, example="Entregar en la puerta")
    direccion: dict = Field(None, example={"calle": "123 Main St", "ciudad": "Ciudad", "codigo_postal": "12345"})

    class Config:
        from_attributes = True

class PedidoCreateDto(BaseModel):
    usuario_id: str = Field(..., example="USER12345")
    promocion_id: Optional[int] = Field(None, example=1)
    notas: str = Field(None, example="Entregar en la puerta")
    direccion: dict = Field(None, example={"calle": "123 Main St", "ciudad": "Ciudad", "codigo_postal": "12345"})

class PedidoUpdateDto(BaseModel):
    promocion_id: Optional[int] = Field(None, example=1)
    estado: Optional[str] = Field(None, example="pendiente")
    notas: Optional[str] = Field(None, example="Entregar en la puerta")
    direccion: Optional[dict] = Field(None, example={"calle": "123 Main St", "ciudad": "Ciudad", "codigo_postal": "12345"})
