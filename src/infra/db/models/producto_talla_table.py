from sqlalchemy import Column, ForeignKey, Integer, String
from src.infra.db.database import Base

class ProductoTallaTable(Base):
    __tablename__ = "producto_talla"

    producto_talla_id = Column(Integer, primary_key=True, autoincrement=True)
    producto_id = Column(String, ForeignKey("producto.producto_id"), nullable=False)
    talla_id = Column(Integer, ForeignKey("talla.talla_id"), nullable=False)
