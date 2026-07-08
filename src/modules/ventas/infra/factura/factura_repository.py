from datetime import datetime
from typing import Any, cast

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.ventas.domain.models import FacturaModel, EstadoFactura, PedidoItemModel
from src.modules.ventas.domain.ports import FacturaPort
from src.modules.ventas.infra.factura.factura_table import FacturaTable, EstadoFactura as EstadoFacturaTable
from src.modules.ventas.infra.pedido.pedido_table import PedidoTable


def to_domain(table: FacturaTable) -> FacturaModel:
    # Aseguramos que items sea una lista para iterar y evitar warnings de Any

    return FacturaModel(
        factura_id=table.factura_id,
        pedido_id=table.pedido_id,
        folio=table.folio,
        uuid_fiscal=table.uuid_fiscal,
        fecha_emision=table.fecha_emision,
        fecha_vencimiento=table.fecha_vencimiento,
        emisor_datos=cast(dict[str, Any], table.emisor_datos),
        receptor_datos=cast(dict[str, Any], table.receptor_datos),
        moneda=table.moneda,
        subtotal=float(table.subtotal),
        descuento_total=float(table.descuento_total),
        impuestos_totales=float(table.impuestos_totales),
        total=float(table.total),
        estado=EstadoFactura(table.estado.value),
        metodo_pago=table.metodo_pago,
        forma_pago=table.forma_pago,
        items=[
            PedidoItemModel(
                pedido_item_id=item.get("pedido_item_id"),
                pedido_id=item.get("pedido_id"),
                producto_id=str(item.get("producto_id", "")),
                nombre_producto=str(item.get("nombre_producto", "")),
                color_id=int(item.get("color_id", 0)),
                talla_id=int(item.get("talla_id", 0)),
                cantidad=int(item.get("cantidad", 0)),
                precio_unitario=float(item.get("precio_unitario", 0.0))
            )
            for item in table.items
        ]
    )


class FacturaRepository(FacturaPort):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, factura: FacturaModel) -> FacturaModel:
        factura_db = FacturaTable(
            pedido_id=factura.pedido_id,
            folio=factura.folio,
            uuid_fiscal=cast(str, factura.uuid_fiscal),
            fecha_emision=factura.fecha_emision,
            fecha_vencimiento=cast(datetime, factura.fecha_vencimiento),
            emisor_datos=factura.emisor_datos,
            receptor_datos=factura.receptor_datos,
            moneda=factura.moneda,
            subtotal=factura.subtotal,
            descuento_total=factura.descuento_total,
            impuestos_totales=factura.impuestos_totales,
            total=factura.total,
            estado=EstadoFacturaTable(factura.estado.value),
            metodo_pago=factura.metodo_pago,
            forma_pago=factura.forma_pago,
            items=[
                {
                    "pedido_item_id": item.pedido_item_id,
                    "pedido_id": item.pedido_id,
                    "producto_id": item.producto_id,
                    "nombre_producto": item.nombre_producto,
                    "color_id": item.color_id,
                    "talla_id": item.talla_id,
                    "cantidad": item.cantidad,
                    "precio_unitario": item.precio_unitario
                }
                for item in factura.items
            ]
        )
        self.session.add(factura_db)
        await self.session.commit()
        await self.session.refresh(factura_db)
        return to_domain(factura_db)

    async def get_all(self) -> list[FacturaModel]:
        stmt = select(FacturaTable)
        results = await self.session.execute(stmt)
        results = results.scalars().all()
        return [to_domain(f) for f in results]

    async def get_by_id(self, factura_id: int) -> FacturaModel | None:
        factura_db = await self.session.get(FacturaTable, factura_id)
        if not factura_db:
            return None
        return to_domain(factura_db)  # type: ignore[arg-type]

    async def get_by_folio(self, folio: str) -> FacturaModel | None:
        stmt = select(FacturaTable).where(FacturaTable.folio == folio)
        result = await self.session.execute(stmt)
        result = result.scalar_one_or_none()
        if not result:
            return None
        return to_domain(result)  # type: ignore[arg-type]

    async def get_by_usuario_id(self, usuario_id: str) -> list[FacturaModel]:
        # Unimos con PedidoTable para filtrar por usuario_id
        stmt = (
            select(FacturaTable)
            .join(PedidoTable, FacturaTable.pedido_id == PedidoTable.pedido_id)
            .where(PedidoTable.usuario_id == usuario_id)
        )
        results = await self.session.execute(stmt)
        results = results.scalars().all()
        return [to_domain(f) for f in results]

    async def update(self, factura_id: int, factura: FacturaModel) -> FacturaModel | None:
        factura_db = await self.session.get(FacturaTable, factura_id)
        if not factura_db:
            return None

        factura_db.folio = factura.folio
        factura_db.uuid_fiscal = cast(str, factura.uuid_fiscal)
        factura_db.fecha_vencimiento = cast(datetime, factura.fecha_vencimiento)
        factura_db.emisor_datos = factura.emisor_datos
        factura_db.receptor_datos = factura.receptor_datos
        factura_db.moneda = factura.moneda
        factura_db.subtotal = factura.subtotal
        factura_db.descuento_total = factura.descuento_total
        factura_db.impuestos_totales = factura.impuestos_totales
        factura_db.total = factura.total
        factura_db.estado = EstadoFacturaTable(factura.estado.value)
        factura_db.metodo_pago = factura.metodo_pago
        factura_db.forma_pago = factura.forma_pago
        factura_db.items = [
            {
                "pedido_item_id": item.pedido_item_id,
                "pedido_id": item.pedido_id,
                "producto_id": item.producto_id,
                "nombre_producto": item.nombre_producto,
                "color_id": item.color_id,
                "talla_id": item.talla_id,
                "cantidad": item.cantidad,
                "precio_unitario": item.precio_unitario
            }
            for item in factura.items
        ]

        await self.session.commit()
        await self.session.refresh(factura_db)
        return to_domain(factura_db)  # type: ignore[arg-type]

    async def delete(self, factura_id: int) -> bool:
        factura_db = await self.session.get(FacturaTable, factura_id)
        if not factura_db:
            return False
        self.session.delete(factura_db)
        await self.session.commit()
        return True
