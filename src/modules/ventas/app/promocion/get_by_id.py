from src.modules.ventas.domain import PromocionModel, PromocionPort


class GetById:
    def __init__(self, repo: PromocionPort):
        self.repo = repo

    def execute(self, promocion_id: int) -> PromocionModel:
        model = self.repo.get_by_id(promocion_id)
        if not model:
            raise ValueError(f"Promocion {promocion_id} no existe")
        return model
