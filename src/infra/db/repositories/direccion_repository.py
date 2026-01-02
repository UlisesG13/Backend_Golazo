from datetime import datetime
from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.models.direccion_model import DireccionModel
from src.domain.ports.direccion_port import DireccionPort
from src.infra.db.models.direccion_table import DireccionTable 
from src.infra.db.models.user_table import UserTable
from src.core.exceptions import NotFoundError

class DireccionRepository(DireccionPort):
    def __init__(self, session: Session):
        self.session = session

    def _to_domain(self, r: DireccionTable) -> DireccionModel:
        return DireccionModel(
            direccion_id=r.direccion_id,
            calle=r.calle,
            colonia=r.colonia,
            calle_uno=r.calle_uno,
            calle_dos=r.calle_dos,
            numero_casa=r.numero_casa,
            codigo_postal=r.codigo_postal,
            referencia=r.referencia,
            usuario_id=r.usuario_id,
            is_primary=r.is_primary
        )
    
    def get_direccion_by_id(self, direccion_id: int) -> Optional[DireccionModel]:
        direccion = self.session.query(DireccionTable).filter_by(direccion_id=direccion_id).first()
        if direccion:
            return self._to_domain(direccion)
        return None
    
    def get_direcciones_by_usuario_id(self, usuario_id: str) -> List[DireccionModel]:
        direcciones = self.session.query(DireccionTable).filter_by(usuario_id=usuario_id).all()
        return [self._to_domain(direccion) for direccion in direcciones]
    
    def create_direccion(self, direccion: DireccionModel) -> DireccionModel:
        new_direccion = DireccionTable(
            calle=direccion.calle,
            colonia=direccion.colonia,
            calle_uno=direccion.calle_uno,
            calle_dos=direccion.calle_dos,
            numero_casa=direccion.numero_casa,
            codigo_postal=direccion.codigo_postal,
            referencia=direccion.referencia,
            usuario_id=direccion.usuario_id,
            is_primary=direccion.is_primary
        )
        self.session.add(new_direccion)
        self.session.commit()
        self.session.refresh(new_direccion) # Para obtener el ID generado
        return self._to_domain(new_direccion)
    
    def update_direccion(self, direccion_id: int, direccion: DireccionModel) -> DireccionModel:
        existing_direccion = self.session.query(DireccionTable).filter_by(direccion_id=direccion_id).first()
        if not existing_direccion:
            raise NotFoundError(f"Dirección con ID {direccion_id} no encontrada.")
        
        existing_direccion.calle = direccion.calle
        existing_direccion.colonia = direccion.colonia
        existing_direccion.calle_uno = direccion.calle_uno
        existing_direccion.calle_dos = direccion.calle_dos
        existing_direccion.numero_casa = direccion.numero_casa
        existing_direccion.codigo_postal = direccion.codigo_postal
        existing_direccion.referencia = direccion.referencia
        existing_direccion.is_primary = direccion.is_primary
        
        self.session.commit()
        return self._to_domain(existing_direccion)
    
    def delete_direccion(self, direccion_id: int) -> None:
        direccion = self.session.query(DireccionTable).filter_by(direccion_id=direccion_id).first()
        if not direccion:
            raise NotFoundError(f"Dirección con ID {direccion_id} no encontrada.")
        
        self.session.delete(direccion)
        self.session.commit()
