from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base


class Bendigo(Base):
    __tablename__ = 'bendigo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    app_id = Column(Integer, nullable=False, unique=True)
    app_num = Column(String(255), nullable=False, unique=True)
    app_type = Column(String(255),nullable=True, server_default=None)
    date_received = Column(Integer, nullable=True)
    proposal = Column(Text,nullable=True)
    status = Column(String(255),nullable=True, server_default=None)
    location_ward = Column(Text,nullable=True, server_default=None)
    people = Column(String(255),nullable=True, server_default=None)

    _tid = Column(String(255), nullable=False, server_default=None)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
