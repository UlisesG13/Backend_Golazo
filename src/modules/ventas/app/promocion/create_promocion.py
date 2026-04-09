from src.modules.ventas.domain import PromocionPort, PromocionModel
from src.modules.ventas.infra.promocion.promocion_table import TipoDescuento
from src.modules.ventas.presentation.promocion.promocion_dto import PromocionCreateDTO


class CreatePromocion:
    def __init__(self, repo: PromocionPort):
        self.repo = repo

    def execute(self, dto: PromocionCreateDTO) -> PromocionModel:
        # 0. Validación elegante usando el Enum
        # Esto verifica si el valor enviado está entre ("porcentaje", "monto_fijo")
        if dto.tipo_descuento not in [t.value for t in TipoDescuento]:
            validos = [t.value for t in TipoDescuento]
            raise ValueError(f"Tipo de promoción '{dto.tipo_descuento}' no es válido. Opciones: {validos}")

        # 1. Instanciamos el modelo con los datos del DTO
        nueva_promocion = PromocionModel(
            promocion_id=None,  # Se generará en la BD
            codigo=dto.codigo.upper(),  # Normalizamos el código
            descuento=dto.descuento,
            tipo_descuento=dto.tipo_descuento,
            contador_usos=0,
            usos_maximos=dto.usos_maximos,
            fecha_inicio=dto.fecha_inicio,
            fecha_expiracion=dto.fecha_expiracion,
            esta_activa=False  # Por defecto, la promoción se crea como inactiva
        )

        # 2. Validaciones de Regla de Negocio
        if not nueva_promocion.date_is_valid():
            raise ValueError("La fecha de inicio debe ser anterior a la de expiración.")

        # 3. Verificación de duplicados
        if self.repo.get_by_codigo(nueva_promocion.codigo):
            raise ValueError(f"Ya existe una promoción con el código {nueva_promocion.codigo}")

        # 4. Guardamos
        return self.repo.create(nueva_promocion)
