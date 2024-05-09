from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base

class Yass(Base):
    __tablename__ = 'yass'

    id = Column(Integer, primary_key=True)
    application_id = Column(String(128), nullable=False, unique=True)
    close_date = Column(String(512), nullable=True)
    applicant_name = Column(String(512), nullable=True)
    address = Column(String(512), nullable=True)
    description = Column(String(512), nullable=True)
    documents = Column(Text, nullable=True)
    payable = Column(String(512), nullable=True)
    folio_identifier = Column(String(512), nullable=True)
    street_number = Column(String(512), nullable=True)
    locality = Column(String(512), nullable=True)
    status = Column(String(512), nullable=True)
    determination_date = Column(String(128), nullable=True)
    time_days = Column(String(512), nullable=True)
    _tid = Column(String(255), nullable=False, server_default=None)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())