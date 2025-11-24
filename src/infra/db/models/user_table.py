from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from datetime import datetime
from zoneinfo import ZoneInfo
from src.infra.db.models.rol_enum import Rol
from src.infra.db.database import Base
from sqlalchemy.types import Enum
from sqlalchemy.orm import relationship

class UserTable(Base):
    __tablename__ = "usuario"
    
    usuario_id = Column(String, primary_key=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    telefono = Column(String, nullable=True)
    direccion_id = Column(Integer, ForeignKey("direccion.direccion_id"), nullable=True)
    rol = Column(Enum(Rol), default=Rol.cliente)
    fecha_creacion = Column(
        DateTime(timezone=True), default=lambda: datetime.now(ZoneInfo("America/Mexico_City"))
    )
    
    # direccion = relationship("Direccion", back_populates="usuario")