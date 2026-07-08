from src.modules.catalogo.domain.ports import ProductoPort

class DeleteProducto:
    def __init__(self, repo: ProductoPort):
        self.repo = repo

    async def execute(self, producto_id: str):
        return await self.repo.delete_producto(producto_id)
