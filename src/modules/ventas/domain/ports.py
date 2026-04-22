from datetime import datetime
from typing import Protocol

from src.modules.ventas.domain.models import PromocionModel, PedidoModel, FacturaModel


class PromocionPort(Protocol):
    def create(self, promocion: PromocionModel) -> PromocionModel:
        ...

    def get_all(self) -> list[PromocionModel]:
        ...

    def get_by_id(self, promocion_id: int) -> PromocionModel | None:
        ...

    def delete(self, promocion_id: int) -> None:
        ...

    def update(self, promocion_id: int, updated_data: PromocionModel) -> PromocionModel | None:
        ...

    def change_status(self, promocion_id: int, status: bool) -> PromocionModel:
        ...

    def get_by_codigo(self, codigo: str) -> PromocionModel | None:
        ...

    def save_usage(self, promocion: PromocionModel) -> None:
        ...

class PedidoPort(Protocol):
    def save(self, model: PedidoModel) -> PedidoModel:
        ...

    def get_all(self) -> list[PedidoModel]:
        ...

    def get_by_id(self, pedido_id: int) -> PedidoModel | None:
        ...

    def get_by_user_id(self, user_id: str) -> list[PedidoModel]:
        ...

    def get_by_status(self, status: str) -> list[PedidoModel]:
        ...

    def update_status(self, pedido_id: int, status: str, time: datetime) -> None:
        ...

    def delete(self, pedido_id: int) -> None:
        ...


class NotificationPort(Protocol):

    def send_new_promocion(self, token: str, codigo: str, descuento: str):
        ...


class FacturaPort(Protocol):

    def create(self, factura: FacturaModel) -> FacturaModel:
        ...

    def get_all(self) -> list[FacturaModel]:
        ...

    def get_by_id(self, factura_id: int) -> FacturaModel | None:
        ...

    def get_by_folio(self, folio: str) -> FacturaModel | None:
        ...

    def get_by_usuario_id(self, usuario_id: str) -> list[FacturaModel]:
        ...

    def update(self, factura_id: int, factura: FacturaModel) -> FacturaModel | None:
        ...

    def delete(self, factura_id: int) -> bool:
        ...