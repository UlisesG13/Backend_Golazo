from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.models.imagen_model import ImagenModel
from src.domain.ports.imagen_port import ImagenPort
from src.infra.db.models.imagen_table import ImagenTable
from src.core.exceptions import NotFoundError

class ImagenRepository(ImagenPort):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def _to_domain(self, r: ImagenTable) -> ImagenModel:
        return ImagenModel(
            imagen_id=r.imagen_id,
            path=r.path,
            orden=r.orden
        )
    
    def create(self, imagen: ImagenModel) -> ImagenModel:
        nueva_imagen = ImagenTable(
            path=imagen.path,
            orden=imagen.orden
        )
        self.db_session.add(nueva_imagen)
        self.db_session.commit()
        self.db_session.refresh(nueva_imagen)
        return self._to_domain(nueva_imagen)
    
    def get_by_id(self, imagen_id: int) -> Optional[ImagenModel]:
        imagen_record = self.db_session.query(ImagenTable).filter_by(imagen_id=imagen_id).first()
        if imagen_record is None:
            return None
        return self._to_domain(imagen_record)
    
    def delete(self, imagen_id: int) -> None:
        imagen_record = self.db_session.query(ImagenTable).filter_by(imagen_id=imagen_id).first()
        if imagen_record is None:
            raise NotFoundError(f"Imagen with id {imagen_id} not found")
        self.db_session.delete(imagen_record)
        self.db_session.commit()