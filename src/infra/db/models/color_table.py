from sqlalchemy import Column, Integer, String
from src.infra.db.database import Base

class ColorTable(Base):
    __tablename__ = "color"

    color_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
