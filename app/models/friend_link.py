from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from app.config.database import Base


class FriendLink(Base):
    __tablename__ = "friend_links"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), comment="网站名称")
    url = Column(String(500), comment="网址")
    description = Column(String(255), comment="简介")
    avatar = Column(String(500), comment="头像 URL")
    sort_order = Column(Integer, default=0, server_default="0", comment="排序")
    created_at = Column(DateTime, default=datetime.now, comment="提交时间")
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")
