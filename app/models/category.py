from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from app.config.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), comment="分类名称")
    slug = Column(String(100), unique=True, comment="URL 友好标识")
    description = Column(String(255), comment="分类描述")
    icon = Column(String(50), comment="图标")
    sort_order = Column(Integer, default=0, server_default="0", comment="排序")
    created_at = Column(DateTime, default=datetime.now, comment="创建时间")
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")
