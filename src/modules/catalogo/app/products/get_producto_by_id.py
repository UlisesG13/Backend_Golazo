from src.modules.catalogo.domain.models import ProductoModel
from src.modules.catalogo.domain.ports import ProductoPort


class GetProductoById:
    def __init__(self, repo: ProductoPort):
        self.repo = repo

    def execute(self, producto_id: str) -> ProductoModel:
        return self.repo.get_by_id(producto_id)