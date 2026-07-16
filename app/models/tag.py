from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from app.config.database import Base


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), comment="标签名")
    slug = Column(String(100), unique=True, comment="标签别名")
    created_at = Column(DateTime, default=datetime.now, comment="创建时间")
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")
