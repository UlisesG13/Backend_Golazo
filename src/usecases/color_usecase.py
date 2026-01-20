from src.api.schemas.color_dto import ColorCreateDTO, ColorUpdateDTO
from src.domain.models.color_model import ColorModel
from src.domain.ports.color_port import ColorPort

class ColorUsecases:
    def __init__(self, repo: ColorPort):
        self.repo = repo

    def create_color(self, dto: ColorCreateDTO) -> ColorModel:
        color = ColorModel(
            color_id=0,  # El ID será asignado por la base de datos
            nombre=dto.nombre
        )
        return self.repo.create_color(color)

    def get_color_by_id(self, color_id: int) -> ColorModel:
        return self.repo.get_color_by_id(color_id)
    
    def get_all_colors(self) -> list[ColorModel]:
        return self.repo.get_all_colors()
    
    def update_color(self, color_id: int, dto: ColorUpdateDTO) -> ColorModel:
        color = self.repo.get_color_by_id(color_id)  # si no lo encuentra lanza NotFoundError desde el repositorio
        if dto.nombre is not None:
            color.nombre = dto.nombre
        return self.repo.update_color(color_id, color)
    
    def delete_color(self, color_id: int) -> bool:
        return self.repo.delete_color(color_id)
