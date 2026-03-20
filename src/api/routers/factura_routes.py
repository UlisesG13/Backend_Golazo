from fastapi import APIRouter, Depends
from typing import List
from src.core.security import crear_token
from src.usecases.factura_uescase import FacturaUsecases
from src.core.dependency_inyection.factura_di import get_factura_service
from src.api.schemas.factura_dto import FacturaDTO, FacturaCreateDTO, FacturaUpdateDTO

router = APIRouter()

@router.post("", response_model=FacturaDTO)
def crear_factura(data: FacturaCreateDTO, service: FacturaUsecases = Depends(get_factura_service)):
    factura = service.generar_factura(data)
    return factura

@router.get("", response_model=List[FacturaDTO])
def listar_facturas(service: FacturaUsecases = Depends(get_factura_service)):
    facturas = service.obtener_facturas()
    return facturas

@router.get("/folio/{folio}", response_model=FacturaDTO)
def obtener_factura_folio(folio: str, service: FacturaUsecases = Depends(get_factura_service)):
    factura = service.obtener_factura_por_folio(folio)
    return factura

@router.get("/{factura_id}", response_model=FacturaDTO)
def obtener_factura_id(factura_id: int, service: FacturaUsecases = Depends(get_factura_service)):
    factura = service.obtener_factura_por_id(factura_id)
    return factura

@router.put("/{factura_id}", response_model=FacturaDTO)
def actualizar_factura(factura_id: int, data: FacturaUpdateDTO, service: FacturaUsecases = Depends(get_factura_service)):
    factura = service.actualizar_factura(factura_id, data)
    return factura

@router.delete("/{factura_id}")
def eliminar_factura(factura_id: int, service: FacturaUsecases = Depends(get_factura_service)):
    service.eliminar_factura(factura_id)
    return {"message": f"Factura con ID {factura_id} eliminada exitosamente."}
