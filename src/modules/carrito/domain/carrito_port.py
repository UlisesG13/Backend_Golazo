from typing import Protocol

from src.modules.carrito.domain.carrito_model import CarritoModel


class CarritoPort(Protocol):
    def get_by_user_id(self, user_id: str) -> CarritoModel | None: ...

    def save(self, model: CarritoModel) -> CarritoModel: ...

    def delete(self, cart_id: str) -> None: ...
