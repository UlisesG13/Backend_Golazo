from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.models.talla_model import TallaModel
from src.domain.ports.talla_port import TallaPort
from src.infra.db.models.talla_table import TallaTable
from src.core.exceptions import NotFoundError

class TallaRepository(TallaPort):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def _to_domain(self, r: TallaTable) -> TallaModel:
        return TallaModel(
            talla_id=r.talla_id,
            nombre=r.nombre,
        )

    def create_talla(self, talla: TallaModel) -> TallaModel:
        db_talla = TallaTable(
            nombre=talla.nombre,
        )
        self.db_session.add(db_talla)
        self.db_session.commit()
        self.db_session.refresh(db_talla)
        return self._to_domain(db_talla)

    def get_talla_by_id(self, talla_id: int) -> TallaModel:
        db_talla = self.db_session.query(TallaTable).filter(TallaTable.talla_id == talla_id).first()
        if not db_talla:
            raise NotFoundError(f"Talla con ID {talla_id} no encontrado")
        return self._to_domain(db_talla)

    def get_all_tallas(self) -> List[TallaModel]:
        db_tallas = self.db_session.query(TallaTable).all()
        return [self._to_domain(r) for r in db_tallas]

    def update_talla(self, talla_id: int, talla: TallaModel) -> TallaModel:
        db_talla = self.db_session.query(TallaTable).filter(TallaTable.talla_id == talla_id).first()
        if not db_talla:
            raise NotFoundError(f"Talla con ID {talla_id} no encontrado")
        db_talla.nombre = talla.nombre
        self.db_session.commit()
        self.db_session.refresh(db_talla)
        return self._to_domain(db_talla)

    def delete_talla(self, talla_id: int) -> bool:
        db_talla = self.db_session.query(TallaTable).filter(TallaTable.talla_id == talla_id).first()
        if not db_talla:
            raise NotFoundError(f"Talla con ID {talla_id} no encontrado")
        self.db_session.delete(db_talla)
        self.db_session.commit()
        return True