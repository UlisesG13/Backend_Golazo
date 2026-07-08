from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.catalogo.domain.models import SeccionModel
from src.modules.catalogo.domain.ports import SeccionPort
from src.modules.catalogo.infra.sections.seccion_table import SeccionTable


def _to_domain(r: SeccionTable) -> SeccionModel:
    return SeccionModel(
        seccion_id=r.seccion_id,
        nombre=r.nombre,
    )

class SeccionRepository(SeccionPort):
    def __init__(self, session: AsyncSession):
        self.db = session

    async def get_seccion_by_id(self, seccion_id: int) -> SeccionModel | None:
        r = await self.db.get(SeccionTable, seccion_id)
        return _to_domain(r) if r else None # type: ignore[arg-type]

    async def get_secciones(self) -> list[SeccionModel]:
        stmt = select(SeccionTable).order_by(SeccionTable.nombre)
        results = await self.db.execute(stmt)
        results = results.scalars().all()
        return [_to_domain(r) for r in results]

    async def create_seccion(self, seccion: SeccionModel) -> SeccionModel:
        new_seccion = SeccionTable(nombre=seccion.nombre)
        self.db.add(new_seccion)
        await self.db.commit()
        await self.db.refresh(new_seccion)
        return _to_domain(new_seccion)

    async def update_seccion(self, seccion_id: int, seccion: SeccionModel) -> SeccionModel | None:
        db_seccion = await self.db.get(SeccionTable, seccion_id)
        if not db_seccion:
            return None
        db_seccion.nombre = seccion.nombre
        await self.db.commit()
        await self.db.refresh(db_seccion)
        return _to_domain(db_seccion) # type: ignore[arg-type]

    async def delete_seccion(self, seccion_id: int) -> None:
        db_seccion = await self.db.get(SeccionTable, seccion_id)

        if db_seccion:
            await self.db.delete(db_seccion)
            await self.db.commit()
