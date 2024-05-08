from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base

class Launceston(Base):
    __tablename__ = 'launceston'

    id = Column(Integer, primary_key=True)
    application_id = Column(String(128), nullable=False, unique=True)
    description = Column(String(1024), nullable=True)
    app_group = Column(String(512), nullable=True)
    category = Column(String(512), nullable=True)
    app_names = Column(String(512), nullable=True)
    app_status = Column(String(512), nullable=True)
    closing_date = Column(Integer, nullable=True)
    address = Column(String(512), nullable=True)
    legal_description = Column(String(512), nullable=True)
    officer = Column(String(512), nullable=True)
    council_minute = Column(String(512), nullable=True)
    use_class = Column(String(512), nullable=True)
    develop_description = Column(String(512))
    received = Column(Integer, nullable=True)
    decision = Column(Integer, nullable=True)
    valid = Column(Integer, nullable=True)
    stopped = Column(Integer, nullable=True)
    restarted = Column(Integer, nullable=True)
    advertised = Column(Integer, nullable=True)
    meeting = Column(Integer, nullable=True)
    documents = Column(String(1024), nullable=True)
    _tid = Column(String(255), nullable=False, server_default=None)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())