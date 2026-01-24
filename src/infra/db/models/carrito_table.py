from sqlalchemy import Column, ForeignKey, DateTime, String
from src.infra.db.database import Base

class CarritoTable(Base):
    __tablename__ = "carrito"

    carrito_id  = Column(String, primary_key=True, autoincrement=True)
    usuario_id = Column(String, ForeignKey("usuario.usuario_id"), nullable=False)
    fecha_creacion = Column(DateTime(timezone=True), nullable=False)
    fecha_actualizacion = Column(DateTime(timezone=True), nullable=True)