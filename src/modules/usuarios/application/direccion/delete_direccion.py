from src.modules.usuarios.domain.ports import DireccionPort

class DeleteDireccion:
    def __init__(self, repo: DireccionPort) -> None:
        self.repo = repo

    def execute(self, direccion_id: int, usuario_id: str) -> None:
        direccion = self.repo.get_direccion_by_id(direccion_id, usuario_id)
        if not direccion:
            raise ValueError(f"Dirección con ID {direccion_id} no encontrada")
        return self.repo.delete_direccion(direccion_id, usuario_id)