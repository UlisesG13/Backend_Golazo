from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class PedidoItemDTO(BaseModel):
    pedido_item_id: Optional[int]
    pedido_id: Optional[int]
    producto_id: str
    nombre_producto: str
    color_id: int
    talla_id: int
    cantidad: int
    precio_unitario: float
    subtotal: float

    class Config:
        from_attributes = True


class FacturaResponseDTO(BaseModel):
    factura_id: Optional[int]
    pedido_id: int
    folio: str
    uuid_fiscal: Optional[str]
    fecha_emision: datetime
    fecha_vencimiento: Optional[datetime]
    emisor_datos: dict
    receptor_datos: dict
    moneda: str
    subtotal: float
    descuento_total: float
    impuestos_totales: float
    total: float
    estado: str
    metodo_pago: str
    forma_pago: str
    items: List[PedidoItemDTO]

    class Config:
        from_attributes = True


class CreateFacturaRequestDTO(BaseModel):
    pedido_id: int
    datos_fiscales_receptor: dict


class ChangeStatusRequestDTO(BaseModel):
    estado: str
