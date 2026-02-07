from sqlalchemy import Column, Float, ForeignKey, Integer, String, DateTime, JSON
from src.infra.db.database import Base
from sqlalchemy.types import Enum
from src.infra.db.models.tipo_descuento_enum import TipoDescuento

class PromocionTable(Base):
    __tablename__ = "promocion"

    promocion_id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String, nullable=False, unique=True)
    descuento = Column(Float, nullable=False)
    tipo_descuento = Column(Enum(TipoDescuento), nullable=False)
    contador_usos = Column(Integer, default=0)
    usos_maximos = Column(Integer, nullable=False)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_expiracion = Column(DateTime, nullable=False)
    esta_activa = Column(Integer, nullable=False)
