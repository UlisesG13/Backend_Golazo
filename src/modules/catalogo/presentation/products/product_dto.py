from datetime import datetime
from pydantic import BaseModel, ConfigDict
from src.modules.catalogo.presentation.images.images_dto import ImagenDTO

class ProductoDTO(BaseModel):
    # Usamos ConfigDict para Pydantic V2 (es lo más moderno)
    model_config = ConfigDict(from_attributes=True)

    producto_id: str | None = None
    nombre: str
    precio: int
    descripcion: str | None = None
    esta_activo: bool
    esta_destacado: bool
    categoria_id: int
    fecha_creacion: datetime
    imagenes: list[ImagenDTO] = []

class ProductoCreateDTO(BaseModel):
    nombre: str
    precio: int
    descripcion: str | None = None
    esta_activo: bool
    esta_destacado: bool
    categoria_id: int

class ProductoUpdateDTO(BaseModel):
    # En un Update, todo suele ser opcional porque puedes actualizar solo un campo
    nombre: str | None = None
    precio: int | None = None
    descripcion: str | None = None
    esta_activo: bool | None = None
    esta_destacado: bool | None = None
    categoria_id: int | None = None