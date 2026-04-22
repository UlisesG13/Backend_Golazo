from src.modules.ventas.domain import PromocionPort


class DeletePromocion:
    def __init__(self, repo: PromocionPort):
        self.repo = repo

    def execute(self, promocion_id: int) -> None:
        self.repo.delete(promocion_id)