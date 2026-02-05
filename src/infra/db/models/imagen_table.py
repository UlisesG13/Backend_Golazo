from sqlalchemy import Column, Integer, String
from src.infra.db.database import Base

class ImagenTable(Base):
    __tablename__ = "imagen"
    
    imagen_id = Column(Integer, primary_key=True, autoincrement=True)
    path = Column(String, nullable=False)
    orden = Column(Integer, nullable=False)