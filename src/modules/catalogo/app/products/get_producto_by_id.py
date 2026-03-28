from src.modules.catalogo.app.images.get_images import GetImages
from src.modules.catalogo.app.sizes import GetTallasByProducto
from src.modules.catalogo.domain.models import ProductoModel
from src.modules.catalogo.domain.ports import ProductoPort

class GetProductoById:
    def __init__(self, repo: ProductoPort, uc: GetImages, tallas_uc: GetTallasByProducto):
        self.repo = repo
        self.img_uc = uc
        self.tallas_uc = tallas_uc

    def execute(self, producto_id: str) -> ProductoModel | None:
        producto = self.repo.get_by_id(producto_id)
        if not producto:
            return None
        producto.imagenes = self.img_uc.execute(producto_id) # obtener imagenes
        producto.tallas = self.tallas_uc.execute(producto_id) # obtener tallas
        return producto
