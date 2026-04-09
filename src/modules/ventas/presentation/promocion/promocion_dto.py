from datetime import datetime

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
    contador_usos: int
    usos_maximos: int
    fecha_inicio: datetime
    fecha_expiracion: datetime
    esta_activa: bool


class PromocionUpdateDTO(BaseModel):
    codigo: str | None
    descuento: float | None
    tipo_descuento: str | None
    contador_usos: int | None
    usos_maximos: int | None
    fecha_inicio: datetime | None
    fecha_expiracion: datetime | None
    esta_activa: bool | None
