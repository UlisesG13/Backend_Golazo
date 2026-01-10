from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


class ProductoDTO(BaseModel):
    producto_id: Optional[str] = Field(None, description="ID del producto")
    nombre: str = Field(..., description="Nombre del producto")
    precio: int = Field(..., description="Precio del producto")
    descripcion: Optional[str] = Field(None, description="Descripción del producto")
    esta_activo: bool = Field(..., description="Indica si el producto está activo")
    esta_destacado: bool = Field(..., description="Indica si el producto está destacado")
    categoria_id: int = Field(..., description="ID de la categoría del producto")
    fecha_creacion: datetime = Field(description="Fecha de creación del producto")

    class Config:
        from_attributes = True

class ProductoCreateDTO(BaseModel):
    nombre: str = Field(..., description="Nombre del producto", example="Camiseta de fútbol")
    precio: int = Field(..., description="Precio del producto", example=29.99)
    descripcion: Optional[str] = Field(None, description="Descripción del producto", example="Camiseta oficial del equipo")
    esta_activo: bool = Field(..., description="Indica si el producto está activo", example=True)
    esta_destacado: bool = Field(..., description="Indica si el producto está destacado", example=False)
    categoria_id: int = Field(..., description="ID de la categoría del producto", example=1)

class ProductoUpdateDTO(BaseModel):
    nombre: Optional[str] = Field(None, description="Nombre del producto", example="Camiseta de fútbol")
    precio: Optional[int] = Field(None, description="Precio del producto", example=29.99)
    descripcion: Optional[str] = Field(None, description="Descripción del producto", example="Camiseta oficial del equipo")
    esta_activo: Optional[bool] = Field(None, description="Indica si el producto está activo", example=True)
    esta_destacado: Optional[bool] = Field(None, description="Indica si el producto está destacado", example=False)
    categoria_id: Optional[int] = Field(None, description="ID de la categoría del producto", example=1)

