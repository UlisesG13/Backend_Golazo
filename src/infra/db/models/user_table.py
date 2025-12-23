from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
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
    password = Column(String, nullable=True)
    telefono = Column(String, nullable=True)
    direccion_id = Column(Integer, ForeignKey("direccion.direccion_id"), nullable=True)
    rol = Column(Enum(Rol), default=Rol.cliente)
    fecha_creacion = Column(DateTime(timezone=True))
    is_authenticated = Column(Boolean, default=False)
    google_id = Column(String, unique=True, nullable=True)
    fecha_eliminacion = Column(DateTime(timezone=True), nullable=True)

    direccion = relationship("DireccionTable", back_populates="usuario")