from datetime import datetime
from uuid import uuid4
from src.api.schemas.pedido_dto import PedidoCreateDto, PedidoUpdateDto
from src.domain.models.pedido_model import PedidoModel
from src.domain.ports.pedido_port import PedidoPort

class PedidoUsecases:
    def __init__(self, repo: PedidoPort):
        self.repo = repo

    def create_pedido(self, pedido_data: PedidoCreateDto) -> PedidoModel:
        if pedido_data.promocion_id == 0 or pedido_data.promocion_id is None:
            promocion = None
        else:
            promocion = pedido_data.promocion_id

        pedido = PedidoModel(
            pedido_id=None,
            usuario_id=pedido_data.usuario_id,
            promocion_id=promocion,
            estado="pendiente",
            fecha_pedido=datetime.now(),
            fecha_actualizacion=datetime.now(),
            subtotal=0.0,
            descuento=0.0,
            total=0.0,
            notas=pedido_data.notas,
            direccion=pedido_data.direccion
        )
        return self.repo.create(pedido)

    def get_all(self) -> list[PedidoModel]:
        return self.repo.get_all()

    def get_pedido_by_id(self, pedido_id: int) -> PedidoModel:
        return self.repo.get_by_id(pedido_id)
    
    def get_pedidos_by_user_id(self, user_id: str) -> list[PedidoModel]:
        return self.repo.get_by_user_id(user_id)
    
    def update_pedido(self, pedido_id: int, updated_data: PedidoUpdateDto) -> PedidoModel:
        existing_pedido = self.repo.get_by_id(pedido_id)
        if updated_data.promocion_id is not None:
            existing_pedido.promocion_id = updated_data.promocion_id
        if updated_data.promocion_id == 0:
            existing_pedido.promocion_id = None
        if updated_data.estado is not None:
            existing_pedido.estado = updated_data.estado
        if updated_data.notas is not None:
            existing_pedido.notas = updated_data.notas
        if updated_data.direccion is not None:
            existing_pedido.direccion = updated_data.direccion
        existing_pedido.fecha_actualizacion = datetime.now()
        return self.repo.update(pedido_id, existing_pedido)
    
    def delete_pedido(self, pedido_id: int) -> None:
        return self.repo.delete(pedido_id)
    
    def update_pedido_promocion(self, pedido_id: int, promocion_id: int) -> PedidoModel:
        existing_pedido = self.repo.get_by_id(pedido_id)
        if promocion_id == 0:
            existing_pedido.promocion_id = None
        else:
            existing_pedido.promocion_id = promocion_id
        existing_pedido.fecha_actualizacion = datetime.now()
        return self.repo.update(pedido_id, existing_pedido)
    
    def update_pedido_estado(self, pedido_id: int, estado: str) -> PedidoModel:
        existing_pedido = self.repo.get_by_id(pedido_id)
        existing_pedido.estado = estado
        existing_pedido.fecha_actualizacion = datetime.now()
        return self.repo.update(pedido_id, existing_pedido)