from pydantic import BaseModel

class ProductoTallaCreateDTO(BaseModel):
    """Payload para enlazar una talla con un producto."""
    producto_id: str
    talla_id: int

class ProductoTallaDTO(BaseModel):
    """Respuesta del enlazado de talla con producto."""
    producto_talla_id: int
    producto_id: str
    talla_id: int
    class Config:
        from_attributes = True
