from src.modules.usuarios.presentation.schemas import UserUpdateDTO
from src.modules.usuarios.domain.models import UserModel
from src.modules.usuarios.domain.ports import UserPort

class UpdateUser:
    def __init__(self, repo: UserPort):
        self.user_repository = repo

    def execute(self, usuario_id: str, dto: UserUpdateDTO) -> UserModel:
        user = self.user_repository.get_by_id(usuario_id)
        if not user:
            raise ValueError("Usuario no encontrado")

        if dto.nombre is not None:
            user.nombre = dto.nombre

        if dto.telefono is not None:
            user.telefono = dto.telefono

        return self.user_repository.update(usuario_id, user)