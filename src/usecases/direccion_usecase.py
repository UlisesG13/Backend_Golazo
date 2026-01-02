from typing import List
from src.domain.ports.direccion_port import DireccionPort
from src.api.schemas.direccion_dto import DireccionDTO, DireccionCreateDTO, DireccionUpdateDTO
from src.domain.models.direccion_model import DireccionModel

class DireccionUsecases:
    def __init__(self, repo: DireccionPort):
        self.repo = repo

    def get_direcciones(self, usuario_id: str) -> list[DireccionModel]:
        return self.repo.get_direcciones_by_usuario_id(usuario_id)
    
    def get_direccion(self, direccion_id: int) -> DireccionModel:
        direccion = self.repo.get_direccion_by_id(direccion_id)
        if not direccion:
            raise ValueError(f"Dirección con ID {direccion_id} no encontrada")
        return direccion
    
    def create_direccion(self, usuario_id: str, dto: DireccionCreateDTO) -> DireccionModel:
        direccion = DireccionModel(
            direccion_id=0,  # Será asignado por la base de datos
            calle=dto.calle,
            colonia=dto.colonia,
            calle_uno=dto.calle_uno,
            calle_dos=dto.calle_dos,
            numero_casa=dto.numero_casa,
            codigo_postal=dto.codigo_postal,
            referencia=dto.referencia,
            usuario_id=usuario_id,
            is_primary=dto.is_primary
        )
        return self.repo.create_direccion(direccion)
    
    def update_direccion(self, direccion_id: int, dto: DireccionUpdateDTO) -> DireccionModel:
        existing_direccion = self.repo.get_direccion_by_id(direccion_id)
        if not existing_direccion:
            raise ValueError(f"Dirección con ID {direccion_id} no encontrada")
        
        updated_direccion = DireccionModel(
            direccion_id=direccion_id,
            calle=dto.calle if dto.calle is not None else existing_direccion.calle,
            colonia=dto.colonia if dto.colonia is not None else existing_direccion.colonia,
            calle_uno=dto.calle_uno if dto.calle_uno is not None else existing_direccion.calle_uno,
            calle_dos=dto.calle_dos if dto.calle_dos is not None else existing_direccion.calle_dos,
            numero_casa=dto.numero_casa if dto.numero_casa is not None else existing_direccion.numero_casa,
            codigo_postal=dto.codigo_postal if dto.codigo_postal is not None else existing_direccion.codigo_postal,
            referencia=dto.referencia if dto.referencia is not None else existing_direccion.referencia,
            usuario_id=existing_direccion.usuario_id,
            is_primary=dto.is_primary if dto.is_primary is not None else existing_direccion.is_primary
        )
        return self.repo.update_direccion(direccion_id, updated_direccion)
    
    def delete_direccion(self, direccion_id: int) -> None:
        direccion = self.repo.get_direccion_by_id(direccion_id)
        if not direccion:
            raise ValueError(f"Dirección con ID {direccion_id} no encontrada")
        self.repo.delete_direccion(direccion_id)

    def set_primary_direccion(self, usuario_id: str, direccion_id: int) -> None:
        direcciones = self.repo.get_direcciones_by_usuario_id(usuario_id)
        if not any(d.direccion_id == direccion_id for d in direcciones):
            raise ValueError(f"La dirección con ID {direccion_id} no pertenece al usuario {usuario_id}")
        
        for direccion in direcciones:
            if direccion.direccion_id == direccion_id:
                direccion.is_primary = True
            else:
                direccion.is_primary = False
            self.repo.update_direccion(direccion.direccion_id, direccion)