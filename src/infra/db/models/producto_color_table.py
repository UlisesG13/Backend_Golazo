from sqlalchemy import Column, ForeignKey, Integer, String
from src.infra.db.database import Base

class ProductoColorTable(Base):
    __tablename__ = "producto_color"

    producto_color_id = Column(Integer, primary_key=True, autoincrement=True)
    producto_id = Column(String, ForeignKey("producto.producto_id"), nullable=False)
    color_id = Column(Integer, ForeignKey("color.color_id"), nullable=False)
