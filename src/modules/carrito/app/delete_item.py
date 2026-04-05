from src.modules.carrito.domain import CarritoPort, CarritoModel


class RemoveItemUseCase:
    def __init__(self, repo: CarritoPort):
        self.repo = repo

    def execute(self, usuario_id: str, item_id: int) -> CarritoModel:
        # 1. Obtenemos el carrito completo del usuario
        carrito = self.repo.get_by_user_id(usuario_id)
        if not carrito:
            raise Exception("Carrito no encontrado")

        # 2. Filtramos la lista basándonos SOLO en el ID único del ítem
        # Esto es mucho más seguro y rápido que comparar 3 campos
        carrito.items = [
            i for i in carrito.items
            if i.carrito_item_id != item_id
        ]

        # 3. Guardamos el estado actual.
        # SQLAlchemy detectará que falta un ítem en la lista y lo borrará de la DB.
        return self.repo.save(carrito)