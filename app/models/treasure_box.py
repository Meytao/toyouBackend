from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Enum

from app.config.database import Base


class TreasureBox(Base):
    __tablename__ = "treasure_box"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Enum("text", "image", "resource", name="treasure_box_type"), comment="类型")
    title = Column(String(100), comment="标题")
    description = Column(String(255), comment="描述")
    icon = Column(String(50), comment="图标")
    url = Column(String(500), comment="跳转链接")
    cover = Column(String(500), comment="封面图")
    sort_order = Column(Integer, default=0, server_default="0", comment="排序")
    created_at = Column(DateTime, default=datetime.now, comment="创建时间")
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")
