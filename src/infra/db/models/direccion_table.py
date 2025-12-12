from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from datetime import datetime
from zoneinfo import ZoneInfo
from src.infra.db.models.rol_enum import Rol
from src.infra.db.database import Base
from sqlalchemy.types import Enum
from sqlalchemy.orm import relationship

class DireccionTable(Base):
    __tablename__ = "direccion"
    
    direccion_id = Column(Integer, primary_key=True, autoincrement=True)
    calle = Column(String, nullable=False)
    colonia = Column(String, nullable=False)
    calle_unon = Column(String, nullable=True)
    calle_dos = Column(String, nullable=True)
    numero_casa = Column(Integer, nullable=True)
    codigo_postal = Column(String, nullable=True)
    referencia = Column(String, nullable=True)

    usuario = relationship("UserTable", back_populates="direccion")
