from fastapi import Depends

from src.core.database import get_session
from src.core.messaging.di import get_fcm_service
from src.modules.carrito.infra.carrito_repository import CarritoRepository
from src.modules.catalogo.infra.products.product_repository import ProductoRepository
from src.modules.usuarios.infra.direccion_repository import DireccionRepository
from src.modules.usuarios.infra.fcm_repository import DeviceTokenRepository
from src.modules.ventas.app.pedido import ChangePedidoStatus, CreatePedido, GetPedidoById, GetPedidosByUser, \
    GetPedidos
from src.modules.ventas.infra.pedido.pedido_repository import PedidoRepository
from src.modules.ventas.infra.promocion.promocion_repository import PromocionRepository


def get_create_pedido(session=Depends(get_session)):
    pedido_repo = PedidoRepository(session)
    carrito_repo = CarritoRepository(session)
    direccion_repo = DireccionRepository(session)
    producto_repo = ProductoRepository(session)
    promocion_repo = PromocionRepository(session)
    fcm_repo = DeviceTokenRepository(session)

    return CreatePedido(pedido_repo, carrito_repo, direccion_repo, producto_repo, promocion_repo, fcm_repo, get_fcm_service())


def get_all_pedidos(session=Depends(get_session)):
    pedido_repo = PedidoRepository(session)
    return GetPedidos(pedido_repo)


def get_by_id(session=Depends(get_session)):
    pedido_repo = PedidoRepository(session)
    return GetPedidoById(pedido_repo)


def get_by_user(session=Depends(get_session)):
    pedido_repo = PedidoRepository(session)
    return GetPedidosByUser(pedido_repo)


def get_change_status(session=Depends(get_session)):
    pedido_repo = PedidoRepository(session)
    return ChangePedidoStatus(pedido_repo)
