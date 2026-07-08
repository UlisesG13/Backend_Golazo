from typing import Optional
from pydantic import BaseModel, ConfigDict


class ColorDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    color_id: int
    nombre: str


class ColorCreateDTO(BaseModel):
    nombre: str


class ColorUpdateDTO(BaseModel):
    nombre: Optional[str]


class ProductoColorCreateDTO(BaseModel):
    producto_id: str
    color_id: int


class ProductoColorDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    producto_color_id: int
    producto_id: str
    color_id: int
