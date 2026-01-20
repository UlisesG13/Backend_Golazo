from src.api.schemas.producto_color_dto import ProductoColorCreateDTO
from src.domain.models.producto_color_model import ProductoColorModel
from src.domain.ports.producto_color_port import ProductoColorPort

class ProductoColorUsecases:
    def __init__(self, repo: ProductoColorPort):
        self.repo = repo

    def assign_color_to_producto(self, p_color: ProductoColorCreateDTO) -> ProductoColorModel:
        return self.repo.assign_color_to_producto(p_color)
    
    def get_colors_by_producto(self, producto_id: str) -> list[ProductoColorModel]:
        return self.repo.get_colors_by_producto(producto_id)
    
    def remove_color_from_producto(self, producto_id: str, color_id: int) -> bool:
        return self.repo.remove_color_from_producto(producto_id, color_id)
    
    def get_producto_color_by_id(self, producto_color_id: int) -> ProductoColorModel:
        return self.repo.get_producto_color_by_id(producto_color_id)