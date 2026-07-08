from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

from src.modules.catalogo.presentation.images.images_dto import ImagenDTO
from src.modules.catalogo.presentation.sizes.talla_dto import TallaDTO
from src.modules.catalogo.presentation.colors.color_dto import ColorDTO


class ProductoDTO(BaseModel):
    # Usamos ConfigDict para Pydantic V2 (es lo más moderno)
    model_config = ConfigDict(from_attributes=True)

    producto_id: Optional[str] = None
    nombre: str
    precio: int
    descripcion: Optional[str] = None
    esta_activo: bool
    esta_destacado: bool
    stock: int = 0
    categoria_id: Optional[int] = None
    fecha_creacion: datetime
    imagenes: list[ImagenDTO] = []
    tallas: list[TallaDTO] =  []
    colores: list[ColorDTO] = []

class ProductoCreateDTO(BaseModel):
    nombre: str
    precio: int
    descripcion: Optional[str] = None
    esta_activo: bool
    esta_destacado: bool
    stock: int = 0
    categoria_id: int

class ProductoUpdateDTO(BaseModel):
    # En un Update, all suele ser opcional porque puedes actualizar solo un campo
    nombre: Optional[str] = None
    precio: Optional[int] = None
    descripcion: Optional[str] = None
    esta_activo: Optional[bool] = None
    esta_destacado: Optional[bool] = None
    stock: Optional[int] = None
    categoria_id: Optional[int] = None