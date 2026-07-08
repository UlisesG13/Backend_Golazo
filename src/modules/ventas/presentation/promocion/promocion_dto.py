from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class PromocionDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    promocion_id: int
    codigo: str
    descuento: float
    tipo_descuento: str
    contador_usos: int
    usos_maximos: int
    fecha_inicio: datetime
    fecha_expiracion: datetime
    esta_activa: bool


class PromocionCreateDTO(BaseModel):
    codigo: str
    descuento: float
    tipo_descuento: str
    usos_maximos: int
    fecha_inicio: datetime
    fecha_expiracion: datetime
    esta_activa: bool


class PromocionUpdateDTO(BaseModel):
    codigo: Optional[str]
    descuento: Optional[float]
    tipo_descuento: Optional[str]
    contador_usos: Optional[int]
    usos_maximos: Optional[int]
    fecha_inicio: Optional[datetime]
    fecha_expiracion: Optional[datetime]
    esta_activa: Optional[bool]
