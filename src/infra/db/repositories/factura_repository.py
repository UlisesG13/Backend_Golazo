from datetime import datetime
from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.models.factura_model import FacturaModel
from src.domain.ports.factura_port import FacturaPort
from src.infra.db.models.factura_table import FacturaTable
from src.core.exceptions import NotFoundError

class FacturaRepository(FacturaPort):
    def __init__(self, session: Session):
        self.session = session

    def __to_domain(self, r: FacturaTable) -> FacturaModel:
        return FacturaModel(
            factura_id=r.factura_id,
            pedido_id=r.pedido_id,
            folio=r.folio,
            fecha_emision=r.fecha_emision,
            subtotal=r.subtotal,
            descuento=r.descuento,
            total=r.total,
        )

    def create(self, factura: FacturaModel) -> FacturaModel:
        new_factura = FacturaTable(
            pedido_id=factura.pedido_id,
            folio=factura.folio,
            fecha_emision=factura.fecha_emision,
            subtotal=factura.subtotal,
            descuento=factura.descuento,
            total=factura.total,
        )
        self.session.add(new_factura)
        self.session.commit()
        self.session.refresh(new_factura)
        return self.__to_domain(new_factura)
    
    def get_all(self) -> list[FacturaModel]:
        facturas = self.session.query(FacturaTable).all()
        return [self.__to_domain(f) for f in facturas]
    
    def get_by_id(self, factura_id: int) -> FacturaModel:
        factura = self.session.query(FacturaTable).filter_by(factura_id=factura_id).first()
        if not factura:
            raise NotFoundError(f"Factura con ID {factura_id} no encontrada.")
        return self.__to_domain(factura)
    
    def get_by_folio(self, folio: str) -> FacturaModel:
        factura = self.session.query(FacturaTable).filter_by(folio=folio).first()
        if not factura:
            raise NotFoundError(f"Factura con folio {folio} no encontrada.")
        return self.__to_domain(factura)
    
    def update(self, factura_id: int, factura: FacturaModel) -> FacturaModel:
        existing_factura = self.session.query(FacturaTable).filter_by(factura_id=factura_id).first()
        if not existing_factura:
            raise NotFoundError(f"Factura con ID {factura_id} no encontrada.")
        
        existing_factura.pedido_id = factura.pedido_id
        existing_factura.folio = factura.folio
        existing_factura.fecha_emision = factura.fecha_emision
        existing_factura.subtotal = factura.subtotal
        existing_factura.descuento = factura.descuento
        existing_factura.total = factura.total
        
        self.session.commit()
        return self.__to_domain(existing_factura)
    
    def delete(self, factura_id: int) -> None:
        factura = self.session.query(FacturaTable).filter_by(factura_id=factura_id).first()
        if not factura:
            raise NotFoundError(f"Factura con ID {factura_id} no encontrada.")
        self.session.delete(factura)
        self.session.commit()