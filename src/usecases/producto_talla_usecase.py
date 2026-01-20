from src.api.schemas.producto_talla_dto import ProductoTallaCreateDTO
from src.domain.models.producto_talla_model import ProductoTallaModel
from src.domain.ports.producto_talla_port import ProductoTallaPort

class ProductoTallaUsecases:
    def __init__(self, repo: ProductoTallaPort):
        self.repo = repo

    def assign_talla_to_producto(self, p_talla: ProductoTallaCreateDTO) -> ProductoTallaModel:
        return self.repo.assign_talla_to_producto(p_talla)
    
    def get_tallas_by_producto(self, producto_id: str) -> list[ProductoTallaModel]:
        return self.repo.get_tallas_by_producto(producto_id)
    
    def remove_talla_from_producto(self, producto_id: str, color_id: int) -> bool:
        return self.repo.remove_talla_from_producto(producto_id, color_id)
    
    def get_producto_talla_by_id(self, producto_color_id: int) -> ProductoTallaModel:
        return self.repo.get_producto_talla_by_id(producto_color_id)