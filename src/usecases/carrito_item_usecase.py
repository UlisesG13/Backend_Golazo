from datetime import datetime
from uuid import uuid4
from src.domain.ports.carrito_item_port import CarritoItemPort
from src.api.schemas.carrito_item_dto import CarritoItemCreateDTO, CarritoItemUpdateDTO
from src.domain.models.carrito_item_model import CarritoItemModel

class CarritoItemUseCases:
    def __init__(self, repo: CarritoItemPort):
        self.repo = repo

    def get_items_by_carrito_id(self, carrito_id: str) -> list[CarritoItemModel]:
        items = self.repo.get_items_by_carrito_id(carrito_id)
        return items

    def add_item_to_carrito(self, carrito_id: str, dto: CarritoItemCreateDTO) -> CarritoItemModel:
        item_model = CarritoItemModel(
            carrito_item_id=str(uuid4()),
            carrito_id=carrito_id,
            producto_id=dto.producto_id,
            color_id=dto.color_id,
            talla_id=dto.talla_id,
            cantidad=dto.cantidad,
            precio_unitario=dto.precio_unitario
        )
        return self.repo.add_item_to_carrito(carrito_id, item_model)
    
    def remove_item_from_carrito(self, carrito_id: str, item_id: str) -> None:
        self.repo.remove_item_from_carrito(carrito_id, item_id)

    def update_item_in_carrito(self, carrito_id: str, item_id: str, dto: CarritoItemUpdateDTO) -> CarritoItemModel:
        updated_item_model = CarritoItemModel(
            carrito_item_id=item_id,
            producto_id=dto.producto_id,
            color_id=dto.color_id,
            talla_id=dto.talla_id,
            cantidad=dto.cantidad,
            precio_unitario=dto.precio_unitario
        )
        return self.repo.update_item_in_carrito(carrito_id, item_id, updated_item_model)