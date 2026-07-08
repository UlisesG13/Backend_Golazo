from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from src.modules.catalogo.domain.models import CategoriaModel
from src.modules.catalogo.domain.ports.categoria_port import CategoriaPort
from src.modules.catalogo.infra.category.category_table import CategoriaTable
from src.modules.catalogo.infra.sections.seccion_table import SeccionTable


def to_domain(r: CategoriaTable) -> CategoriaModel:
    return CategoriaModel(
        categoria_id=r.categoria_id,
        nombre=r.nombre,
        seccion_id=r.seccion_id,
        nombre_seccion=r.seccion.nombre if r.seccion else None
    )


class CategoriaRepository(CategoriaPort):
    def __init__(self, db_session: AsyncSession):
        self.db = db_session

    async def get_by_id(self, categoria_id: int) -> CategoriaModel | None:
        stmt = select(CategoriaTable).options(joinedload(CategoriaTable.seccion)).filter_by(categoria_id=categoria_id)
        r = await self.db.execute(stmt)
        r = r.scalars().first()
        return to_domain(r) if r else None

    async def get_all(self) -> list[CategoriaModel]:
        stmt = select(CategoriaTable).options(joinedload(CategoriaTable.seccion)).order_by(CategoriaTable.nombre)
        results = await self.db.execute(stmt)
        results = results.scalars().all()
        return [to_domain(r) for r in results]

    async def get_all_by_seccion(self, seccion: int) -> list[CategoriaModel]:
        stmt = select(CategoriaTable).options(joinedload(CategoriaTable.seccion)).filter_by(seccion_id=seccion)
        results = await self.db.execute(stmt)
        results = results.scalars().all()
        return [to_domain(r) for r in results]

    async def create(self, categoria: CategoriaModel) -> CategoriaModel:
        nueva_categoria = CategoriaTable(
            nombre=categoria.nombre,
            seccion_id=categoria.seccion_id
        )
        self.db.add(nueva_categoria)
        await self.db.commit()
        await self.db.refresh(nueva_categoria)
        # Re-fetch to get the section name
        return await self.get_by_id(nueva_categoria.categoria_id)  # type: ignore[return-value]

    async def update(self, categoria_id: int, categoria: CategoriaModel) -> CategoriaModel | None:
        categoria_db = await self.db.get(CategoriaTable, categoria_id)
        if not categoria_db:
            return None

        categoria_db.nombre = categoria.nombre
        categoria_db.seccion_id = categoria.seccion_id

        await self.db.commit()
        await self.db.refresh(categoria_db)
        return await self.get_by_id(categoria_id)

    async def delete(self, categoria_id: int) -> None:
        stmt = select(CategoriaTable).filter_by(categoria_id=categoria_id)
        r = await self.db.execute(stmt)
        r = r.scalars().first()
        if r:
            await self.db.delete(r)
            await self.db.commit()
