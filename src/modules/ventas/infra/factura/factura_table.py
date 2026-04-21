from enum import Enum as PyEnum
from sqlalchemy import Column, ForeignKey, DateTime, String, Integer, Numeric, JSON, Enum
from sqlalchemy.orm import relationship
from src.core.database import Base


class EstadoFactura(PyEnum):
    EMITIDA = "EMITIDA"
    PAGADA = "PAGADA"
    CANCELADA = "CANCELADA"
    REEMBOLSADA = "REEMBOLSADA"


class FacturaTable(Base):
    __tablename__ = "factura"

    factura_id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey("pedido.pedido_id"), nullable=False)

    # Identificación Fiscal
    folio = Column(String, unique=True, nullable=False)
    uuid_fiscal = Column(String, unique=True, nullable=True)

    # Fechas
    fecha_emision = Column(DateTime(timezone=True), nullable=False)
    fecha_vencimiento = Column(DateTime(timezone=True), nullable=True)

    # Entidades (Snapshot de los datos en ese momento)
    emisor_datos = Column(JSON, nullable=False)  # Datos fiscales del emisor (RFC, nombre, etc.)
    receptor_datos = Column(JSON, nullable=False)  # Datos fiscales del receptor (RFC, nombre, etc.)

    # Desglose Económico
    moneda = Column(String(3), default="MXN", nullable=False)
    subtotal = Column(Numeric, nullable=False)
    descuento_total = Column(Numeric, nullable=False, default=0.0)
    impuestos_totales = Column(Numeric, nullable=False, default=0.0)
    total = Column(Numeric, nullable=False)

    # Estado y Control
    estado = Column(Enum(EstadoFactura), default=EstadoFactura.EMITIDA, nullable=False)
    metodo_pago = Column(String(3), default="PUE", nullable=False)  # PUE (una sola exhibición), PPD (parcialidades)
    forma_pago = Column(String(2), default="01", nullable=False)   # 01 (Efectivo), 04 (Tarjeta), etc.

    # Snapshot de items facturados
    # Se guarda como JSON para preservar los precios exactos y descripciones en el momento de la emisión
    items = Column(JSON, nullable=False)

    # Relación con el pedido
    pedido = relationship("PedidoTable")
