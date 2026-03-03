from src.modules.usuarios.domain.models import DireccionModel
from src.modules.usuarios.infra.tables import DireccionTable
from src.modules.usuarios.domain.ports import DireccionPort
from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy import select, update

def _to_domain(r: DireccionTable) -> DireccionModel:
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

class DireccionRepository(DireccionPort):
    def __init__(self, session: Session):
        self.db = session

    def get_direcciones_by_usuario_id(self, usuario_id: str) -> List[DireccionModel]:
        stmt = select(DireccionTable).where(DireccionTable.usuario_id == usuario_id)
        rows = self.db.execute(stmt).scalars().all()
        return [_to_domain(r) for r in rows]

    def get_direccion_by_id(self, direccion_id: int, usuario_id: str) -> Optional[DireccionModel]:
        stmt = (
            select(DireccionTable)
            .where(
                DireccionTable.direccion_id == direccion_id,
                DireccionTable.usuario_id == usuario_id
            )
        )
        r = self.db.execute(stmt).scalar_one_or_none()
        return _to_domain(r) if r else None

    def create_direccion(self, direccion: DireccionModel) -> DireccionModel:
        model = DireccionTable(
            direccion_id=0,
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
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return _to_domain(model)

    def update_direccion(self, direccion_id: int, direccion: DireccionModel, usuario_id: str) -> Optional[DireccionModel]:

        stmt = select(DireccionTable).where(
            DireccionTable.direccion_id == direccion_id,
            DireccionTable.usuario_id == usuario_id
        )

        entity = self.db.execute(stmt).scalar_one_or_none()

        if not entity:
            return None

        entity.calle = direccion.calle
        entity.colonia = direccion.colonia
        entity.calle_uno = direccion.calle_uno
        entity.calle_dos = direccion.calle_dos
        entity.numero_casa = direccion.numero_casa
        entity.codigo_postal = direccion.codigo_postal
        entity.referencia = direccion.referencia
        entity.is_primary = direccion.is_primary

        self.db.commit()
        self.db.refresh(entity)

        return _to_domain(entity)

    def delete_direccion(self, direccion_id: int, usuario_id: str) -> None:
        stmt = select(DireccionTable).where(
            DireccionTable.direccion_id == direccion_id,
            DireccionTable.usuario_id == usuario_id
        )
        model = self.db.execute(stmt).scalar_one_or_none()
        if model:
            self.db.delete(model)
            self.db.commit()
        return

    def set_primary(self, direccion_id: int, usuario_id: str) -> None:

        stmt = select(DireccionTable).where(
            DireccionTable.direccion_id == direccion_id,
            DireccionTable.usuario_id == usuario_id
        )

        direccion = self.db.execute(stmt).scalar_one_or_none()

        if not direccion:
            return None

        stmt_reset = (
            update(DireccionTable)
            .where(DireccionTable.usuario_id == usuario_id)
            .values(is_primary=False)
        )
        self.db.execute(stmt_reset)

        stmt_set = (
            update(DireccionTable)
            .where(
                DireccionTable.direccion_id == direccion_id,
                DireccionTable.usuario_id == usuario_id
            )
            .values(is_primary=True)
        )
        self.db.execute(stmt_set)
        return self.db.commit()