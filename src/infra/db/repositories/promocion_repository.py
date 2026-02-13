from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.models.promocion_model import PromocionModel
from src.domain.ports.promocion_port import PromocionPort
from src.infra.db.models.promocion_table import PromocionTable
from src.core.exceptions import NotFoundError

class PromocionRepository(PromocionPort):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def _to_domain(self, r: PromocionTable) -> PromocionModel:
        return PromocionModel(
            promocion_id = r.promocion_id,
            codigo=r.codigo,
            descuento=r.descuento,
            tipo_descuento=r.tipo_descuento,
            contador_usos=r.contador_usos,
            usos_maximos=r.usos_maximos,
            fecha_inicio=r.fecha_inicio,
            fecha_expiracion=r.fecha_expiracion,
            esta_activa=r.esta_activa
        )
    
    def create(self, promocion: PromocionModel) -> PromocionModel:
        new_promocion = PromocionTable(
            codigo=promocion.codigo,
            descuento=promocion.descuento,
            tipo_descuento=promocion.tipo_descuento,
            contador_usos=promocion.contador_usos,
            usos_maximos=promocion.usos_maximos,
            fecha_inicio=promocion.fecha_inicio,
            fecha_expiracion=promocion.fecha_expiracion,
            esta_activa=promocion.esta_activa
        )
        self.db_session.add(new_promocion)
        self.db_session.commit()
        self.db_session.refresh(new_promocion)
        return self._to_domain(new_promocion)
    
    def get_all(self) -> list[PromocionModel]:
        promociones = self.db_session.query(PromocionTable).all()
        return [self._to_domain(p) for p in promociones]
    
    def get_by_id(self, promocion_id: int) -> PromocionModel:
        promocion = self.db_session.query(PromocionTable).filter_by(promocion_id=promocion_id).first()
        if not promocion:
            raise NotFoundError(f"Promoción con ID {promocion_id} no encontrada.")
        return self._to_domain(promocion)
    
    def delete(self, promocion_id: int) -> None:
        promocion = self.db_session.query(PromocionTable).filter_by(promocion_id=promocion_id).first()
        if not promocion:
            raise NotFoundError(f"Promoción con ID {promocion_id} no encontrada.")
        self.db_session.delete(promocion)
        self.db_session.commit()

    def update(self, promocion_id: int, updated_data: PromocionModel) -> PromocionModel:
        promocion = self.db_session.query(PromocionTable).filter_by(promocion_id=promocion_id).first()
        if not promocion:
            raise NotFoundError(f"Promoción con ID {promocion_id} no encontrada.")
        
        promocion.codigo = updated_data.codigo
        promocion.descuento = updated_data.descuento
        promocion.tipo_descuento = updated_data.tipo_descuento
        promocion.contador_usos = updated_data.contador_usos
        promocion.usos_maximos = updated_data.usos_maximos
        promocion.fecha_inicio = updated_data.fecha_inicio
        promocion.fecha_expiracion = updated_data.fecha_expiracion
        promocion.esta_activa = updated_data.esta_activa

        self.db_session.commit()
        self.db_session.refresh(promocion)
        return self._to_domain(promocion)
    
    def activar(self, promocion_id: int) -> PromocionModel:
        promocion = self.db_session.query(PromocionTable).filter_by(promocion_id=promocion_id).first()
        if not promocion:
            raise NotFoundError(f"Promoción con ID {promocion_id} no encontrada.")
        
        promocion.esta_activa = True
        self.db_session.commit()
        self.db_session.refresh(promocion)
        return self._to_domain(promocion)
    
    def desactivar(self, promocion_id: int) -> PromocionModel:
        promocion = self.db_session.query(PromocionTable).filter_by(promocion_id=promocion_id).first()
        if not promocion:
            raise NotFoundError(f"Promoción con ID {promocion_id} no encontrada.")
        
        promocion.esta_activa = False
        self.db_session.commit()
        self.db_session.refresh(promocion)
        return self._to_domain(promocion)