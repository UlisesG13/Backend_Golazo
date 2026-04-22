from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, ConfigDict


class AddItemRequest(BaseModel):
    """Lo que el cliente envía para agregar un producto"""
    producto_id: str
    color_id: int
    talla_id: int
    cantidad: int = Field(gt=0, description="La cantidad debe ser mayor a 0")


class UpdateItemQuantityRequest(BaseModel):
    """Si solo quieres actualizar la cantidad de un ítem específico"""
    cantidad: int = Field(gt=0)


class CarritoItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    """Representación de un ítem para el frontend"""
    carrito_item_id: int
    producto_id: str
    color_id: int
    talla_id: int
    cantidad: int
    precio_unitario: float
    subtotal: float


class CarritoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    """Representación completa del carrito"""
    carrito_id: str
    usuario_id: str
    items: List[CarritoItemResponse]
    total: float
    fecha_actualizacion: datetime
