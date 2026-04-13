from typing import List
from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.params import File
from src.usecases.imagen_usecase import ImagenUsecases
from src.core.dependency_inyection.imagen_di import get_imagen_service
from src.api.schemas.imagen_dto import ImagenCreateDTO, ImagenDTO, ProductoImagenCreateDTO, ProductoImagenDTO
from src.core.config import settings

router = APIRouter(prefix="/api/imagenes", tags=["imagenes"])

def build_public_url(path: str) -> str:
    return (
        f"{settings.SUPABASE_URL}"
        f"/storage/v1/object/public/"
        f"{settings.SUPABASE_BUCKET}/"
        f"{path}"
    )

@router.post("/", response_model=ImagenDTO, status_code=status.HTTP_201_CREATED)
async def subir_imagen(
    dto: ImagenCreateDTO = Depends(ImagenCreateDTO.as_form),
    file: UploadFile = File(...),
    service: ImagenUsecases = Depends(get_imagen_service)
):
    content = await file.read()
    file.filename = file.filename.replace(" ", "_")
    imagen = service.subir_imagen(
        imagen_data=content,
        filename=file.filename,
        orden=dto.orden
    )
    return ImagenDTO(
        imagen_id=imagen.imagen_id,
        path=build_public_url(imagen.path),
        orden=imagen.orden
    )

@router.get("/producto/{producto_id}", response_model=List[ImagenDTO])
def get_imagenes_por_producto(
    producto_id: str,
    service: ImagenUsecases = Depends(get_imagen_service)
):
    imagenes = service.get_imagenes_por_producto(producto_id)

    productoImagenes = []
    for img in imagenes:
        productoImagenes.append(
            ImagenDTO(
                imagen_id=img.imagen_id,
                path=build_public_url(img.path),
                orden=img.orden
            )
        )
    return productoImagenes

@router.post("/producto", response_model=ProductoImagenDTO, status_code=status.HTTP_201_CREATED)
def asociar_imagen(
    dto: ProductoImagenCreateDTO,
    service: ImagenUsecases = Depends(get_imagen_service)
):
    relacion = service.asociar_imagen_a_producto(dto)
    return relacion

@router.delete("/{imagen_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_imagen(
    imagen_id: int,
    service: ImagenUsecases = Depends(get_imagen_service)
):
    service.eliminar_imagen(imagen_id)

@router.delete("/producto/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_imagenes_producto(
    producto_id: str,
    service: ImagenUsecases = Depends(get_imagen_service)
):
    service.eliminar_imagenes_por_producto(producto_id)
