from dataclasses import dataclass

@dataclass
class DireccionModel:
    direccion_id: int
    calle: str
    colonia: str
    calle_uno: str | None
    calle_dos: str | None
    numero_casa: int | None
    codigo_postal: str | None
    referencia: str | None
    usuario_id: str
    is_primary: bool