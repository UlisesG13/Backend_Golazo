from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from src.infra.db.database import Base

class ProductoImagenTable(Base):
    __tablename__ = "producto_imagen"
    
    producto_imagen_id = Column(Integer, primary_key=True, autoincrement=True)
    producto_id = Column(String, ForeignKey("producto.producto_id"), nullable=False)
    imagen_id = Column(Integer, ForeignKey("imagen.imagen_id"), nullable=False)
    es_principal = Column(Boolean, nullable=False)
