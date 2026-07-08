from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import subqueryload

from src.modules.catalogo.domain.models import ProductoModel, ImagenModel, TallaModel, ColorModel
from src.modules.catalogo.domain.ports import ProductoPort
from src.modules.catalogo.infra.products.product_table import ProductoTable


def _to_domain(r: ProductoTable) -> ProductoModel:
    return ProductoModel(
        producto_id=r.producto_id,
        nombre=r.nombre,
        precio=r.precio,
        descripcion=r.descripcion,
        esta_activo=r.esta_activo,
        esta_destacado=r.esta_destacado,
        stock=r.stock,
        categoria_id=r.categoria_id,
        fecha_creacion=r.fecha_creacion,
        imagenes=[ImagenModel(imagen_id=i.imagen_id, path=i.path, orden=i.orden) for i in r.imagenes],
        tallas=[TallaModel(talla_id=t.talla_id, nombre=t.nombre) for t in r.tallas],
        colores=[ColorModel(color_id=c.color_id, nombre=c.nombre) for c in r.colores]
    )


class ProductoRepository(ProductoPort):
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_by_id(self, producto_id: str) -> ProductoModel | None:
        stmt = select(ProductoTable).filter_by(producto_id=producto_id).options(
            subqueryload(ProductoTable.imagenes),
            subqueryload(ProductoTable.tallas),
            subqueryload(ProductoTable.colores)
        )
        r = await self.db_session.execute(stmt)
        r = r.scalar_one_or_none()
        return _to_domain(r)

    async def get_all(self) -> list[ProductoModel]:
        stmt = (
            select(ProductoTable)
            .options(
                subqueryload(ProductoTable.imagenes),
                subqueryload(ProductoTable.tallas),
                subqueryload(ProductoTable.colores)
            )
        )
        rows = await self.db_session.execute(stmt)
        rows = rows.scalars().all()
        return [_to_domain(r) for r in rows]

    async def get_by_categoria(self, categoria_id: int) -> list[ProductoModel]:
        stmt = select(ProductoTable).filter_by(categoria_id=categoria_id).options(
            subqueryload(ProductoTable.imagenes),
            subqueryload(ProductoTable.tallas),
            subqueryload(ProductoTable.colores)
        )
        rows = await self.db_session.execute(stmt)
        rows = rows.scalars()
        return [_to_domain(r) for r in rows]

    async def create_producto(self, producto: ProductoModel) -> ProductoModel:
        new_producto = ProductoTable(
            producto_id=producto.producto_id,
            nombre=producto.nombre,
            precio=producto.precio,
            descripcion=producto.descripcion,
            esta_activo=producto.esta_activo,
            esta_destacado=producto.esta_destacado,
            stock=producto.stock,
            categoria_id=producto.categoria_id,
            fecha_creacion=producto.fecha_creacion
        )
        self.db_session.add(new_producto)
        await self.db_session.commit()
        return _to_domain(new_producto)

    async def update_producto(self, producto_id: str, producto: ProductoModel) -> ProductoModel | None:
        stmt = select(ProductoTable).filter_by(producto_id=producto_id)
        r = await self.db_session.execute(stmt)
        r = r.scalar_one_or_none()
        if not r:
            return None

        r.nombre = producto.nombre
        r.precio = producto.precio
        r.descripcion = producto.descripcion
        r.esta_activo = producto.esta_activo
        r.esta_destacado = producto.esta_destacado
        r.stock = producto.stock
        r.categoria_id = producto.categoria_id
        # no se modifica ni el ID ni la fecha_creacion
        await self.db_session.commit()
        return _to_domain(r)

    async def delete_producto(self, producto_id: str) -> None:
        stmt = select(ProductoTable).filter_by(producto_id=producto_id)
        r = await self.db_session.execute(stmt)
        r = r.scalar_one_or_none()
        if r:
            await self.db_session.delete(r)
            await self.db_session.commit()
        return None
