from sqlalchemy import Column, ForeignKey, Integer, String, Numeric
from src.core.database import Base
from sqlalchemy.orm import relationship

class CarritoItemTable(Base):
    __tablename__ = "carrito_item"

    carrito_item_id = Column(Integer, primary_key=True, autoincrement=True)
    carrito_id = Column(String, ForeignKey("carrito.carrito_id"), nullable=False)
    producto_id = Column(String, ForeignKey("producto.producto_id"), nullable=False)
    color_id = Column(Integer, ForeignKey("color.color_id"), nullable=True)
    talla_id = Column(Integer, ForeignKey("talla.talla_id"), nullable=True)

    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Numeric, nullable=False)

    carrito = relationship("CarritoTable", back_populates="items")
    producto = relationship("ProductoTable")
    color = relationship("ColorTable")
    talla = relationship("TallaTable")