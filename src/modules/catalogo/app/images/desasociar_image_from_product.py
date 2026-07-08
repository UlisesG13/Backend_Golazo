from src.modules.catalogo.domain.ports import ProductImagePort

class DesasociarImageFromProduct:
    def __init__(self, producto_imagen_repo: ProductImagePort):
        self.producto_imagen_repo = producto_imagen_repo

    async def execute(self, producto_id: str, imagen_id: int) -> None:
        await self.producto_imagen_repo.delete(producto_id, imagen_id)
