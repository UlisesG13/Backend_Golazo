from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from src.core.database import Base


class ImagenTable(Base):
    __tablename__ = "imagen"

    imagen_id = Column(Integer, primary_key=True, autoincrement=True)
    path = Column(String, nullable=False)
    orden = Column(Integer, nullable=False)


class ProductoImagenTable(Base):
    __tablename__ = "producto_imagen"

    producto_imagen_id = Column(Integer, primary_key=True, autoincrement=True)
    producto_id = Column(String, ForeignKey("producto.producto_id"), nullable=False)
    imagen_id = Column(Integer, ForeignKey("imagen.imagen_id"), nullable=False)
    es_principal = Column(Boolean, nullable=False)
