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
            # Lógica para inicializar un CarritoModel nuevo
            pass

        producto = self.producto_repo.get_by_id(dto.producto_id)

        if not producto:
            raise Exception("Producto no encontrado")

        nuevo_item: CarritoItemModel = CarritoItemModel(
            carrito_item_id=None,
            producto_id=dto.producto_id,
            color_id=dto.color_id,
            cantidad=dto.cantidad,
            talla_id=dto.talla_id,
            precio_unitario=producto.precio
        )
        # 2. Buscar si el ítem ya existe en el carrito
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

        # 3. Persistir el agregado completo
        return self.repo.save(carrito)
