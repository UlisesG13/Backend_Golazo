from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from src.modules.carrito.domain import CarritoPort
from src.modules.carrito.domain.carrito_model import CarritoModel, CarritoItemModel
from src.modules.carrito.infra.carrito_table import CarritoTable, CarritoItemTable


def to_domain(table: CarritoTable) -> CarritoModel:
    return CarritoModel(
        carrito_id=table.carrito_id,
        usuario_id=table.usuario_id,
        fecha_creacion=table.fecha_creacion,
        fecha_actualizacion=table.fecha_actualizacion,
        # Mapeamos los ítems de la tabla a modelos de dominio
        items=[
            CarritoItemModel(
                carrito_item_id=item.carrito_item_id,
                producto_id=item.producto_id,
                color_id=item.color_id,
                talla_id=item.talla_id,
                cantidad=item.cantidad,
                precio_unitario=float(item.precio_unitario)
            ) for item in table.items
        ]
    )


class CarritoRepository(CarritoPort):
    def __init__(self, session: Session):
        self.session = session

    def get_by_user_id(self, user_id: str) -> CarritoModel | None:
        # Usamos joinedload para traer los ítems en una sola consulta (Eager Loading)
        stmt = select(CarritoTable).where(CarritoTable.usuario_id == user_id).options(
            joinedload(CarritoTable.items)
        )
        result = self.session.execute(stmt).unique().scalar_one_or_none()

        if not result:
            return None

        return to_domain(result)

    def save(self, model: CarritoModel):
        carrito_db = self.session.get(CarritoTable, model.carrito_id)

        if not carrito_db:
            carrito_db = CarritoTable(carrito_id=model.carrito_id, usuario_id=model.usuario_id)
            self.session.add(carrito_db)

        # 1. Creamos un diccionario con los ítems que ya existen en la DB para comparar rápido
        # La clave es la combinación que causa el error: (prod, color, talla)
        existentes = {
            (item.producto_id, item.color_id, item.talla_id): item
            for item in carrito_db.items
        }

        # 2. Lista para los ítems finales
        nuevos_items_db = []

        for item_dominio in model.items:
            key = (item_dominio.producto_id, item_dominio.color_id, item_dominio.talla_id)

            if key in existentes:
                # SI YA EXISTE: Actualizamos el objeto existente en lugar de crear uno nuevo
                item_db = existentes[key]
                item_db.cantidad = item_dominio.cantidad
                item_db.precio_unitario = item_dominio.precio_unitario
                nuevos_items_db.append(item_db)
            else:
                # SI ES NUEVO: Creamos la instancia
                nuevo_item_db = CarritoItemTable(
                    producto_id=item_dominio.producto_id,
                    color_id=item_dominio.color_id,
                    talla_id=item_dominio.talla_id,
                    cantidad=item_dominio.cantidad,
                    precio_unitario=item_dominio.precio_unitario
                )
                nuevos_items_db.append(nuevo_item_db)

        # 3. Asignamos la lista sincronizada
        carrito_db.items = nuevos_items_db

        self.session.commit()
        return model

    def delete(self, cart_id: str) -> None:
        carrito = self.session.get(CarritoTable, cart_id)
        if carrito:
            self.session.delete(carrito)
            self.session.commit()