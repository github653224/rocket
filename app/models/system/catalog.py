from sqlalchemy import Column, String, INT, UniqueConstraint

from app.base.model import RocketBaseModel


class Catalog(RocketBaseModel):
    __tablename__ = 'sys_catalog'

    name = Column(String(32), nullable=False, comment='目录名称')
    parent_id = Column(INT, comment='父级id')
    project_id = Column(INT, nullable=False, comment='项目id')

    # 联合索引，防止同一层次出现同名目录
    __table_args__ = (
        UniqueConstraint('project_id', 'name', 'parent_id'),
    )

    def __init__(self, form):
        self.name = form.name
        self.parent_id = form.parent_id
        self.project_id = form.project_id