from typing import Protocol

from src.modules.ventas.domain.models import PromocionModel


class PromocionPort(Protocol):
    def create(self, promocion: PromocionModel) -> PromocionModel:
        ...

    def get_all(self) -> list[PromocionModel]:
        ...

    def get_by_id(self, promocion_id: int) -> PromocionModel:
        ...

    def delete(self, promocion_id: int) -> None:
        ...

    def update(self, promocion_id: int, data: PromocionModel) -> PromocionModel:
        ...

    def change_status(self, promocion_id: int, status: bool) -> PromocionModel:
        ...

    def get_by_codigo(self, codigo: str) -> PromocionModel | None:
        ...