from fastapi import APIRouter, Depends, status
from typing import List
from src.modules.ventas.domain.models import EstadoFactura
from src.modules.ventas.presentation.factura.factura_dto import (
    FacturaResponseDTO, CreateFacturaRequestDTO, ChangeStatusRequestDTO
)
from src.modules.ventas.presentation.factura.factura_di import (
    get_all_facturas, get_factura_by_id, get_factura_by_folio, get_facturas_by_usuario,
    get_create_factura, get_change_factura_status, get_delete_factura
)
from src.modules.ventas.app.factura import (
    GetAll, GetById, GetByFolio, GetByUsuario, CreateFactura, ChangeStatus, DeleteFactura
)

router = APIRouter()


@router.post("/", response_model=FacturaResponseDTO, status_code=status.HTTP_201_CREATED)
async def create_factura(
    request: CreateFacturaRequestDTO,
    use_case: CreateFactura = Depends(get_create_factura)
):
    return await use_case.execute(request.pedido_id, request.datos_fiscales_receptor)


@router.get("/", response_model=List[FacturaResponseDTO])
async def get_all(use_case: GetAll = Depends(get_all_facturas)):
    return await use_case.execute()


@router.get("/{factura_id}", response_model=FacturaResponseDTO)
async def get_by_id(factura_id: int, use_case: GetById = Depends(get_factura_by_id)):
    return await use_case.execute(factura_id)


@router.get("/folio/{folio}", response_model=FacturaResponseDTO)
async def get_by_folio(folio: str, use_case: GetByFolio = Depends(get_factura_by_folio)):
    return await use_case.execute(folio)


@router.get("/usuario/{usuario_id}", response_model=List[FacturaResponseDTO])
async def get_by_usuario(usuario_id: str, use_case: GetByUsuario = Depends(get_facturas_by_usuario)):
    return await use_case.execute(usuario_id)


@router.patch("/{factura_id}/status", response_model=FacturaResponseDTO)
async def change_status(
    factura_id: int,
    request: ChangeStatusRequestDTO,
    use_case: ChangeStatus = Depends(get_change_factura_status)
):
    nuevo_estado = EstadoFactura(request.estado.upper())
    return await use_case.execute(factura_id, nuevo_estado)


@router.delete("/{factura_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_factura_route(factura_id: int, use_case: DeleteFactura = Depends(get_delete_factura)):
    await use_case.execute(factura_id)
    return None
