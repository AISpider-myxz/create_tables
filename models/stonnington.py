from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base

class Stonnington(Base):
    __tablename__ = 'stonnington'

    id = Column(Integer, primary_key=True)
    app_number = Column(String(128), nullable=True, unique=True)
    lodged = Column(Integer, nullable=True)
    site_address = Column(Text, nullable=True)
    reason_for_permit = Column(Text, nullable=True)
    status = Column(String(128), nullable=True)
    vicsmart = Column(String(128), nullable=True)
    revision = Column(String(128), nullable=True)
    notice_of_application = Column(Text, nullable=True)
    jurisdiction = Column(String(128), nullable=True)
    decision_date = Column(Integer, nullable=True)
    decision = Column(String(128), nullable=True)
    final_decision_date = Column(Integer, nullable=True)
    final_decision = Column(String(128), nullable=True)
    amendment = Column(Text, nullable=True)
    site_addresses = Column(Text, nullable=True)
    tribunal_decision = Column(Text, nullable=True)
    ward = Column(String(128), nullable=True)
    _tid = Column(String(255), nullable=False, server_default=None)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())