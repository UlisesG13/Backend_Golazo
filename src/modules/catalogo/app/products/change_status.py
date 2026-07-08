from src.core.exceptions import NotFoundError
from src.modules.catalogo.domain.models import ProductoModel
from src.modules.catalogo.domain.ports import ProductoPort


class ChangeStatus:
    def __init__(self, repo: ProductoPort):
        self.repo = repo

    async def execute(self, producto_id: str, status: bool) -> ProductoModel:
        producto = await self.repo.get_by_id(producto_id)
        if not producto:
            raise NotFoundError(f"Producto {producto_id} no existe")
        producto.esta_activo = status
        return await self.repo.update_producto(producto_id, producto)
