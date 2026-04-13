from enum import Enum as PyEnum

from sqlalchemy import Column, ForeignKey, DateTime, String, Integer, Numeric, Text, JSON, Enum
from sqlalchemy.orm import relationship

from src.core.database import Base


class EstadoPedido(PyEnum):
    pendiente = "pendiente"
    procesando = "procesando"
    camino = "camino"
    completado = "completado"
    cancelado = "cancelado"


class PedidoTable(Base):
    __tablename__ = "pedido"

    pedido_id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(String, ForeignKey("usuario.usuario_id"), nullable=False)
    promocion_id = Column(Integer, ForeignKey("promocion.promocion_id"), nullable=True)

    estado = Column(Enum(EstadoPedido), nullable=False)

    fecha_pedido = Column(DateTime(timezone=True), nullable=False)
    fecha_actualizacion = Column(DateTime(timezone=True), nullable=True)

    subtotal = Column(Numeric, nullable=False)
    descuento = Column(Numeric, nullable=False)
    total = Column(Numeric, nullable=False)

    notas = Column(Text, nullable=True)

    # snapshot de dirección (simple)
    direccion = Column(JSON, nullable=False)

    items = relationship(
        "PedidoItemTable",
        back_populates="pedido",
        cascade="all, delete-orphan",
        passive_deletes=True
    )


class PedidoItemTable(Base):
    __tablename__ = "pedido_item"

    pedido_item_id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey("pedido.pedido_id"), nullable=False)

    producto_id = Column(String, ForeignKey("producto.producto_id"), nullable=False)
    nombre_producto = Column(String, nullable=False)

    color_id = Column(Integer, ForeignKey("color.color_id"), nullable=True)
    talla_id = Column(Integer, ForeignKey("talla.talla_id"), nullable=True)

    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Numeric, nullable=False)

    pedido = relationship("PedidoTable", back_populates="items")

    producto = relationship("ProductoTable")
    color = relationship("ColorTable")
    talla = relationship("TallaTable")
