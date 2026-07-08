from src.modules.catalogo.domain.ports.categoria_port import CategoriaPort


class DeleteCategory:
    def __init__(self, repo: CategoriaPort):
        self.repo = repo

    async def execute(self, categoria_id: int) -> None:
        return await self.repo.delete(categoria_id)
