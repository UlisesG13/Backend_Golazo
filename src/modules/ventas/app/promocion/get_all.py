from src.modules.ventas.domain import PromocionModel, PromocionPort


class GetAll:
    def __init__(self, repo: PromocionPort):
        self.repo = repo

    async def execute(self) -> list[PromocionModel]:
        return await self.repo.get_all()
