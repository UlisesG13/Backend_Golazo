from src.modules.ventas.domain import FacturaPort, FacturaModel


class GetAll:
    def __init__(self, repo: FacturaPort):
        self.repo = repo

    def execute(self) -> list[FacturaModel]:
        return self.repo.get_all()
