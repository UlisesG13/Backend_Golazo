from sqlalchemy import Column, String, DateTime, Boolean, Integer, ForeignKey
from src.core.database import Base
from sqlalchemy.types import Enum
from enum import Enum as PyEnum

class Rol(PyEnum):
    cliente = "cliente"
    administrador = "administrador"

class UserTable(Base):
    __tablename__ = "usuario"
    
    usuario_id = Column(String, primary_key=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=True)
    telefono = Column(String, nullable=True)
    rol = Column(Enum(Rol), default=Rol.cliente)
    fecha_creacion = Column(DateTime(timezone=True))
    is_authenticated = Column(Boolean, default=False)
    google_id = Column(String, unique=True, nullable=True)
    fecha_eliminacion = Column(DateTime(timezone=True), nullable=True)


class DireccionTable(Base):
    __tablename__ = "direccion"

    direccion_id = Column(Integer, primary_key=True, autoincrement=True)
    calle = Column(String, nullable=False)
    colonia = Column(String, nullable=False)
    calle_uno = Column(String, nullable=True)
    calle_dos = Column(String, nullable=True)
    numero_casa = Column(Integer, nullable=True)
    codigo_postal = Column(String, nullable=True)
    referencia = Column(String, nullable=True)
    usuario_id = Column(String, ForeignKey("usuario.usuario_id"), nullable=False)
    is_primary = Column(Boolean, default=False)


class DeviceTokenTable(Base):
    __tablename__ = "device_tokens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey('usuario.usuario_id'), nullable=False)
    token = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False)