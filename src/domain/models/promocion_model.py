from dataclasses import dataclass
from datetime import datetime

@dataclass
class PromocionModel:
    promocion_id: int
    codigo: str
    descuento: float
    tipo_descuento: str
    contador_usos: int
    usos_maximos: int
    fecha_inicio: datetime
    fecha_expiracion: datetime
    esta_activa: bool