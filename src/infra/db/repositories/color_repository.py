from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.models.color_model import ColorModel
from src.domain.ports.color_port import ColorPort
from src.infra.db.models.color_table import ColorTable
from src.core.exceptions import NotFoundError

class ColorRepository(ColorPort):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def _to_domain(self, r: ColorTable) -> ColorModel:
        return ColorModel(
            color_id=r.color_id,
            nombre=r.nombre,
        )
    
    def create_color(self, color: ColorModel) -> ColorModel:
        db_color = ColorTable(
            nombre=color.nombre,
        )
        self.db_session.add(db_color)
        self.db_session.commit()
        self.db_session.refresh(db_color)
        return self._to_domain(db_color)
    
    def get_color_by_id(self, color_id: int) -> ColorModel:
        db_color = self.db_session.query(ColorTable).filter(ColorTable.color_id == color_id).first()
        if not db_color:
            raise NotFoundError(f"Color con ID {color_id} no encontrado")
        return self._to_domain(db_color)
    
    def get_all_colors(self) -> List[ColorModel]:
        db_colors = self.db_session.query(ColorTable).all()
        return [self._to_domain(r) for r in db_colors]
    
    def update_color(self, color_id: int, color: ColorModel) -> ColorModel:
        db_color = self.db_session.query(ColorTable).filter(ColorTable.color_id == color_id).first()
        if not db_color:
            raise NotFoundError(f"Color con ID {color_id} no encontrado")
        db_color.nombre = color.nombre
        self.db_session.commit()
        self.db_session.refresh(db_color)
        return self._to_domain(db_color)
    
    def delete_color(self, color_id: int) -> bool:
        db_color = self.db_session.query(ColorTable).filter(ColorTable.color_id == color_id).first()
        if not db_color:
            raise NotFoundError(f"Color con ID {color_id} no encontrado")
        self.db_session.delete(db_color)
        self.db_session.commit()
        return True