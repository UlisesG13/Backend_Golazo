from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.catalogo.domain.models import TallaModel, ProductoTallaModel
from src.modules.catalogo.domain.ports import TallaPort, ProductoTallaPort
from src.modules.catalogo.infra.sizes.talla_table import TallaTable, ProductoTallaTable


def to_domain_talla(r: TallaTable) -> TallaModel:
    return TallaModel(
        talla_id=r.talla_id,
        nombre=r.nombre
    )


class TallaRepository(TallaPort):
    def __init__(self, db_session: AsyncSession):
        self.db = db_session

    async def get_all(self) -> list[TallaModel]:
        stmt = select(TallaTable)
        rows = await self.db.execute(stmt)
        rows = rows.scalars().all()
        return [to_domain_talla(r) for r in rows]

    async def get_by_id(self, talla_id: int) -> TallaModel | None:
        r = await self.db.get_one(TallaTable, talla_id)
        return to_domain_talla(r) if r else None  # type: ignore[arg-type]

    async def create(self, model: TallaModel) -> TallaModel:
        talla = TallaTable(
            nombre=model.nombre
        )
        self.db.add(talla)
        await self.db.commit()
        await self.db.refresh(talla)
        return to_domain_talla(talla)

    async def update(self, talla_id: int, model: TallaModel) -> TallaModel | None:
        r = await self.db.get_one(TallaTable, talla_id)
        if not r:
            return None
        r.nombre = model.nombre
        await self.db.commit()
        await self.db.refresh(r)
        return to_domain_talla(r)  # type: ignore[arg-type]

    async def delete(self, talla_id: int) -> None:
        r = await self.db.get(TallaTable, talla_id)
        await self.db.delete(r)
        await self.db.commit()
        return


def to_domain_p_talla(r: ProductoTallaTable) -> ProductoTallaModel:
    return ProductoTallaModel(
        producto_talla_id=r.producto_talla_id,
        talla_id=r.talla_id,
        producto_id=r.producto_id
    )


class ProductoTallaRepository(ProductoTallaPort):
    def __init__(self, db_session: AsyncSession):
        self.db = db_session

    async def get_all_by_producto(self, p_id: str) -> list[TallaModel]:
        stmt = (
            select(TallaTable)
            .join(ProductoTallaTable, TallaTable.talla_id == ProductoTallaTable.talla_id)
            .where(ProductoTallaTable.producto_id == p_id)
        )
        rows = await self.db.execute(stmt)
        rows = rows.scalars().all()

        return [to_domain_talla(r) for r in rows]

    async def get_by_id(self, p_talla_id: int) -> ProductoTallaModel | None:
        r = await self.db.get(ProductoTallaTable, p_talla_id)
        return to_domain_p_talla(r) if r else None  # type: ignore[arg-type]

    async def assign_to_producto(self, p_talla: ProductoTallaModel) -> ProductoTallaModel:
        assign = ProductoTallaTable(
            producto_id=p_talla.producto_id,
            talla_id=p_talla.talla_id
        )
        self.db.add(assign)
        await self.db.commit()
        await self.db.refresh(assign)
        return to_domain_p_talla(assign)

    async def remove_from_producto(self, producto_id: str, talla_id: int) -> None:
        stmt = (select(ProductoTallaTable)
                .filter(ProductoTallaTable.producto_id == producto_id)
                .filter(ProductoTallaTable.talla_id == talla_id)
                )
        r = await self.db.execute(stmt)
        r = r.scalar_one_or_none()
        await self.db.delete(r)
        await self.db.commit()
        return
