from src.modules.catalogo.domain.ports import SeccionPort


class DeleteSeccion:
    def __init__(self, repo: SeccionPort):
        self.repo = repo

    async def execute(self, seccion_id: int) -> None:
        return await self.repo.delete_seccion(seccion_id)
