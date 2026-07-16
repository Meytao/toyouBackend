from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey, Index, JSON

from app.config.database import Base


class Moment(Base):
    __tablename__ = "moments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    source_id = Column(Integer, ForeignKey("rss_sources.id", ondelete="CASCADE"), comment="订阅源 ID（外键）")
    title = Column(String(200), comment="RSS 条目标题")
    link = Column(String(500), nullable=False, unique=True, comment="原文链接（用于去重）")
    content = Column(Text, comment="内容摘要/全文")
    content_type = Column(Enum("text", "html", name="moment_content_type"), nullable=False, default="text",
                          server_default="text", comment="内容格式")
    images = Column(JSON, comment="提取的图片 URL 数组")
    published_at = Column(DateTime, comment="原作者发布时间")
    status = Column(Enum("unread", "read", "featured", name="moment_status"), nullable=False, default="unread",
                    server_default="unread", comment="状态：未读/已读/精选")
    created_at = Column(DateTime, default=datetime.now, comment="入库时间")
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")

    __table_args__ = (
        Index("idx_source_pub", "source_id", "published_at"),
        Index("idx_status_pub", "status", "published_at"),
    )
