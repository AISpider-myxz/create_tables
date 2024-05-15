from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base

class Mandurah(Base):
    __tablename__ = 'mandurah'

    id = Column(Integer, primary_key=True)
    app_number = Column(String(128), nullable=False, unique=True)
    ApplicationType = Column(String(512), nullable=True)
    SiteName = Column(String(512), nullable=True)
    Description = Column(Text, nullable=True)
    Lodged = Column(Integer, nullable=True)
    Accepted = Column(Integer, nullable=True)
    Determined = Column(String(512), nullable=True)
    Effective = Column(Integer, nullable=True)
    ModificationCategory = Column(String(512), nullable=True)
    development = Column(String(512), nullable=True)
    NSWPlanningPortal = Column(String(512), nullable=True)
    notification = Column(String(512), nullable=True)
    dwellinghouse = Column(String(512), nullable=True)
    Lapsed = Column(Integer, nullable=True)
    Completed = Column(Integer, nullable=True)
    progress = Column(Text, nullable=True)
    people = Column(String(512), nullable=True)
    associations = Column(Text, nullable=True)
    documents = Column(Text, nullable=True)
    _tid = Column(String(255), nullable=False, server_default=None)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())