from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base

class Vincent(Base):
    __tablename__ = 'vincent'

    id = Column(Integer, primary_key=True)
    app_number = Column(String(128), nullable=False, unique=True)
    address = Column(String(512), nullable=True)
    data_received = Column(Integer, nullable=True)
    date_advertised = Column(Integer, nullable=True)
    agenda = Column(String(512), nullable=True)
    minute = Column(String(512), nullable=True)
    determination = Column(String(512), nullable=True)
    type_work = Column(String(512), nullable=True)
    date_lodged = Column(Integer, nullable=True)
    cost_work = Column(String(512), nullable=True)
    planning_officer = Column(String(512), nullable=True)
    determination_details = Column(String(512), nullable=True)
    determination_date = Column(Integer, nullable=True)
    fee_type = Column(String(512), nullable=True)
    _tid = Column(String(255), nullable=False, server_default=None)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())