from src.modules.ventas.domain import PromocionModel, PromocionPort


class GetAll:
    def __init__(self, repo: PromocionPort):
        self.repo = repo

    def execute(self) -> list[PromocionModel]:
        return self.repo.get_all()