from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from src.infra.db.database import Base

class FacturaTable(Base):
    __tablename__ = "factura"
    
    factura_id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey("pedido.pedido_id"), nullable=False)
    folio = Column(String, nullable=False)
    fecha_emision = Column(DateTime(timezone=False), nullable=False)
    subtotal = Column(Float, nullable=False)
    descuento = Column(Float, nullable=False) # puede ser 0
    total = Column(Float, nullable=False)