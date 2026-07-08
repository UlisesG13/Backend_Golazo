from typing import Protocol

from src.modules.carrito.domain.carrito_model import CarritoModel


class CarritoPort(Protocol):
    async def get_by_user_id(self, user_id: str) -> CarritoModel | None: ...

    async def save(self, model: CarritoModel) -> CarritoModel: ...

    async def delete(self, cart_id: str) -> None: ...
