from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class PromocionModel:
    promocion_id: int | None
    codigo: str
    descuento: float
    tipo_descuento: str  # Sugerencia: "PORCENTAJE" o "FIJO"
    contador_usos: int
    usos_maximos: int
    fecha_inicio: datetime
    fecha_expiracion: datetime
    esta_activa: bool

    def date_is_valid(self) -> bool:
        return self.fecha_inicio < self.fecha_expiracion

    def is_expired(self, now: datetime) -> bool:
        return now > self.fecha_expiracion

    def has_uses_left(self) -> bool:
        return self.contador_usos < self.usos_maximos

    def is_available(self, now: datetime) -> bool:
        """Verifica todas las condiciones de negocio."""
        return (
                self.esta_activa and
                self.date_is_valid() and
                not self.is_expired(now) and
                now >= self.fecha_inicio and
                self.has_uses_left()
        )

    def calculate_discount_amount(self, total_amount: float) -> float:
        """Calcula el monto a restar basado en el tipo de descuento."""
        if self.tipo_descuento == "PORCENTAJE":
            # Aseguramos que el descuento no sea negativo y aplicamos %
            return max(0.0, total_amount * (self.descuento / 100))

        elif self.tipo_descuento == "FIJO":
            # No podemos descontar más de lo que vale el producto
            return min(max(0.0, self.descuento), total_amount)

        return 0.0

    def apply_usage(self):
        """Method auxiliar para registrar un uso de forma controlada."""
        if self.has_uses_left():
            self.contador_usos += 1
        else:
            raise ValueError("La promoción ha alcanzado su límite de usos.")


@dataclass
class PedidoItemModel:
    pedido_item_id: int | None
    pedido_id: int | None
    producto_id: str
    nombre_producto: str
    color_id: int
    talla_id: int
    cantidad: int
    precio_unitario: float

    @property
    def subtotal(self) -> float:
        return self.cantidad * self.precio_unitario

@dataclass
class PedidoModel:
    pedido_id: int | None
    usuario_id: str
    promocion_id: int | None
    estado: str
    fecha_pedido: datetime
    fecha_actualizacion: datetime

    subtotal: float
    descuento: float
    total: float

    notas: str
    direccion: dict
    items: list[PedidoItemModel] = field(default_factory=list)