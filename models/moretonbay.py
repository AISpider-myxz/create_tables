"""
Create your db model here
"""
from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base



class MoretonbayDAList(Base):
    __tablename__ = 'moretonbay_da_list'
    id = Column(Integer, primary_key=True)

    da_number = Column(String(255), nullable=False,unique=True)
    lodged = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)

    _tid = Column(String(255), nullable=False, server_default=None)
    created_at = Column(DateTime, server_default=func.now())
    update_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
