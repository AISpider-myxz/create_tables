from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base


class Perth(Base):
    __tablename__ = 'perth'

    id = Column(Integer, primary_key=True, autoincrement=True)

    app_num = Column(String(255), nullable=False, unique=True)
    detail_text = Column(Text,nullable=True, server_default=None)
    location = Column(Text, nullable=True, server_default=None)
    decision_ = Column(String(255),nullable=True,server_default=None)
    decision_date = Column(String(255),nullable=True,server_default=None)
    received_date = Column(String(255),nullable=True,server_default=None)
    cost = Column(String(255),nullable=True, server_default=None)
    app_type = Column(String(255),nullable=True, server_default=None)

    _tid = Column(String(255), nullable=False, server_default=None)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
