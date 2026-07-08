from src.modules.catalogo.domain.ports.categoria_port import CategoriaPort


class GetAllBySection:
    def __init__(self, repo: CategoriaPort):
        self.repo = repo

    async def execute(self, seccion_id: int):
        return await self.repo.get_all_by_seccion(seccion_id)
