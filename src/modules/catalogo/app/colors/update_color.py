from src.core.exceptions import NotFoundError
from src.modules.catalogo.domain.models import ColorModel
from src.modules.catalogo.domain.ports import ColorPort
from src.modules.catalogo.presentation.colors.color_dto import ColorUpdateDTO


class UpdateColor:
    def __init__(self, repo: ColorPort):
        self.repo = repo

    async def execute(self, color_id: int, dto: ColorUpdateDTO) -> ColorModel:
        current = await self.repo.get_by_id(color_id)
        if not current:
            raise NotFoundError(f"Color id {color_id} no existe")
        current.nombre = dto.nombre
        return await self.repo.update(color_id, current)
