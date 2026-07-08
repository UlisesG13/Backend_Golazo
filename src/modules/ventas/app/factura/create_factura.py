from typing import cast

from src.core.exceptions import NotFoundError
from src.modules.ventas.domain.models import FacturaModel
from src.modules.ventas.domain.ports import FacturaPort, PedidoPort


class CreateFactura:
    def __init__(self, factura_repo: FacturaPort, pedido_repo: PedidoPort):
        self.factura_repo = factura_repo
        self.pedido_repo = pedido_repo

    async def execute(self, pedido_id: int, datos_fiscales_receptor: dict) -> FacturaModel:
        # 1. Obtener el pedido completo con sus items
        pedido = await self.pedido_repo.get_by_id(pedido_id)
        if not pedido:
            raise NotFoundError("Pedido no encontrado")

        # 2. Crear la entidad de Factura (Snapshot)
        nueva_factura = FacturaModel(
            factura_id=None,
            pedido_id=cast(int, pedido.pedido_id),
            folio=f"FAC-{pedido.pedido_id}-2026",  # Generador de folios
            receptor_datos=datos_fiscales_receptor,
            emisor_datos={
                "rfc": "MI_ECOMMERCE_RFC",
                "nombre": "Mi Tienda S.A. de C.V.",
                "regimen": "601"
            },
            descuento_total=pedido.descuento,
            items=pedido.items,
            metodo_pago="PUE",
            forma_pago="04"  # Supongamos Tarjeta de Crédito
        )

        # 3. Calcular impuestos y totales
        nueva_factura.calcular_totales(tasa_impuesto=0.16)

        # 4. Persistir en la base de datos
        return await self.factura_repo.create(nueva_factura)
