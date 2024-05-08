from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base

class Wenworth(Base):
    __tablename__ = 'wentworth'

    id = Column(Integer, primary_key=True)
    application_id = Column(String(128), nullable=False, unique=True)
    applicant = Column(String(512), nullable=True)
    address = Column(String(512), nullable=True)
    proposal = Column(String(512), nullable=True)
    notification = Column(String(512), nullable=True)
    description = Column(String(512), nullable=True)
    value_exgst = Column(String(512), nullable=True)
    determination_date = Column(Integer, nullable=True)
    active_days = Column(String(512), nullable=True)
    _tid = Column(String(255), nullable=False, server_default=None)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())