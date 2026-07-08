from src.modules.carrito.domain import CarritoPort


class RemoveCartUseCase:
    def __init__(self, port: CarritoPort):
        self.repo = port

    async def execute(self, cart_id: str):
        return await self.repo.delete(cart_id)
