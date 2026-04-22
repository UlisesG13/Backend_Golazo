from src.modules.carrito.domain import CarritoPort, CarritoModel


class UpdateQuantityUseCase:
    def __init__(self, repo: CarritoPort):
        self.repo = repo

    def execute(self, usuario_id: str, item_id: int, nueva_cantidad: int) -> CarritoModel:
        # 1. Validamos que la cantidad sea lógica
        if nueva_cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero. Use eliminar para quitar el producto.")

        # 2. Obtenemos el carrito
        carrito = self.repo.get_by_user_id(usuario_id)
        if not carrito:
            raise Exception("Carrito no encontrado")

        # 3. Buscamos el ítem dentro de la lista del modelo de dominio
        item = next((i for i in carrito.items if i.carrito_item_id == item_id), None)

        if not item:
            raise Exception("El ítem no pertenece a este carrito")

        # 4. Actualizamos la cantidad en el objeto de dominio
        item.cantidad = nueva_cantidad

        # 5. Persistimos el cambio
        # El repositorio detectará el cambio en el objeto y hará el UPDATE en la BD
        return self.repo.save(carrito)