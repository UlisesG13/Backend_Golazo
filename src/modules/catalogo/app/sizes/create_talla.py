from src.modules.catalogo.domain.models import TallaModel
from src.modules.catalogo.domain.ports import TallaPort
from src.modules.catalogo.presentation.sizes.talla_dto import TallaCreateDTO


class CreateTalla:
    def __init__(self, repo: TallaPort):
        self.repo = repo

    async def execute(self, dto: TallaCreateDTO) -> TallaModel:
        model = TallaModel(
            talla_id=None,
            nombre=dto.nombre
        )
        return await self.repo.create(model)
