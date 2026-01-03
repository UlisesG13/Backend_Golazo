from dataclasses import dataclass

@dataclass
class CategoriaModel:
    categoria_id: int
    seccion_id: int
    nombre: str