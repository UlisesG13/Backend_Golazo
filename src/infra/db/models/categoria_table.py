from sqlalchemy import Column, ForeignKey, Integer, String
from src.infra.db.database import Base

class CategoriaTable(Base):
    __tablename__ = "categoria"

    categoria_id = Column(Integer, primary_key=True, autoincrement=True)
    seccion_id = Column(Integer, ForeignKey("seccion.seccion_id"), nullable=False)
    nombre = Column(String, nullable=False)
