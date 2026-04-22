from datetime import datetime
from typing import cast

from sqlalchemy import select, update
from sqlalchemy.orm import Session, joinedload
import json

from src.modules.ventas.domain import PedidoModel, PedidoPort, PedidoItemModel
from src.modules.ventas.infra.pedido.pedido_table import PedidoTable, PedidoItemTable

def to_domain(table: PedidoTable) -> PedidoModel:
    return PedidoModel(
        pedido_id=table.pedido_id,
        usuario_id=table.usuario_id,
        promocion_id=table.promocion_id,
        estado=table.estado,
        fecha_pedido=table.fecha_pedido,
        fecha_actualizacion=table.fecha_actualizacion,
        subtotal=float(table.subtotal),
        descuento=float(table.descuento),
        total=float(table.total),
        notas=table.notas,
        direccion=json.loads(table.direccion),
        items=[
            PedidoItemModel(
                pedido_item_id=item.pedido_item_id,
                pedido_id=item.pedido_id,
                producto_id=item.producto_id,
                nombre_producto=item.nombre_producto,
                color_id=item.color_id,
                talla_id=item.talla_id,
                cantidad=item.cantidad,
                precio_unitario=float(item.precio_unitario)
            )
            for item in table.items
        ]
    )

class PedidoRepository(PedidoPort):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[PedidoModel]:
        stmt = (
            select(PedidoTable)
            .options(joinedload(PedidoTable.items))
        )
        results = self.session.execute(stmt).unique().scalars().all()
        return [to_domain(p) for p in results]

    def save(self, model: PedidoModel) -> PedidoModel:
        pedido_db = PedidoTable(
            usuario_id=model.usuario_id,
            promocion_id=cast(int, model.promocion_id),
            estado=model.estado,
            fecha_pedido=model.fecha_pedido,
            fecha_actualizacion=model.fecha_actualizacion,
            subtotal=model.subtotal,
            descuento=model.descuento,
            total=model.total,
            notas=model.notas,
            direccion=json.dumps(model.direccion)
        )
        pedido_db.items = [
            PedidoItemTable(
                producto_id=item.producto_id,
                nombre_producto=item.nombre_producto,
                color_id=item.color_id,
                talla_id=item.talla_id,
                cantidad=item.cantidad,
                precio_unitario=item.precio_unitario
            )
            for item in model.items
        ]

        self.session.add(pedido_db)
        self.session.commit()
        self.session.refresh(pedido_db)

        return to_domain(pedido_db)

    def get_by_id(self, pedido_id: int) -> PedidoModel | None:
        result = self.session.get(
            PedidoTable,
            pedido_id,
            options=[joinedload(PedidoTable.items)]
        )
        if not result:
            return None

        return to_domain(result) # type: ignore[arg-type]

    def get_by_user_id(self, user_id: str) -> list[PedidoModel]:
        stmt = (
            select(PedidoTable)
            .where(PedidoTable.usuario_id == user_id)
            .options(joinedload(PedidoTable.items))
        )
        results = self.session.execute(stmt).unique().scalars().all()
        return [to_domain(p) for p in results]

    def get_by_status(self, status: str) -> list[PedidoModel]:
        stmt = (
            select(PedidoTable)
            .where(PedidoTable.estado == status)
            .options(joinedload(PedidoTable.items))
        )
        results = self.session.execute(stmt).unique().scalars().all()
        return [to_domain(p) for p in results]

    def update_status(self, pedido_id: int, status: str, time: datetime) -> None:
        stmt = (
            update(PedidoTable)
            .where(PedidoTable.pedido_id == pedido_id)
            .values(estado = status)
            .values(fecha_actualizacion = time)
        )
        self.session.execute(stmt)
        self.session.commit()

    def delete(self, pedido_id: int) -> None:
        pedido = self.session.get(PedidoTable, pedido_id)
        if pedido:
            self.session.delete(pedido)
            self.session.commit()