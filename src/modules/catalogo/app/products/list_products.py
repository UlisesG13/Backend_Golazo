
from src.modules.catalogo.app.images import GetImages
from src.modules.catalogo.app.sizes import GetTallasByProducto
from src.modules.catalogo.domain.models import ProductoModel
from src.modules.catalogo.domain.ports import ProductoPort


class ListProducts:
    def __init__(self, repo: ProductoPort, img_uc: GetImages, tallas_uc: GetTallasByProducto):
        self.repo = repo
        self.img_uc = img_uc
        self.tallas_uc = tallas_uc

    def execute(self) -> list[ProductoModel]:
        productos = self.repo.get_all()

        for p in productos:
            p.imagenes = self.img_uc.execute(p.producto_id)
            p.tallas = self.tallas_uc.execute(p.producto_id)

        return productos