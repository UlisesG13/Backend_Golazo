from src.api.schemas.categoria_dto import CategoriaDTO, CategoriaCreateDTO, CategoriaUpdateDTO
from src.domain.models.categoria_model import CategoriaModel
from src.domain.ports.categoria_port import CategoriaPort

class CategoriaUsecases:
    def __init__(self, repo: CategoriaPort):
        self.repo = repo

    def get_categorias(self) -> list[CategoriaModel]:
        return self.repo.get_categorias()
    
    def get_categoria_by_id(self, categoria_id: int) -> CategoriaModel:
        categoria = self.repo.get_categoria_by_id(categoria_id)
        if not categoria:
            raise ValueError(f"Categoria con id {categoria_id} no encontrada")
        return categoria

    def get_categorias_by_seccion_id(self, seccion_id: int) -> list[CategoriaModel]:
        return self.repo.get_categorias_by_seccion(seccion_id)
    
    def create_categoria(self, dto: CategoriaCreateDTO) -> CategoriaModel:
        categoria = CategoriaModel(
            categoria_id=0,
            nombre=dto.nombre,
            seccion_id=dto.seccion_id
        )
        return self.repo.create_categoria(categoria)

    def update_categoria(self, categoria_id: int, dto: CategoriaUpdateDTO) -> CategoriaModel:
        existing = self.repo.get_categoria_by_id(categoria_id)
        if not existing:
            raise ValueError(f"Categoria con id {categoria_id} no encontrada")

        updated = CategoriaModel(
            categoria_id=categoria_id,
            nombre=dto.nombre,
            seccion_id=dto.seccion_id
        )
        return self.repo.update_categoria(categoria_id, updated)

    def delete_categoria(self, categoria_id: int) -> None:
        existing = self.repo.get_categoria_by_id(categoria_id)
        if not existing:
            raise ValueError(f"Categoria con id {categoria_id} no encontrada")

        self.repo.delete_categoria(categoria_id)
