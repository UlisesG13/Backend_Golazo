from dataclasses import dataclass

@dataclass
class CategoriaModel:
    categoria_id: int | None
    name: str
    seccion_id: int