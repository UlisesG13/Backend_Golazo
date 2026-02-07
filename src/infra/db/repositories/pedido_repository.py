from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.models.pedido_model import PedidoModel
from src.domain.ports.pedido_port import PedidoPort
from src.infra.db.models.pedido_table import PedidoTable
from src.core.exceptions import NotFoundError
from src.infra.db.models.promocion_table import PromocionTable # importando para que cargue el modelo

class PedidoRepository(PedidoPort):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def _to_domain(self, r: PedidoTable) -> PedidoModel:
        return PedidoModel(
            pedido_id=r.pedido_id,
            usuario_id=r.usuario_id,
            promocion_id=r.promocion_id,
            estado=str(r.estado.value) if r.estado is not None else None,
            fecha_pedido=r.fecha_pedido,
            fecha_actualizacion=r.fecha_actualizacion,
            subtotal=r.subtotal,
            descuento=r.descuento,
            total=r.total,
            notas=r.notas,
            direccion=r.direccion
        )
    def get_by_id(self, pedido_id: int) -> PedidoModel:
        pedido = self.db_session.query(PedidoTable).filter_by(pedido_id=pedido_id).first()
        if not pedido:
            raise NotFoundError(f"Pedido con ID {pedido_id} no encontrado")
        return self._to_domain(pedido)
    
    def get_by_user_id(self, user_id: str) -> list[PedidoModel]:
        pedidos = self.db_session.query(PedidoTable).filter_by(usuario_id=user_id).all()
        return [self._to_domain(p) for p in pedidos]
    
    def create(self, pedido: PedidoModel) -> PedidoModel:
        model = PedidoTable(
            usuario_id=pedido.usuario_id,
            promocion_id=pedido.promocion_id,
            estado=pedido.estado,
            fecha_pedido=pedido.fecha_pedido,
            fecha_actualizacion=pedido.fecha_actualizacion,
            subtotal=pedido.subtotal,
            descuento=pedido.descuento,
            total=pedido.total,
            notas=pedido.notas,
            direccion=pedido.direccion
        )
        self.db_session.add(model)
        self.db_session.commit()
        self.db_session.refresh(model)
        return self._to_domain(model)
    
    def delete(self, pedido_id: int) -> None:
        pedido = self.db_session.query(PedidoTable).filter_by(pedido_id=pedido_id).first()
        if not pedido:
            raise NotFoundError(f"Pedido con ID {pedido_id} no encontrado")
        self.db_session.delete(pedido)
        self.db_session.commit()

    def update(self, pedido_id: int, updated_data: PedidoModel) -> PedidoModel:
        pedido = self.db_session.query(PedidoTable).filter_by(pedido_id=pedido_id).first()
        if not pedido:
            raise NotFoundError(f"Pedido con ID {pedido_id} no encontrado")
        
        pedido.usuario_id = updated_data.usuario_id
        pedido.promocion_id = updated_data.promocion_id
        pedido.estado = updated_data.estado
        pedido.fecha_pedido = updated_data.fecha_pedido
        pedido.fecha_actualizacion = updated_data.fecha_actualizacion
        pedido.subtotal = updated_data.subtotal
        pedido.descuento = updated_data.descuento
        pedido.total = updated_data.total
        pedido.notas = updated_data.notas
        pedido.direccion = updated_data.direccion
        
        self.db_session.commit()
        return self._to_domain(pedido)