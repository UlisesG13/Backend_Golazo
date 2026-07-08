from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.modules.catalogo.domain.ports import ProductImagePort
from src.modules.catalogo.domain.models import ProductoImagenModel
from src.modules.catalogo.infra.images.db.image_table import ProductoImagenTable


def _to_domain(r: ProductoImagenTable) -> ProductoImagenModel:
    return ProductoImagenModel(
        producto_imagen_id=r.producto_imagen_id,
        producto_id=r.producto_id,
        imagen_id=r.imagen_id,
        es_principal=r.es_principal
    )

class ProductImageRepository(ProductImagePort):
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create(self, r: ProductoImagenModel) -> ProductoImagenModel:
        nueva_asociacion = ProductoImagenTable(
            producto_id=r.producto_id,
            imagen_id=r.imagen_id,
            es_principal=r.es_principal
        )
        self.db_session.add(nueva_asociacion)
        await self.db_session.commit()
        await self.db_session.refresh(nueva_asociacion)
        return _to_domain(nueva_asociacion)

    async def delete(self, producto_id: str, imagen_id: int) -> None:
        stmt = select(ProductoImagenTable).filter_by(
            producto_id=producto_id,
            imagen_id=imagen_id
        )
        r = await self.db_session.execute(stmt)
        r = r.scalars().first()
        if r is None:
            return
        await self.db_session.delete(r)
        await self.db_session.commit()

    async def get_by_producto(self, producto_id: str) -> list[ProductoImagenModel]:
        stmt = select(ProductoImagenTable).filter_by(producto_id=producto_id)
        rows = await self.db_session.execute(stmt)
        rows = rows.scalars()
        return [_to_domain(r) for r in rows]

    async def delete_by_producto(self, producto_id: str) -> None:
        stmt = select(ProductoImagenTable).filter_by(producto_id=producto_id)
        rows = await self.db_session.execute(stmt)
        rows = rows.scalars()
        for r in rows:
            await self.db_session.delete(r)
        await self.db_session.commit()
