from enum import Enum as PyEnum
from sqlalchemy import Column, Float, Integer, String, DateTime, Boolean
from sqlalchemy.types import Enum
from src.core.database import Base

class TipoDescuento(PyEnum):
    PORCENTAJE = "PORCENTAJE"
    FIJO = "FIJO"

class PromocionTable(Base):
    __tablename__ = "promocion"

    promocion_id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(50), nullable=False, unique=True, index=True)
    descuento = Column(Float, nullable=False)
    tipo_descuento = Column(Enum(TipoDescuento), nullable=False)
    contador_usos = Column(Integer, default=0, nullable=False)
    usos_maximos = Column(Integer, nullable=False)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_expiracion = Column(DateTime, nullable=False)
    esta_activa = Column(Boolean, default=True, nullable=False)