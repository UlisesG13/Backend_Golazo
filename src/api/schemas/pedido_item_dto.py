from pydantic import BaseModel, Field


class PedidoItemCreateDto(BaseModel):
    pedido_id: int = Field(..., example=1)
    producto_id: str = Field(..., example="PROD12345")
    color_id: int = Field(..., example=1)
    talla_id: int = Field(..., example=1)
    cantidad: int = Field(..., example=2)

class PedidoItemDto(BaseModel):
    id: int = Field(..., example=1)
    pedido_id: int = Field(..., example=1)
    producto_id: str = Field(..., example="PROD12345")
    color_id: int = Field(..., example=1)
    talla_id: int = Field(..., example=1)
    cantidad: int = Field(..., example=2)

    class Config:
        orm_mode = True
