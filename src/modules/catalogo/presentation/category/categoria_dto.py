from pydantic import BaseModel, ConfigDict


class CategoriaDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    categoria_id: int
    name: str
    seccion_id: int


class CategoriaCreate(BaseModel):
    name: str
    seccion_id: int


class CategoriaUpdate(BaseModel):
    name: str
    seccion_id: int
