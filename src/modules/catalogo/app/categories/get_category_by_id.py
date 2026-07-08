from src.modules.catalogo.domain.models import CategoriaModel
from src.modules.catalogo.domain.ports.categoria_port import CategoriaPort


class GetCategoryById:
    def __init__(self, repo: CategoriaPort):
        self.repo = repo

    async def execute(self, categoria_id: int) -> CategoriaModel:
        return await self.repo.get_by_id(categoria_id)
