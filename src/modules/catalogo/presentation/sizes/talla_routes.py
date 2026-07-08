from fastapi import APIRouter, status
from fastapi.params import Depends

from src.modules.catalogo.app.sizes import GetAllTallas, CreateTalla, GetTallaById, UpdateTalla, DeleteTalla, \
    AsociarTalla, GetPTallaById, GetTallasByProducto, DesasociarTalla
from src.modules.catalogo.presentation.sizes.talla_dependencies import get_all_tallas, create_talla, get_talla_by_id, \
    update_talla, delete_talla, asociar_talla, get_ptalla_by_id, get_tallas_by_producto, desasociar_talla
from src.modules.catalogo.presentation.sizes.talla_dto import TallaDTO, TallaCreateDTO, TallaUpdateDTO, \
    ProductoTallaDTO, ProductoTallaCreateDTO

router = APIRouter()


@router.get("", response_model=list[TallaDTO])
async def get_all_tallas(
        uc: GetAllTallas = Depends(get_all_tallas)
):
    return await uc.execute()


@router.post("", response_model=TallaDTO, status_code=status.HTTP_201_CREATED)
async def create_talla(
        dto: TallaCreateDTO,
        uc: CreateTalla = Depends(create_talla)
):
    return await uc.execute(dto)


@router.get("/{talla_id}", response_model=TallaDTO)
async def get_talla_by_id(
        talla_id: int,
        uc: GetTallaById = Depends(get_talla_by_id)
):
    return await uc.execute(talla_id)


@router.put("/{talla_id}", response_model=TallaDTO)
async def update_talla(
        talla_id: int,
        dto: TallaUpdateDTO,
        uc: UpdateTalla = Depends(update_talla)
):
    return await uc.execute(talla_id, dto)


@router.delete("/{talla_id}", status_code=204)
async def delete_talla(
        talla_id: int,
        uc: DeleteTalla = Depends(delete_talla)
):
    await uc.execute(talla_id)


# RUTAS DE TALLAS Y PRODUCTOS
@router.post("/productos", response_model=ProductoTallaDTO, status_code=status.HTTP_201_CREATED)
async def assign_talla_to_producto(
        dto: ProductoTallaCreateDTO,
        uc: AsociarTalla = Depends(asociar_talla),
):
    return await uc.execute(dto)


@router.get("/productos/detalles/{p_talla_id}", response_model=ProductoTallaDTO)
async def get_producto_talla_by_id(
        p_talla_id: int,
        uc: GetPTallaById = Depends(get_ptalla_by_id),
):
    return await uc.execute(p_talla_id)


@router.get("/productos/{producto_id}", response_model=list[TallaDTO])
async def get_tallas_by_producto(
        producto_id: str,
        uc: GetTallasByProducto = Depends(get_tallas_by_producto),
):
    return await uc.execute(producto_id)


@router.delete("/productos/{producto_id}/{talla_id}", status_code=204)
async def remove_talla_from_producto(
        producto_id: str,
        talla_id: int,
        uc: DesasociarTalla = Depends(desasociar_talla),
):
    return await uc.execute(producto_id, talla_id)
