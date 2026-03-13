from typing import List

from src.modules.catalogo.app.images.get_images import GetImages
from src.modules.catalogo.domain.models import ProductoModel
from src.modules.catalogo.domain.ports import ProductoPort


class ListProducts:
    def __init__(self, repo: ProductoPort, uc: GetImages):
        self.repo = repo
        self.img_uc = uc

    def execute(self) -> List[ProductoModel]:
        productos = self.repo.get_all()

        for p in productos:
            p.imagenes = self.img_uc.execute(p.producto_id)
        return productos