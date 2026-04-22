from sqlalchemy import select
from sqlalchemy.orm import Session

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
    def __init__(self, db_session: Session):
        self.db = db_session

    def create(self, promocion: PromocionModel) -> PromocionModel:
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
        self.db.flush()  # Envía los cambios a la BD pero NO cierra la transacción
        self.db.refresh(new_promocion)
        self.db.commit()
        return to_domain(new_promocion)

    def get_all(self) -> list[PromocionModel]:
        stmt = select(PromocionTable)
        rows = self.db.execute(stmt).scalars().all()
        return [to_domain(r) for r in rows]

    def get_by_id(self, promocion_id: int) -> PromocionModel | None:
        r = self.db.get(PromocionTable, promocion_id)
        return to_domain(r) if r else None  # type: ignore[arg-type]

    def delete(self, promocion_id: int) -> None:
        r = self.db.get(PromocionTable, promocion_id)
        self.db.delete(r)
        self.db.commit()
        return

    def update(self, promocion_id: int, updated_data: PromocionModel) -> PromocionModel | None:
        r = self.db.get(PromocionTable, promocion_id)
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

        self.db.commit()
        self.db.refresh(r)
        return to_domain(r)  # type: ignore[arg-type]

    def change_status(self, promocion_id: int, status: bool) -> PromocionModel:
        r = self.db.get_one(PromocionTable, promocion_id)
        r.esta_activa = status

        self.db.commit()
        self.db.refresh(r)
        return to_domain(r)  # type: ignore[arg-type]

    def get_by_codigo(self, codigo: str) -> PromocionModel | None:
        stmt = select(PromocionTable).filter(PromocionTable.codigo == codigo)
        r = self.db.execute(stmt).scalars().first()
        return to_domain(r) if r else None  # type: ignore[arg-type]

    def save_usage(self, promocion: PromocionModel) -> None:
        r = self.db.get(PromocionTable, promocion.promocion_id)
        r.contador_usos = promocion.contador_usos
        self.db.commit()
        self.db.refresh(r)
