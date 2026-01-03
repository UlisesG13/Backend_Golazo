from src.api.schemas.seccion_dto import SeccionDTO, SeccionCreateDTO, SeccionUpdateDTO
from src.domain.models.seccion_model import SeccionModel
from src.domain.ports.seccion_port import SeccionPort

class SeccionUsecases:
    def __init__(self, repo: SeccionPort):
        self.repo = repo

    def get_secciones(self) -> list[SeccionModel]:
        return self.repo.get_secciones()

    def get_seccion_by_id(self, seccion_id: int) -> SeccionModel:
        seccion = self.repo.get_seccion_by_id(seccion_id)
        if not seccion:
            raise ValueError(f"Seccion con id {seccion_id} no encontrada")
        return seccion

    def create_seccion(self, dto: SeccionCreateDTO) -> SeccionModel:
        seccion = SeccionModel(
            seccion_id=0,
            nombre=dto.nombre
        )
        return self.repo.create_seccion(seccion)

    def update_seccion(self, seccion_id: int, dto: SeccionUpdateDTO) -> SeccionModel:
        existing = self.repo.get_seccion_by_id(seccion_id)
        if not existing:
            raise ValueError(f"Seccion con id {seccion_id} no encontrada")

        updated = SeccionModel(
            seccion_id=seccion_id,
            nombre=dto.nombre
        )
        return self.repo.update_seccion(seccion_id, updated)

    def delete_seccion(self, seccion_id: int) -> None:
        existing = self.repo.get_seccion_by_id(seccion_id)
        if not existing:
            raise ValueError(f"Seccion con id {seccion_id} no encontrada")

        self.repo.delete_seccion(seccion_id)
