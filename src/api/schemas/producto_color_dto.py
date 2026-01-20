from pydantic import BaseModel

class ProductoColorCreateDTO(BaseModel):
    """Payload para enlazar un color con un producto."""
    producto_id: str
    color_id: int

class ProductoColorDTO(BaseModel):
    """Respuesta del enlazado de color con producto."""
    producto_color_id: int
    producto_id: str
    color_id: int
    class Config:
        from_attributes = True
