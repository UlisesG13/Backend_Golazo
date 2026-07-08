from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.ventas.domain import PromocionPort, PromocionModel
from src.modules.ventas.infra.promocion.promocion_table import PromocionTable


def to_domain(r: PromocionTable) -> PromocionModel:
    return PromocionModel(
        promocion_id=r.promocion_id,
        codigo=r.codigo,
        descuento=r.descuento,
        tipo_descuento=r.tipo_descuento,
        contador_usos=r.contador_usos,
        usos_maximos=r.usos_maximos,
        fecha_inicio=r.fecha_inicio,
        fecha_expiracion=r.fecha_expiracion,
        esta_activa=r.esta_activa
    )


class PromocionRepository(PromocionPort):
    def __init__(self, db_session: AsyncSession):
        self.db = db_session

    async def create(self, promocion: PromocionModel) -> PromocionModel:
        new_promocion = PromocionTable(
            codigo=promocion.codigo,
            descuento=promocion.descuento,
            tipo_descuento=promocion.tipo_descuento,
            contador_usos=promocion.contador_usos,
            usos_maximos=promocion.usos_maximos,
            fecha_inicio=promocion.fecha_inicio,
            fecha_expiracion=promocion.fecha_expiracion,
            esta_activa=promocion.esta_activa
        )
        self.db.add(new_promocion)
        await self.db.flush()  # Envía los cambios a la BD pero NO cierra la transacción
        await self.db.refresh(new_promocion)
        await self.db.commit()
        return to_domain(new_promocion)

    async def get_all(self) -> list[PromocionModel]:
        stmt = select(PromocionTable)
        rows = await self.db.execute(stmt)
        rows = rows.scalars().all()
        return [to_domain(r) for r in rows]

    async def get_by_id(self, promocion_id: int) -> PromocionModel | None:
        r = await self.db.get(PromocionTable, promocion_id)
        return to_domain(r) if r else None  # type: ignore[arg-type]

    async def delete(self, promocion_id: int) -> None:
        r = await self.db.get(PromocionTable, promocion_id)
        self.db.delete(r)
        await self.db.commit()
        return

    async def update(self, promocion_id: int, updated_data: PromocionModel) -> PromocionModel | None:
        r = await self.db.get(PromocionTable, promocion_id)
        if not r:
            return None
        r.codigo = updated_data.codigo
        r.descuento = updated_data.descuento
        r.tipo_descuento = updated_data.tipo_descuento
        r.contador_usos = updated_data.contador_usos
        r.usos_maximos = updated_data.usos_maximos
        r.fecha_inicio = updated_data.fecha_inicio
        r.fecha_expiracion = updated_data.fecha_expiracion
        r.esta_activa = updated_data.esta_activa

        await self.db.commit()
        await self.db.refresh(r)
        return to_domain(r)  # type: ignore[arg-type]

    async def change_status(self, promocion_id: int, status: bool) -> PromocionModel:
        r = await self.db.get_one(PromocionTable, promocion_id)
        r.esta_activa = status

        await self.db.commit()
        await self.db.refresh(r)
        return to_domain(r)  # type: ignore[arg-type]

    async def get_by_codigo(self, codigo: str) -> PromocionModel | None:
        stmt = select(PromocionTable).filter(PromocionTable.codigo == codigo)
        r = await self.db.execute(stmt)
        r = r.scalars().first()
        return to_domain(r) if r else None  # type: ignore[arg-type]

    async def save_usage(self, promocion: PromocionModel) -> None:
        r = await self.db.get(PromocionTable, promocion.promocion_id)
        r.contador_usos = promocion.contador_usos
        await self.db.commit()
        await self.db.refresh(r)
