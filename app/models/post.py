from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, Index

from app.config.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False, comment="标题")
    slug = Column(String(200), nullable=False, unique=True, comment="URL 别名")
    excerpt = Column(String(500), comment="摘要")
    cover = Column(String(500), comment="封面图")
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="SET NULL"), comment="分类 ID（外键）")
    author_id = Column(Integer, ForeignKey("users.id", ondelete="RESTRICT"), nullable=False,
                       comment="作者用户 ID（外键）")
    content = Column(String(500), nullable=False, comment="正文 .md 文件相对路径，如 /context/{uuid}/index.md")
    status = Column(Enum("draft", "published", name="post_status"), nullable=False, default="draft",
                    server_default="draft", comment="状态")
    published_at = Column(DateTime, comment="发布时间")
    read_minutes = Column(Integer, default=0, server_default="0", comment="预计阅读分钟")
    created_at = Column(DateTime, default=datetime.now, comment="创建时间")
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")

    __table_args__ = (
        Index("idx_status_pub", "status", "published_at"),
        Index("idx_category", "category_id"),
        Index("idx_author", "author_id"),
    )
