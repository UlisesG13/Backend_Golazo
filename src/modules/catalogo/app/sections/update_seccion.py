from src.core.exceptions import NotFoundError
from src.modules.catalogo.domain.ports import SeccionPort
from src.modules.catalogo.domain.models import SeccionModel
from src.modules.catalogo.presentation.section.seccion_dto import SeccionUpdate


class UpdateSeccion:
    def __init__(self, repo: SeccionPort):
        self.repo = repo

    async def execute(self, seccion_id: int, dto: SeccionUpdate) -> SeccionModel | None:
        seccion = await self.repo.get_seccion_by_id(seccion_id)
        if not seccion:
            raise NotFoundError(f'Seccion {seccion_id} no existe')
        seccion.nombre = dto.nombre
        return await self.repo.update_seccion(seccion_id, seccion)
