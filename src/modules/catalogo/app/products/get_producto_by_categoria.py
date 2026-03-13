from typing import List
from src.modules.catalogo.domain.models import ProductoModel
from src.modules.catalogo.domain.ports import ProductoPort


class GetProductoByCategoria:
    def __init__(self, repo: ProductoPort):
        self.repo = repo

    def execute(self, categoria_id: int) -> List[ProductoModel]:
        return self.repo.get_by_categoria(categoria_id)