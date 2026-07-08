from datetime import datetime
from typing import Protocol

from src.modules.ventas.domain.models import PromocionModel, PedidoModel, FacturaModel


class PromocionPort(Protocol):
    async def create(self, promocion: PromocionModel) -> PromocionModel:
        ...

    async def get_all(self) -> list[PromocionModel]:
        ...

    async def get_by_id(self, promocion_id: int) -> PromocionModel | None:
        ...

    async def delete(self, promocion_id: int) -> None:
        ...

    async def update(self, promocion_id: int, updated_data: PromocionModel) -> PromocionModel | None:
        ...

    async def change_status(self, promocion_id: int, status: bool) -> PromocionModel:
        ...

    async def get_by_codigo(self, codigo: str) -> PromocionModel | None:
        ...

    async def save_usage(self, promocion: PromocionModel) -> None:
        ...

class PedidoPort(Protocol):
    async def save(self, model: PedidoModel) -> PedidoModel:
        ...

    async def get_all(self) -> list[PedidoModel]:
        ...

    async def get_by_id(self, pedido_id: int) -> PedidoModel | None:
        ...

    async def get_by_user_id(self, user_id: str) -> list[PedidoModel]:
        ...

    async def get_by_status(self, status: str) -> list[PedidoModel]:
        ...

    async def update_status(self, pedido_id: int, status: str, time: datetime) -> None:
        ...

    async def delete(self, pedido_id: int) -> None:
        ...


class NotificationPort(Protocol):

    def send_new_promocion(self, token: str, codigo: str, descuento: str):
        ...


class FacturaPort(Protocol):

    async def create(self, factura: FacturaModel) -> FacturaModel:
        ...

    async def get_all(self) -> list[FacturaModel]:
        ...

    async def get_by_id(self, factura_id: int) -> FacturaModel | None:
        ...

    async def get_by_folio(self, folio: str) -> FacturaModel | None:
        ...

    async def get_by_usuario_id(self, usuario_id: str) -> list[FacturaModel]:
        ...

    async def update(self, factura_id: int, factura: FacturaModel) -> FacturaModel | None:
        ...

    async def delete(self, factura_id: int) -> bool:
        ...
