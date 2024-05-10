from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base

class Busselton(Base):
    __tablename__ = 'busselton'

    id = Column(Integer, primary_key=True)
    application_number = Column(String(128), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    address = Column(Text, nullable=True)
    legal = Column(Text, nullable=True)
    determined_date = Column(Integer, nullable=True)
    decision = Column(String(512), nullable=True)
    cost = Column(String(512), nullable=True)
    days = Column(String(128), nullable=True)
    complete_date = Column(Integer, nullable=True)
    _tid = Column(String(255), nullable=True, server_default=None)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())