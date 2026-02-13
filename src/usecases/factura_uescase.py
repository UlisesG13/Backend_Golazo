from typing import List
from datetime import datetime
import random
from src.domain.ports.factura_port import FacturaPort
from src.api.schemas.factura_dto import FacturaCreateDTO, FacturaUpdateDTO 
from src.domain.models.factura_model import FacturaModel

class FacturaUsecases:
    def __init__(self, repo: FacturaPort):
        self.repo = repo

    def generar_factura(self, data: FacturaCreateDTO) -> FacturaModel:
        now = datetime.now()
        random_id = random.randint(1000, 9999)
        date_str = now.strftime('%Y%m%d')
        folio = f"F-{random_id}-{date_str}" # folio = F-1234-20260213
        total = data.subtotal - data.descuento
        factura_model = FacturaModel(
            factura_id=None,
            pedido_id=data.pedido_id,
            fecha_emision=datetime.now(),
            subtotal=data.subtotal,
            folio=folio,
            descuento=data.descuento,
            total=total
        )
        created_factura = self.repo.create(factura_model)
        return created_factura
    
    def obtener_facturas(self) -> List[FacturaModel]:
        return self.repo.get_all()
    
    def obtener_factura_por_id(self, factura_id: int) -> FacturaModel:
        return self.repo.get_by_id(factura_id)
    
    def obtener_factura_por_folio(self, folio: str) -> FacturaModel:
        return self.repo.get_by_folio(folio)
    
    def actualizar_factura(self, factura_id: int, data: FacturaUpdateDTO) -> FacturaModel:
        existing_factura = self.repo.get_by_id(factura_id)
        total = (data.subtotal if data.subtotal is not None else existing_factura.subtotal) - (data.descuento if data.descuento is not None else existing_factura.descuento)
        updated_factura = FacturaModel(
            factura_id=None,
            pedido_id=data.pedido_id if data.pedido_id is not None else existing_factura.pedido_id,
            fecha_emision=datetime.now(),
            subtotal=data.subtotal if data.subtotal is not None else existing_factura.subtotal,
            folio=data.folio if data.folio is not None else existing_factura.folio,
            descuento=data.descuento if data.descuento is not None else existing_factura.descuento,
            total=total
        )
        return self.repo.update(factura_id, updated_factura)
    
    def eliminar_factura(self, factura_id: int) -> None:
        self.repo.delete(factura_id)