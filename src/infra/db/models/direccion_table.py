from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from src.infra.db.database import Base

class DireccionTable(Base):
    __tablename__ = "direccion"
    
    direccion_id = Column(Integer, primary_key=True, autoincrement=True)
    calle = Column(String, nullable=False)
    colonia = Column(String, nullable=False)
    calle_uno = Column(String, nullable=True)
    calle_dos = Column(String, nullable=True)
    numero_casa = Column(Integer, nullable=True)
    codigo_postal = Column(String, nullable=True)
    referencia = Column(String, nullable=True)
    usuario_id = Column(String, ForeignKey("usuario.usuario_id"), nullable=False)
    is_primary = Column(Boolean, default=False)
