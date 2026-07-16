from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from app.config.database import Base


class NavItem(Base):
    __tablename__ = "nav_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True, comment="唯一标识（路由 name）")
    path = Column(String(255), nullable=False, comment="路由路径（如 /about）")
    title = Column(String(100), nullable=False, comment="菜单显示文字")
    icon = Column(String(100), comment="图标类名或 emoji")
    sort_order = Column(Integer, nullable=False, default=0, server_default="0", comment="排序")
    parent_id = Column(Integer, nullable=False, default=0, server_default="0", comment="父菜单 ID，0 为顶级")
    status = Column(Integer, nullable=False, default=1, server_default="1", comment="0-禁用，1-启用")
    is_hidden = Column(Integer, nullable=False, default=0, server_default="0", comment="0-显示，1-隐藏")
    created_at = Column(DateTime, default=datetime.now, comment="创建时间")
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")
