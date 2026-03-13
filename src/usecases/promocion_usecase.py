from typing import List
from datetime import datetime
from src.domain.ports.promocion_port import PromocionPort
from src.api.schemas.promocion_dto import PromocionCreateDTO, PromocionUpdateDTO
from src.domain.models.promocion_model import PromocionModel
# get_all get_by_id delete update activar desactivar
class PromocionUsecases:
    def __init__(self, repo: PromocionPort):
        self.repo = repo

    def create_promocion(self, data: PromocionCreateDTO) -> PromocionModel:
        promocion = PromocionModel(
            promocion_id=None,
            codigo=data.codigo,
            descuento=data.descuento,
            tipo_descuento=data.tipo_descuento,
            contador_usos=0,
            usos_maximos=data.usos_maximos,
            fecha_inicio=data.fecha_inicio, # el usuario elige la fecha de inicio, no se asigna automáticamente
            fecha_expiracion=data.fecha_expiracion,
            esta_activa=False  # Por defecto, la promoción se crea como inactiva
        )
        return self.repo.create(promocion)
    
    def get_all_promociones(self) -> List[PromocionModel]:
        return self.repo.get_all()
    
    def get_by_id(self, id: int) -> PromocionModel:
        return self.repo.get_by_id(id)
    
    def remove_promocion(self, id:int) -> None:
        return self.repo.delete(id)
    
    def update_promocion(self, id: int, data: PromocionUpdateDTO) -> PromocionModel:
        existing_promocion = self.repo.get_by_id(id)
        updated_promocion = PromocionModel(
            promocion_id=None,
            codigo=data.codigo or existing_promocion.codigo,
            descuento=data.descuento if data.descuento is not None else existing_promocion.descuento,
            tipo_descuento=data.tipo_descuento or existing_promocion.tipo_descuento,
            contador_usos=existing_promocion.contador_usos,  # No se actualiza el contador de usos aquí
            usos_maximos=data.usos_maximos if data.usos_maximos is not None else existing_promocion.usos_maximos,
            fecha_inicio=data.fecha_inicio or existing_promocion.fecha_inicio,
            fecha_expiracion=data.fecha_expiracion or existing_promocion.fecha_expiracion,
            esta_activa=existing_promocion.esta_activa  # No se cambia el estado de activación aquí
        )
        return self.repo.update(id, updated_promocion)
    
    def activar_promocion(self, id: int) -> PromocionModel:
        return self.repo.activar(id)
    
    def desactivar_promocion(self, id: int) -> PromocionModel:
        return self.repo.desactivar(id)

    def delete(self, promocion_id: int) -> None:
        return self.repo.delete(promocion_id)