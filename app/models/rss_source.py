from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from app.config.database import Base


class RssSource(Base):
    __tablename__ = "rss_sources"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), comment="订阅源名称（网站/作者名）")
    feed_url = Column(String(500), unique=True, comment="RSS 地址")
    site_url = Column(String(500), comment="网站主页")
    description = Column(String(255), comment="订阅源描述")
    status = Column(Integer, nullable=False, default=1, server_default="1", comment="0-停用，1-启用")
    created_at = Column(DateTime, default=datetime.now, comment="创建时间")
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")
