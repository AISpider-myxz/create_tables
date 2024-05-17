from sqlalchemy import Column, String, Text, Integer, DateTime, func, UniqueConstraint
from .metadata_base import Base


class Midcoast(Base):

    __tablename__ = 'midcoast'

    id = Column(Integer, primary_key=True, autoincrement=True)
    application_id = Column(String(255), unique=True, nullable=False)
    description = Column(Text, nullable=True, server_default=None)
    application_group = Column(String(255), nullable=True, server_default=None)
    category = Column(String(255), nullable=True, server_default=None)
    sub_category = Column(Text, nullable=True, server_default=None)
    status = Column(String(255), nullable=True, server_default=None)
    lodged_date = Column(Integer, nullable=True,)
    stage = Column(String(255), nullable=True, server_default=None)
    estimated_cost = Column(String(255), nullable=True, server_default=None)
    address = Column(String(255), nullable=True, server_default=None)
    documents = Column(Text, nullable=True, server_default=None)
    _tid = Column(String(255), nullable=False, server_default=None)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
