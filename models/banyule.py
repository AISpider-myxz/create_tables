from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base


class Banyule(Base):
    __tablename__ = 'banyule_city_council'

    id = Column(Integer, primary_key=True, autoincrement=True)
    app_id = Column(String(255), nullable=False, unique=True)
    applications = Column(Text, nullable=True, server_default=None)
    amendments = Column(Text, nullable=True, server_default=None)
    description = Column(Text, nullable=True, server_default=None)
    location = Column(Text, nullable=True, server_default=None)
    docs = Column(Text, nullable=True, server_default=None)

    _tid = Column(String(255), nullable=False, server_default=None)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
