from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.models.categoria_model import CategoriaModel
from src.domain.ports.categoria_port import CategoriaPort
from src.infra.db.models.categoria_table import CategoriaTable 
from src.core.exceptions import NotFoundError

class CategoriaRepository(CategoriaPort):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def _to_domain(self, r: CategoriaTable) -> CategoriaModel:
        return CategoriaModel(
            categoria_id=r.categoria_id,
            nombre=r.nombre,
            seccion_id=r.seccion_id
        )
    
    def get_categoria_by_id(self, categoria_id: int) -> Optional[CategoriaModel]:
        categoria = self.db_session.query(CategoriaTable).filter_by(categoria_id=categoria_id).first()
        if categoria:
            return self._to_domain(categoria)
        return None
    
    def get_categorias(self) -> List[CategoriaModel]:
        categorias = self.db_session.query(CategoriaTable).all()
        return [self._to_domain(c) for c in categorias]
    
    def get_categorias_by_seccion(self, seccion_id: int) -> List[CategoriaModel]:
        categorias = self.db_session.query(CategoriaTable).filter_by(seccion_id=seccion_id).all()
        return [self._to_domain(c) for c in categorias]
    
    def create_categoria(self, categoria: CategoriaModel) -> CategoriaModel:
        nueva_categoria = CategoriaTable(
            nombre=categoria.nombre,
            seccion_id=categoria.seccion_id
        )
        self.db_session.add(nueva_categoria)
        self.db_session.commit()
        self.db_session.refresh(nueva_categoria)
        return self._to_domain(nueva_categoria)
    
    def update_categoria(self, categoria_id: int, categoria: CategoriaModel) -> CategoriaModel:
        categoria_db = self.db_session.query(CategoriaTable).filter_by(categoria_id=categoria_id).first()
        if not categoria_db:
            raise NotFoundError(f"Categoria with ID {categoria_id} not found")
        
        categoria_db.nombre = categoria.nombre
        categoria_db.seccion_id = categoria.seccion_id
        
        self.db_session.commit()
        self.db_session.refresh(categoria_db)
        return self._to_domain(categoria_db)
    
    def delete_categoria(self, categoria_id: int) -> None:
        categoria_db = self.db_session.query(CategoriaTable).filter_by(categoria_id=categoria_id).first()
        if not categoria_db:
            raise NotFoundError(f"Categoria with ID {categoria_id} not found")
        
        self.db_session.delete(categoria_db)
        self.db_session.commit()