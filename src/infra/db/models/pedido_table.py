from sqlalchemy import Column, Float, ForeignKey, Integer, String, DateTime, JSON
from src.core.database import Base
from sqlalchemy.types import Enum
from src.infra.db.models.estado_pedido_enum import EstadoPedido

class PedidoTable(Base):
    __tablename__ = "pedido"
    
    pedido_id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(String, ForeignKey("usuario.usuario_id"), nullable=False)
    promocion_id = Column(Integer, ForeignKey("promocion.promocion_id"), nullable=True)
    estado = Column(Enum(EstadoPedido), default= EstadoPedido.pendiente, nullable=False)
    fecha_pedido = Column(DateTime(timezone=False), nullable=False)
    fecha_actualizacion = Column(DateTime(timezone=False), nullable=False)
    subtotal = Column(Float, nullable=False)
    descuento = Column(Float, nullable=True)
    total = Column(Float, nullable=False)    
    notas = Column(String, nullable=True)
    direccion = Column(JSON, nullable=False)