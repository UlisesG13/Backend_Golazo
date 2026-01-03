from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.models.seccion_model import SeccionModel
from src.domain.ports.seccion_port import SeccionPort
from src.infra.db.models.seccion_table import SeccionTable 
from src.core.exceptions import NotFoundError

class SeccionRepository(SeccionPort):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def _to_domain(self, r: SeccionTable) -> SeccionModel:
        return SeccionModel(
            seccion_id=r.seccion_id,
            nombre=r.nombre
        )
    
    def get_seccion_by_id(self, seccion_id: int) -> Optional[SeccionModel]:
        seccion = self.db_session.query(SeccionTable).filter(SeccionTable.seccion_id == seccion_id).first()
        if seccion:
            return self._to_domain(seccion)
        return None
    
    def get_secciones(self) -> List[SeccionModel]:
        secciones = self.db_session.query(SeccionTable).all()
        return [self._to_domain(seccion) for seccion in secciones]
    
    def create_seccion(self, seccion: SeccionModel) -> SeccionModel:
        new_seccion = SeccionTable(
            nombre=seccion.nombre
        )
        self.db_session.add(new_seccion)
        self.db_session.commit()
        self.db_session.refresh(new_seccion)
        return self._to_domain(new_seccion)
    
    def update_seccion(self, seccion_id: int, seccion: SeccionModel) -> SeccionModel:
        existing_seccion = self.db_session.query(SeccionTable).filter(SeccionTable.seccion_id == seccion_id).first()
        if not existing_seccion:
            raise NotFoundError(f"Sección con ID {seccion_id} no encontrada.")
        
        existing_seccion.nombre = seccion.nombre
        self.db_session.commit()
        self.db_session.refresh(existing_seccion)
        return self._to_domain(existing_seccion)
    
    def delete_seccion(self, seccion_id: int) -> None:
        seccion = self.db_session.query(SeccionTable).filter(SeccionTable.seccion_id == seccion_id).first()
        if not seccion:
            raise NotFoundError(f"Sección con ID {seccion_id} no encontrada.")
        
        self.db_session.delete(seccion)
        self.db_session.commit()