from src.modules.ventas.domain import FacturaPort, FacturaModel


class GetAll:
    def __init__(self, repo: FacturaPort):
        self.repo = repo

    async def execute(self) -> list[FacturaModel]:
        return await self.repo.get_all()
