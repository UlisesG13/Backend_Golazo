from typing import Optional
from pydantic import BaseModel, Field
from fastapi import Form

class ImagenCreateDTO(BaseModel):
    """Payload para crear una imagen."""
    orden: int = Field(..., example=1)

    @classmethod
    def as_form(cls, orden: int = Form(...)):
        return cls(orden=orden)

class ImagenDTO(BaseModel):
    """Respuesta para las imagenes."""
    imagen_id: int
    path: str
    orden: int

    class Config:
        from_attributes = True

class ProductoImagenCreateDTO(BaseModel):
    """Payload para asociar una imagen a un producto."""
    producto_id: str = Field(..., example="PROD12345")
    imagen_id: int = Field(..., example=1)
    es_principal: Optional[bool] = Field(False, example=True)

class ProductoImagenDTO(BaseModel):
    """Respuesta para las imagenes asociadas a un producto."""
    producto_imagen_id: int
    producto_id: str
    imagen_id: int
    es_principal: bool

    class Config:
        from_attributes = True
