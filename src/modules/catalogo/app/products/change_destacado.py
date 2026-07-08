from src.core.exceptions import NotFoundError
from src.modules.catalogo.domain.models import ProductoModel
from src.modules.catalogo.domain.ports import ProductoPort


class ChangeDestacado:
    def __init__(self, repo: ProductoPort):
        self.repo = repo

    async def execute(self, producto_id: str, destacado: bool) -> ProductoModel:
        producto = await self.repo.get_by_id(producto_id)
        if not producto:
            raise NotFoundError(f"Producto {producto_id} no existe")
        producto.esta_destacado = destacado
        return await self.repo.update_producto(producto_id, producto)
