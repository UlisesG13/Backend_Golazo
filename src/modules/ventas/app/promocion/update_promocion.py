from src.modules.ventas.domain import PromocionPort, PromocionModel


class UpdatePromocion:
    def __init__(self, repo: PromocionPort):
        self.repo = repo

    def execute(self, promocion_id: int, dto) -> PromocionModel:
        # 1. Recuperar la entidad existente
        current = self.repo.get_by_id(promocion_id)
        if not current:
            raise ValueError(f"Promocion {promocion_id} no existe")

        # 2. Actualizar los campos permitidos desde el DTO
        current.codigo = dto.codigo.upper() if dto.codigo else current.codigo
        current.descuento = dto.descuento
        current.tipo_descuento = dto.tipo_descuento
        current.usos_maximos = dto.usos_maximos
        current.fecha_inicio = dto.fecha_inicio
        current.fecha_expiracion = dto.fecha_expiracion
        current.esta_activa = dto.esta_activa

        # 3. Validar consistencia tras la actualización
        # Si al mover las fechas la de inicio queda después de la de fin, lanzamos error
        if not current.date_is_valid():
            raise ValueError("Error de consistencia: La fecha de inicio no puede ser posterior a la de expiración.")

        # 4. Verificar si el nuevo código (si cambió) ya está tomado por otra promoción
        existing = self.repo.get_by_codigo(current.codigo)
        if existing and existing.promocion_id != promocion_id:
            raise ValueError(f"El código {current.codigo} ya está siendo usado por otra promoción.")

        # 5. Guardar cambios
        return self.repo.update(current)