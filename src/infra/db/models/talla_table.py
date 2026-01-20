from sqlalchemy import Column, Integer, String
from src.infra.db.database import Base

class TallaTable(Base):
    __tablename__ = "talla"

    talla_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
