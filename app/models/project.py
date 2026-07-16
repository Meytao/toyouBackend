from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime

from app.config.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), comment="项目名称")
    description = Column(Text, comment="项目描述")
    cover = Column(String(500), comment="封面图")
    url = Column(String(500), comment="项目链接")
    sort_order = Column(Integer, default=0, server_default="0", comment="排序")
    created_at = Column(DateTime, default=datetime.now, comment="创建时间")
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")
