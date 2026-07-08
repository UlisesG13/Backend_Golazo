from src.modules.catalogo.domain.models import SeccionModel
from src.modules.catalogo.domain.ports import SeccionPort
from src.modules.catalogo.presentation.section.seccion_dto import SeccionCreate


class CreateSeccion:
    def __init__(self, repo: SeccionPort):
        self.repo = repo

    async def execute(self, dto: SeccionCreate) -> SeccionModel:
        seccion = SeccionModel(
            seccion_id=None,
            nombre=dto.nombre,
        )
        return await self.repo.create_seccion(seccion)
