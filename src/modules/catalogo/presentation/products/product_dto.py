from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class ProductoDTO(BaseModel):
    producto_id: Optional[str]
    nombre: str
    precio: int
    descripcion: Optional[str]
    esta_activo: bool
    esta_destacado: bool
    categoria_id: int
    fecha_creacion: datetime

    class Config:
        from_attributes = True

class ProductoCreateDTO(BaseModel):
    nombre: str
    precio: int
    descripcion: Optional[str]
    esta_activo: bool
    esta_destacado: bool
    categoria_id: int

class ProductoUpdateDTO(BaseModel):
    nombre: Optional[str]
    precio: Optional[int]
    descripcion: Optional[str]
    esta_activo: Optional[bool]
    esta_destacado: Optional[bool]
    categoria_id: Optional[int]

