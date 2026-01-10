from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from src.infra.db.database import Base

class ProductoTable(Base):
    __tablename__ = "productos"

    producto_id = Column(String, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    precio = Column(Integer, nullable=False)
    esta_activo = Column(Boolean, default=True)
    esta_destacado = Column(Boolean, default=False)
    fecha_creacion = Column(DateTime, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categoria.categoria_id"), nullable=True)
