from datetime import datetime
from uuid import uuid4
from src.api.schemas.carrito_dto import CreateCarritoDTO, UpdateCarritoDTO, CarritoDTO
from src.domain.models.carrito_model import CarritoModel
from src.domain.ports.carrito_port import CarritoPort

class CarritoUseCases:
    def __init__(self, repo: CarritoPort):
        self.repo = repo
    
    def get_carrito_by_user_id(self, user_id: str) -> CarritoModel:
        carrito_model = self.repo.get_by_user_id(user_id)
        if not carrito_model:
            raise ValueError(f"Carrito para el usuario con ID {user_id} no encontrado")
        return carrito_model
    
    def create_carrito(self, dto: CreateCarritoDTO) -> CarritoModel:
        carrito_model = CarritoModel(
            carrito_id=str(uuid4()),
            usuario_id=dto.usuario_id
        )
        return self.repo.create_carrito(carrito_model)

    def update_carrito(self, dto: UpdateCarritoDTO) -> CarritoModel:
        existing_carrito = self.repo.get_by_user_id(dto.usuario_id)
        updated_data = CarritoModel(
            fecha_actualizacion=datetime.now()
        )
        return self.repo.udate_carrito(existing_carrito.carrito_id, updated_data)
        
    def delete_carrito(self, usuario_id: str) -> None:
        existing_carrito = self.repo.get_by_user_id(usuario_id)
        carrito_id = existing_carrito.carrito_id
        return self.repo.delete_carrito(carrito_id)