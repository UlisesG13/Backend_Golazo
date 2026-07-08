from src.core.exceptions import NotFoundError
from src.modules.catalogo.domain.models import ColorModel
from src.modules.catalogo.domain.ports import ColorPort


class GetColorById:
    def __init__(self, repo: ColorPort):
        self.repo = repo

    async def execute(self, color_id: int) -> ColorModel:
        current = await self.repo.get_by_id(color_id)
        if not current:
            raise NotFoundError(f"Color id {color_id} no existe")
        return current
