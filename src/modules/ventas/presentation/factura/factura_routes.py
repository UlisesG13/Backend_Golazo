from fastapi import APIRouter, Depends, HTTPException, status
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
def create_factura(
    request: CreateFacturaRequestDTO,
    use_case: CreateFactura = Depends(get_create_factura)
):
    try:
        return use_case.execute(request.pedido_id, request.datos_fiscales_receptor)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/", response_model=List[FacturaResponseDTO])
def get_all(use_case: GetAll = Depends(get_all_facturas)):
    return use_case.execute()


@router.get("/{factura_id}", response_model=FacturaResponseDTO)
def get_by_id(factura_id: int, use_case: GetById = Depends(get_factura_by_id)):
    try:
        return use_case.execute(factura_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/folio/{folio}", response_model=FacturaResponseDTO)
def get_by_folio(folio: str, use_case: GetByFolio = Depends(get_factura_by_folio)):
    try:
        return use_case.execute(folio)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/usuario/{usuario_id}", response_model=List[FacturaResponseDTO])
def get_by_usuario(usuario_id: str, use_case: GetByUsuario = Depends(get_facturas_by_usuario)):
    return use_case.execute(usuario_id)


@router.patch("/{factura_id}/status", response_model=FacturaResponseDTO)
def change_status(
    factura_id: int,
    request: ChangeStatusRequestDTO,
    use_case: ChangeStatus = Depends(get_change_factura_status)
):
    try:
        try:
            nuevo_estado = EstadoFactura(request.estado.upper())
        except ValueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Estado inválido")
            
        return use_case.execute(factura_id, nuevo_estado)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{factura_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_factura_route(factura_id: int, use_case: DeleteFactura = Depends(get_delete_factura)):
    try:
        use_case.execute(factura_id)
        return None
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
