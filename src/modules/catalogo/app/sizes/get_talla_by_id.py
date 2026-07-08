from src.core.exceptions import NotFoundError
from src.modules.catalogo.domain.models import TallaModel
from src.modules.catalogo.domain.ports import TallaPort


class GetTallaById:
    def __init__(self, repo: TallaPort):
        self.repo = repo

    async def execute(self, talla_id: int) -> TallaModel:
        talla = await self.repo.get_by_id(talla_id)
        if not talla:
            raise NotFoundError(f"Talla id {talla_id} not found")
        return talla
