from sqlalchemy import Column, ForeignKey, Integer, String
from src.infra.db.database import Base


class PedidoItemTable(Base):
    __tablename__ = "pedido_item"

    pedido_item_id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey("pedido.pedido_id"), nullable=False)
    producto_id = Column(String, ForeignKey("producto.producto_id"), nullable=False)
    color_id = Column(Integer, ForeignKey("color.color_id"), nullable=False)
    talla_id = Column(Integer, ForeignKey("talla.talla_id"), nullable=False)
    cantidad = Column(Integer, nullable=False)
