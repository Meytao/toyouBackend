from sqlalchemy import Column, Integer, ForeignKey

from app.config.database import Base


class ProjectTech(Base):
    __tablename__ = "project_techs"

    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), primary_key=True,
                        comment="项目 ID（外键）")
    tech_stack_id = Column(Integer, ForeignKey("tech_stacks.id", ondelete="CASCADE"), primary_key=True,
                           comment="技术栈 ID（外键）")
