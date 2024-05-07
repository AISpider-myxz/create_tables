from sqlalchemy import Column, String, Text, Integer, func, DateTime
from .metadata_base import Base

class Monash(Base):
    __tablename__ = 'monash'

    id = Column(Integer, primary_key=True)
    application_number = Column(String(512), nullable=False, unique=True)
    loged = Column(Integer, nullable=True)
    status = Column(String(512), nullable=True)
    current_decision = Column(String(512), nullable=True)
    description = Column(String(512), nullable=True)
    decision_date = Column(Integer, nullable=True)
    decision_type = Column(String(512), nullable=True)
    decision_lssuedby = Column(String(512), nullable=True)
    location = Column(String(512), nullable=True)
    application_date = Column(Integer, nullable=True)
    application_type = Column(String(512), nullable=True)
    _tid = Column(String(255), nullable=False, server_default=None)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())