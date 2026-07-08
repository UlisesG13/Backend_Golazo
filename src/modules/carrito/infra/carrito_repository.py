from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.modules.carrito.domain import CarritoPort
from src.modules.carrito.domain.carrito_model import CarritoModel, CarritoItemModel
from src.modules.carrito.infra.carrito_table import CarritoTable, CarritoItemTable


def to_domain(table: CarritoTable) -> CarritoModel:
    return CarritoModel(
        carrito_id=table.carrito_id,
        usuario_id=table.usuario_id,
        fecha_creacion=table.fecha_creacion,
        fecha_actualizacion=table.fecha_actualizacion,
        # Mapeamos los ítems de la tabla a modelos de dominio
        items=[
            CarritoItemModel(
                carrito_item_id=item.carrito_item_id,
                producto_id=item.producto_id,
                color_id=item.color_id,
                talla_id=item.talla_id,
                cantidad=item.cantidad,
                precio_unitario=float(item.precio_unitario)
            ) for item in table.items
        ]
    )


class CarritoRepository(CarritoPort):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_user_id(self, user_id: str) -> CarritoModel | None:
        # Usamos joinedload para traer los ítems en una sola consulta (Eager Loading)
        stmt = select(CarritoTable).where(CarritoTable.usuario_id == user_id).options(
            joinedload(CarritoTable.items)
        )
        result = await self.session.execute(stmt)
        result = result.unique().scalar_one_or_none()

        if not result:
            return None

        return to_domain(result)

    async def save(self, model: CarritoModel):
        carrito_db = await self.session.get(CarritoTable, model.carrito_id)

        if not carrito_db:
            carrito_db = CarritoTable(
                carrito_id=model.carrito_id,
                usuario_id=model.usuario_id
            )
            self.session.add(carrito_db)

        existentes = {
            (item.producto_id, item.color_id, item.talla_id): item
            for item in carrito_db.items
        }

        nuevos_items_db = []

        for item_dominio in model.items:
            key = (item_dominio.producto_id, item_dominio.color_id, item_dominio.talla_id)

            if key in existentes:
                item_db = existentes[key]
                item_db.cantidad = item_dominio.cantidad
                item_db.precio_unitario = item_dominio.precio_unitario
            else:
                item_db = CarritoItemTable(
                    producto_id=item_dominio.producto_id,
                    color_id=item_dominio.color_id,
                    talla_id=item_dominio.talla_id,
                    cantidad=item_dominio.cantidad,
                    precio_unitario=item_dominio.precio_unitario
                )

            nuevos_items_db.append(item_db)

        carrito_db.items = nuevos_items_db
        carrito_db.fecha_creacion = model.fecha_creacion
        carrito_db.fecha_actualizacion = model.fecha_actualizacion

        await self.session.commit()
        await self.session.refresh(carrito_db)

        return to_domain(carrito_db)  # # type: ignore[arg-type]

    async def delete(self, cart_id: str) -> None:
        carrito = await self.session.get(CarritoTable, cart_id)
        if carrito:
            self.session.delete(carrito)
            await self.session.commit()
