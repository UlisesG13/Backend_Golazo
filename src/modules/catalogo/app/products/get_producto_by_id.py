from typing import List, Optional

from src.modules.catalogo.app.images.get_images import GetImages
from src.modules.catalogo.domain.models import ProductoModel
from src.modules.catalogo.domain.ports import ProductoPort

class GetProductoById:
    def __init__(self, repo: ProductoPort, uc: GetImages):
        self.repo = repo
        self.img_uc = uc

    def execute(self, producto_id: str) -> Optional[ProductoModel]:
        producto = self.repo.get_by_id(producto_id)
        if not producto:
            return None
        producto.imagenes = self.img_uc.execute(producto_id)
        return producto
