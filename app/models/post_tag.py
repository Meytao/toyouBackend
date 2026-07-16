from sqlalchemy import Column, Integer, ForeignKey, Index

from app.config.database import Base


class PostTag(Base):
    __tablename__ = "post_tags"

    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True, comment="文章 ID（外键）")
    tag_id = Column(Integer, ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True, comment="标签 ID（外键）")

    __table_args__ = (
        Index("idx_tag", "tag_id"),
    )
