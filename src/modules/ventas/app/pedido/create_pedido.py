from datetime import datetime

from src.core.exceptions import NotFoundError, BadRequestError
from src.shared.domain.ports.messaging_port import MessagingPort
from src.modules.carrito.domain import CarritoPort
from src.modules.catalogo.domain.ports import ProductoPort
from src.modules.usuarios.domain.ports import DireccionPort, DeviceTokenPort
from src.modules.ventas.domain import PedidoPort, PromocionPort
from src.modules.ventas.domain.models import PedidoModel, PedidoItemModel
from src.modules.ventas.infra.pedido.pedido_table import EstadoPedido
from src.modules.ventas.presentation.pedido.pedido_dto import CreatePedidoDTO

class CreatePedido:

    def __init__(
            self,
            pedido_repo: PedidoPort,
            carrito_repo: CarritoPort,
            direccion_repo: DireccionPort,
            producto_repo: ProductoPort,
            promocion_repo: PromocionPort,
            token_repo: DeviceTokenPort,
            notification_service: MessagingPort,
    ):
        self.pedido_repo = pedido_repo
        self.carrito_repo = carrito_repo
        self.direccion_repo = direccion_repo
        self.producto_repo = producto_repo
        self.promocion_repo = promocion_repo
        self.token_repo = token_repo
        self.fcm_service = notification_service

    async def execute(self, dto: CreatePedidoDTO, usuario_id: str) -> PedidoModel:

        now = datetime.now()

        # 1. Carrito
        carrito = await self.carrito_repo.get_by_user_id(usuario_id)
        if not carrito or not carrito.items:
            raise BadRequestError("Carrito vacío")

        # 2. Dirección
        direccion = await self.direccion_repo.get_direccion_by_id(dto.direccion_id, usuario_id)
        if not direccion:
            raise NotFoundError("Dirección no encontrada")

        direccion = direccion.to_dict()
        # 3. Items (SNAPSHOT)
        items_pedido = []

        for item in carrito.items:
            producto = await self.producto_repo.get_by_id(item.producto_id)

            if not producto:
                raise NotFoundError(f"Producto no encontrado: {item.producto_id}")

            # Validación de Stock Dinámico
            if producto.stock != 0:
                if item.cantidad > producto.stock:
                    raise BadRequestError(f"El producto {producto.nombre} ya no tiene stock suficiente. Disponible: {producto.stock}")

            items_pedido.append(
                PedidoItemModel(
                    pedido_item_id=None,
                    pedido_id=None,
                    producto_id=item.producto_id,
                    nombre_producto=producto.nombre,
                    color_id=item.color_id,
                    talla_id=item.talla_id,
                    cantidad=item.cantidad,
                    precio_unitario=item.precio_unitario,
                )
            )

        # 4. Subtotal
        subtotal = sum(i.subtotal for i in items_pedido)

        # 5. Promoción
        descuento = 0.0
        promocion_id = None

        if dto.promocion:
            promo = await self.promocion_repo.get_by_codigo(dto.promocion)

            if not promo:
                raise NotFoundError("Promoción no encontrada")

            if not promo.is_available(now):
                raise BadRequestError("Promoción no válida")

            descuento = promo.calculate_discount_amount(subtotal)
            promo.apply_usage()

            await self.promocion_repo.save_usage(promo)
            promocion_id = promo.promocion_id

        # 6. Total
        total = max(0.0, subtotal - descuento)
        if dto.notas:
            notas = dto.notas
        else:
            notas = "Sin comentarios"

        # 7. Pedido (SNAPSHOT)
        pedido = PedidoModel(
            pedido_id=None,
            usuario_id=usuario_id,
            estado=EstadoPedido.pendiente.value,
            fecha_pedido=now,
            fecha_actualizacion=now,
            promocion_id=promocion_id,
            subtotal=subtotal,
            descuento=descuento,
            total=total,
            direccion=direccion,  # snapshot
            items=items_pedido,
            notas=notas,
        )

        # 8. Persistir
        pedido_guardado = await self.pedido_repo.save(pedido)

        # 9. Limpiar carrito
        await self.carrito_repo.delete(carrito.carrito_id)

        tokens = await self.token_repo.get_all()

        for token in tokens:
            try:
                self.fcm_service.send(
                    token=token.token,
                    title="Nuevo pedido",
                    body=f"Pedido #{pedido_guardado.pedido_id} creado",
                    data={
                        "type": "NEW_ORDER",
                        "pedido_id": str(pedido_guardado.pedido_id)
                    }
                )
            except Exception:
                await self.token_repo.delete(token.token)
        return pedido_guardado
