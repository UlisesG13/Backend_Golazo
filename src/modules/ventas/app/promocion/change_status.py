from src.modules.ventas.domain import PromocionModel, PromocionPort


class ChangeStatus:
    def __init__(self, repo: PromocionPort):
        self.repo = repo

    def execute(self,promocion_id: int, status: bool) -> PromocionModel | None:
        current = self.repo.get_by_id(promocion_id)
        if not current:
            raise ValueError(f"Promocion {promocion_id} no existe")
        current.status = status
        return current