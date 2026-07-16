from datetime import datetime

from sqlalchemy import Column, String, Text, DateTime

from app.config.database import Base


class Setting(Base):
    __tablename__ = "settings"

    key = Column(String(50), primary_key=True, comment="配置键")
    value = Column(Text, comment="配置值")
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")
