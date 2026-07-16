from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Enum

from app.config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True, comment="登录用户名")
    password_hash = Column(String(255), comment="加密后密码")
    display_name = Column(String(50), comment="显示名称")
    avatar = Column(String(500), comment="头像 URL")
    email = Column(String(100), comment="邮箱")
    role = Column(Enum("admin", "editor", name="user_role"), nullable=False, default="admin", server_default="admin",
                  comment="角色")
    created_at = Column(DateTime, default=datetime.now, comment="注册时间")
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")
