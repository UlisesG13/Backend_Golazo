from typing import Optional
from pydantic import BaseModel, Field

class CarritoItemDTO(BaseModel):
    """Respuesta para los items del carrito."""
    carrito_item_id: int
    carrito_id: str
    producto_id: str
    color_id: int
    talla_id: int
    cantidad: int
    precio_unitario: float

    class Config:
        from_attributes = True

class CarritoItemCreateDTO(BaseModel):
    """Payload para crear un item en el carrito."""
    producto_id: str = Field(..., example="prod-123")
    carrito_id: str = Field(..., example="carrito-123")
    color_id: int = Field(..., example=1)
    talla_id: int = Field(..., example=1)
    cantidad: int = Field(..., example=2)
    precio_unitario: float = Field(..., example=29.99)

class CarritoItemUpdateDTO(BaseModel):
    """Payload para actualizar un item en el carrito (todos campos opcionales)."""
    producto_id: Optional[str] = Field(None, example="prod-123")
    color_id: Optional[int] = Field(None, example=1)
    talla_id: Optional[int] = Field(None, example=1)
    cantidad: Optional[int] = Field(None, example=2)
    precio_unitario: Optional[float] = Field(None, example=29.99)