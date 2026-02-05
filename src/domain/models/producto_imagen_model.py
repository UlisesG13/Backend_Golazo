from dataclasses import dataclass

@dataclass
class ProductoImagenModel:
    producto_imagen_id: int
    producto_id: str
    imagen_id: int
    es_principal: bool