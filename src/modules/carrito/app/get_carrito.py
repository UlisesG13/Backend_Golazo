from datetime import datetime
from uuid import uuid4

from src.modules.carrito.domain import CarritoPort, CarritoModel


class GetCartUseCase:
    def __init__(self, repo: CarritoPort):
        self.repo = repo

    async def execute(self, usuario_id: str) -> CarritoModel:
        carrito = await self.repo.get_by_user_id(usuario_id)
        if not carrito:
            # si no existe un carrito lo crea
            carrito = CarritoModel(
                carrito_id=str(uuid4()),
                usuario_id=usuario_id,
                fecha_creacion=datetime.now(),
                fecha_actualizacion=datetime.now(),
                items=[]
            )
            await self.repo.save(carrito)  # persistir inmediatamente

        return carrito
