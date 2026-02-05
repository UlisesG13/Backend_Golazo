from typing import List
from src.api.schemas.imagen_dto import ProductoImagenCreateDTO
from src.domain.ports.imagen_port import ImagenPort
from src.domain.ports.producto_imagen_port import ProductoImagenPort
from src.domain.ports.image_storage_port import ImagenStoragePort
from src.domain.models.imagen_model import ImagenModel
from src.domain.models.producto_imagen_model import ProductoImagenModel

class ImagenUsecases:
    def __init__(self, imagenDB: ImagenPort, productoImagenDB: ProductoImagenPort, storage: ImagenStoragePort):
        self.imagenRepository = imagenDB
        self.productoImagenRepository = productoImagenDB
        self.storage = storage

    def subir_imagen(self, imagen_data: bytes, filename: str, orden: int) -> ImagenModel:
        path = f"productos/{filename}"
        self.storage.upload(imagen_data, path)
        imagen = ImagenModel(
            imagen_id=None,
            path=path,
            orden=orden
        )
        return self.imagenRepository.create(imagen)
    
    def eliminar_imagen(self, imagen_id: int) -> None:
        imagen = self.imagenRepository.get_by_id(imagen_id)
        if not imagen:
            return
        self.storage.delete(imagen.path)
        self.imagenRepository.delete(imagen_id)

    def asociar_imagen_a_producto(self, dto: ProductoImagenCreateDTO) -> ProductoImagenModel:
        producto_imagen = ProductoImagenModel(
            producto_imagen_id=None,
            producto_id=dto.producto_id,
            imagen_id=dto.imagen_id,
            es_principal=dto.es_principal
        )
        return self.productoImagenRepository.create(producto_imagen)
    
    def desasociar_imagen_de_producto(self, producto_id: str, imagen_id: int) -> None:
        self.productoImagenRepository.delete(producto_id, imagen_id)

    def get_imagenes_por_producto(self, producto_id: str) -> list[ImagenModel]:
        relaciones = self.productoImagenRepository.get_by_producto(producto_id)

        imagenes: List[ImagenModel] = []

        for rel in relaciones:
            imagen = self.imagenRepository.get_by_id(rel.imagen_id)
            if imagen:
                imagenes.append(imagen)

        return imagenes

    def eliminar_imagenes_por_producto(self, producto_id: str) -> None:
        relaciones = self.productoImagenRepository.get_by_producto(producto_id)

        for rel in relaciones:
            imagen = self.imagenRepository.get_by_id(rel.imagen_id)
            if imagen:
                self.storage.delete(imagen.path)
                self.imagenRepository.delete(imagen.imagen_id)

        self.productoImagenRepository.delete_by_producto(producto_id)