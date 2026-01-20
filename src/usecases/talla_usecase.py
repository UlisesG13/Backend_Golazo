from src.api.schemas.talla_dto import TallaCreateDTO, TallaUpdateDTO
from src.domain.models.talla_model import TallaModel
from src.domain.ports.talla_port import TallaPort

class TallaUsecases:
    def __init__(self, repo: TallaPort):
        self.repo = repo

    def create_talla(self, dto: TallaCreateDTO) -> TallaModel:
        talla = TallaModel(
            nombre=dto.nombre
        )
        return self.repo.create_talla(talla)

    def get_talla_by_id(self, talla_id: int) -> TallaModel:
        return self.repo.get_talla_by_id(talla_id)

    def get_all_tallas(self) -> list[TallaModel]:
        return self.repo.get_all_tallas()

    def update_talla(self, talla_id: int, dto: TallaUpdateDTO) -> TallaModel:
        talla = self.repo.get_talla_by_id(talla_id)
        if dto.nombre is not None:
            talla.nombre = dto.nombre
        return self.repo.update_talla(talla_id, talla)

    def delete_talla(self, talla_id: int) -> bool:
        return self.repo.delete_talla(talla_id)
