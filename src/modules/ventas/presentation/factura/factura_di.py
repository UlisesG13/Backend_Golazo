from fastapi import Depends
from src.core.database import get_session
from src.modules.ventas.app.factura import (
    GetAll, GetById, GetByFolio, GetByUsuario, CreateFactura, ChangeStatus, DeleteFactura
)
from src.modules.ventas.infra.factura.factura_repository import FacturaRepository
from src.modules.ventas.infra.pedido.pedido_repository import PedidoRepository


def get_create_factura(session=Depends(get_session)):
    factura_repo = FacturaRepository(session)
    pedido_repo = PedidoRepository(session)
    return CreateFactura(factura_repo, pedido_repo)


def get_all_facturas(session=Depends(get_session)):
    repo = FacturaRepository(session)
    return GetAll(repo)


def get_factura_by_id(session=Depends(get_session)):
    repo = FacturaRepository(session)
    return GetById(repo)


def get_factura_by_folio(session=Depends(get_session)):
    repo = FacturaRepository(session)
    return GetByFolio(repo)


def get_facturas_by_usuario(session=Depends(get_session)):
    repo = FacturaRepository(session)
    return GetByUsuario(repo)


def get_change_factura_status(session=Depends(get_session)):
    repo = FacturaRepository(session)
    return ChangeStatus(repo)


def get_delete_factura(session=Depends(get_session)):
    repo = FacturaRepository(session)
    return DeleteFactura(repo)
