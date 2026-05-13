from uuid import uuid4
from datetime import datetime
from src.modules.carrito.domain import CarritoModel, CarritoPort, CarritoItemModel
from src.modules.carrito.presentation.carrito_dto import AddItemRequest
from src.modules.catalogo.domain.ports import ProductoPort


class AddItemUseCase:
    def __init__(self, repo: CarritoPort, producto_repo: ProductoPort):
        self.repo = repo
        self.producto_repo = producto_repo

    def execute(self, usuario_id: str, dto: AddItemRequest) -> CarritoModel:
        carrito = self.repo.get_by_user_id(usuario_id)

        if not carrito:
            carrito = CarritoModel(
                carrito_id=str(uuid4()),
                usuario_id=usuario_id,
                fecha_creacion=datetime.now(),
                fecha_actualizacion=datetime.now(),
                items=[]
            )
            carrito = self.repo.save(carrito)  # persistir inmediatamente

        producto = self.producto_repo.get_by_id(dto.producto_id)

        if not producto:
            raise Exception("Producto no encontrado")

        # Validación de Stock Dinámico
        if producto.stock != 0:
            cantidad_total = dto.cantidad
            item_existente = next((
                item for item in carrito.items
                if item.producto_id == dto.producto_id
                and item.color_id == dto.color_id
                and item.talla_id == dto.talla_id
            ), None)
            
            if item_existente:
                cantidad_total += item_existente.cantidad
                
            if cantidad_total > producto.stock:
                raise ValueError(f"No hay suficiente stock. Límite disponible: {producto.stock}")

        nuevo_item = CarritoItemModel(
            carrito_item_id=None,
            producto_id=dto.producto_id,
            color_id=dto.color_id,
            cantidad=dto.cantidad,
            talla_id=dto.talla_id,
            precio_unitario=producto.precio
        )

        item_existente = next((
            item for item in carrito.items
            if item.producto_id == nuevo_item.producto_id
            and item.color_id == nuevo_item.color_id
            and item.talla_id == nuevo_item.talla_id
        ), None)

        if item_existente:
            item_existente.cantidad += nuevo_item.cantidad
        else:
            carrito.items.append(nuevo_item)

        carrito.fecha_actualizacion = datetime.now()

        return self.repo.save(carrito)