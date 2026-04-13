from src.modules.usuarios.presentation.schemas import DireccionRequestDTO
from src.modules.usuarios.domain.models import DireccionModel
from src.modules.usuarios.domain.ports import DireccionPort

class CreateDireccion:
    def __init__(self, repo: DireccionPort) -> None:
        self.repo = repo

    def execute(self, usuario_id: str, dto: DireccionRequestDTO) -> DireccionModel:
        model = DireccionModel(
            direccion_id=None, # La base de datos generara el ID
            calle=dto.calle,
            colonia=dto.colonia,
            calle_uno=dto.calle_uno,
            calle_dos=dto.calle_dos,
            numero_casa=dto.numero_casa,
            codigo_postal=dto.codigo_postal,
            referencia=dto.referencia,
            usuario_id=usuario_id,
            is_primary=dto.is_primary
        )
        return self.repo.create_direccion(model)