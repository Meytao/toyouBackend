from sqlalchemy import Column, Integer, String

from app.config.database import Base


class TechStack(Base):
    __tablename__ = "tech_stacks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, comment="技术名称")
