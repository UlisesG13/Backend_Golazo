from src.modules.ventas.domain import PromocionPort


class DeletePromocion:
    def __init__(self, repo: PromocionPort):
        self.repo = repo

    async def execute(self, promocion_id: int) -> None:
        await self.repo.delete(promocion_id)
